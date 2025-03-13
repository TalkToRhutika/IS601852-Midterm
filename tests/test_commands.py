"""Test commands"""

from decimal import Decimal
import os
import sys
import logging
import pytest
from unittest import mock
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.history import HistoryCommand
from app.plugins.menu import MenuCommand
from app.plugins.exit import ExitCommand
from app.commands import CommandHandler

@pytest.mark.parametrize("a, b, command, expected", [
    (Decimal('10'), Decimal('5'), AddCommand, Decimal('15')),  # Test addition
    (Decimal('10'), Decimal('5'), SubtractCommand, Decimal('5')),  # Test subtraction
    (Decimal('10'), Decimal('5'), MultiplyCommand, Decimal('50')),  # Test multiplication
    (Decimal('10'), Decimal('2'), DivideCommand, Decimal('5')),  # Test division
    (Decimal('10.5'), Decimal('0.5'), AddCommand, Decimal('11.0')),  # Test addition with decimals
    (Decimal('10.5'), Decimal('0.5'), SubtractCommand, Decimal('10.0')),  # Test subtraction with decimals
    (Decimal('10.5'), Decimal('2'), MultiplyCommand, Decimal('21.0')),  # Test multiplication with decimals
    (Decimal('10'), Decimal('0.5'), DivideCommand, Decimal('20')),  # Test division with decimals
])

# pylint: disable=invalid-name
def test_calculation_commands(a, b, command, expected):
    """
    Test calculation commands with various scenarios.

    This test ensures that the command class correctly performs the arithmetic operation
    (specified by the 'command' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.

    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        command (function): The arithmetic command to perform.
        expected (Decimal): The expected result of the operation.
    """
    assert command().evaluate(a, b) == expected, f"Failed {command.__name__} command with {a} and {b}"  # Perform the operation and assert that the result matches the expected value.

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ZeroDivisionError
    """
    with pytest.raises(ZeroDivisionError, match="Cannot divide by 0!"):  # Expect a ZeroDivisionError to be raised.
        DivideCommand().evaluate(Decimal(3), Decimal(0))  # Attempt to perform the calculation, which should trigger the ZeroDivisionError.

@pytest.fixture
def history_command(tmp_path):
    """ history_command """
    handler = CommandHandler()
    history_file = tmp_path / "test_history.log"
    csv_file = tmp_path / "test_history.csv"
    return HistoryCommand(handler, str(history_file), str(csv_file))

@pytest.fixture
def command():
    return HistoryCommand(mock.MagicMock())

def test_execute(command):
    command.execute("show")  # Calls show_history()
    command.execute("clear")  # Calls clear_history()
    command.execute("save")  # Calls save_history()
    command.execute("delete", "1")  # Calls delete_history_entry(0)
    command.execute("delete")  # Tests missing index case
    command.execute("delete", "invalid")  # Tests invalid index format
    command.execute("unknown")  # Tests unknown command

def test_history_initial_empty(history_command):
    """ test_history."""
    assert len(history_command.command_handler.history) == 0

def test_add_to_history(history_command):
    """ test_history."""
    history_command.command_handler.history.append("add 2 3 = 5")
    history_command.save_history()
    assert os.path.exists(history_command.csv_file)

def test_delete_valid_entry(history_command):
    """ test_history."""
    history_command.command_handler.history.append("add 2 3 = 5")
    history_command.delete_history_entry(0)
    assert len(history_command.command_handler.history) == 0

def test_delete_invalid_entry(history_command, capsys):
    """ test_history."""
    history_command.delete_history_entry(10)
    captured = capsys.readouterr()
    assert "Invalid index." in captured.out

def test_show_empty_history(history_command, capsys):
    """ test_history."""
    history_command.show_history()
    captured = capsys.readouterr()
    assert "No command history found." in captured.out

def test_clear_history(history_command):
    """ test_history."""
    history_command.command_handler.history.append("add 1 1 = 2")
    history_command.clear_history()
    assert len(history_command.command_handler.history) == 0

def test_invalid_arguments(history_command, capsys):
    """ test_history."""
    history_command.execute("unknown")
    captured = capsys.readouterr()
    assert "Unknown history command." in captured.out

def test_empty_delete_command(history_command, capsys):
    """ test_history."""
    history_command.execute("delete")
    captured = capsys.readouterr()
    assert "Invalid index." in captured.out

def test_out_of_bound_delete(history_command, capsys):
    """ test_history."""
    history_command.command_handler.history = ["add 2 3 = 5"]
    history_command.execute("delete", "10")
    captured = capsys.readouterr()
    assert "Invalid index." in captured.out

def test_valid_delete(history_command, capsys):
    """ test_history."""
    history_command.command_handler.history = ["add 2 3 = 5"]
    history_command.execute("delete", "1")
    captured = capsys.readouterr()
    assert "Deleted entry: add 2 3 = 5" in captured.out
    assert len(history_command.command_handler.history) == 0

def test_save_history_permission_error(command):
    with mock.patch("pandas.DataFrame.to_csv", side_effect=PermissionError("No write access")):
        command.save_history()  # Should log error

def test_save_history_generic_error(command):
    with mock.patch("pandas.DataFrame.to_csv", side_effect=Exception("Unexpected Error")):
        command.save_history()  # Should log general error

def test_clear_history(command):
    command.clear_history()
    assert command.command_handler.history == []

def test_show_history_empty(command, capsys):
    command.command_handler.history = []
    command.show_history()
    captured = capsys.readouterr()
    assert "No command history found." in captured.out

def test_delete_history_entry(command):
    command.command_handler.history = ["add 2 2 = 4", "subtract 3 1 = 2"]
    command.delete_history_entry(0)
    assert command.command_handler.history == ["subtract 3 1 = 2"]

def test_delete_invalid_index(command, capsys):
    command.delete_history_entry(10)
    captured = capsys.readouterr()
    assert "Invalid index." in captured.out

def test_load_history_missing_file(command):
    with mock.patch("os.path.exists", return_value=False):
        command.load_history()
    assert command.command_handler.history == []

def test_load_history_malformed(command):
    with mock.patch("builtins.open", mock.mock_open(read_data="invalid_line")):
        command.load_history()
    assert command.command_handler.history == ["invalid_line"]

@pytest.fixture
def caplog(caplog):
    """ caplog. """
    return caplog

# Test failed CSV save (simulate permission error)
def test_failed_csv_save(history_command, monkeypatch, capsys, caplog):
    """ Test case for test_failed_csv_same."""
    def mock_to_csv(*args, **kwargs):
        raise PermissionError("CSV save failed")
    monkeypatch.setattr("pandas.DataFrame.to_csv", mock_to_csv)

    logging.basicConfig(level=logging.ERROR)

    history_command.save_history()
    captured = capsys.readouterr()

    assert "Failed to save history: CSV save failed" in captured.err
#   assert "ERROR" in caplog_fixture.text #captured.out
    assert any(record.message == "Failed to save history: CSV save failed" for record in caplog.records)
    assert any(record.levelname == "ERROR" for record in caplog.records)

# Ensure CSV file format is correct
def test_csv_content(history_command):
    """ test_history."""
    history_command.command_handler.history = ["add 2 3 = 5"]
    history_command.save_history()
    with open(history_command.csv_file, encoding='utf-8') as f:
        content = f.read()
    assert "Operation,Operand 1,Operand 2,Result" in content
    assert "add,2,3,5" in content

@pytest.fixture
def menu_command():
    """ test_menu."""
    return MenuCommand()

# Verify menu output
def test_menu_display(menu_command, capsys):
    """ test_menu."""
    menu_command.execute()
    captured = capsys.readouterr()

    assert "Available Commands:" in captured.out
    assert "add                : Add two numbers" in captured.out
    assert "exit               : Exit the application" in captured.out

# Test unknown menu command (should gracefully fail)
def test_unknown_command(menu_command, capsys):
    """ test_menu."""
    menu_command.execute("unknown")
    captured = capsys.readouterr()
    assert "Available Commands:" in captured.out

def test_exit_command(monkeypatch):
    """ test_exit."""
    # Mock sys.exit to prevent the program from actually exiting
    def mock_exit(msg):
        assert msg == "Exiting the program..."

    # Monkeypatch sys.exit with the mock function
    monkeypatch.setattr(sys, "exit", mock_exit)

    # Create an instance of ExitCommand and execute it
    exit_command = ExitCommand()
    exit_command.execute()
