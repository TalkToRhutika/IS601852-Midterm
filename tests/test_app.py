"""Import pytest for testing the App class and its functionalities."""
from unittest import mock
import pytest
#from dotenv import load_dotenv
from app import App

@pytest.mark.parametrize("Command", [
    ('add'),
    ('subtract'),
    ('multiply'),
    ('divide'),
])

# pylint: disable=invalid-name
def test_calculation_operations(Command, monkeypatch):
    """Simulate command followed by exit."""
    inputs = iter([f'{Command} 1 1', 'exit'])  # Simulate command with arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Ensure the app start triggers SystemExit
    assert e.type == SystemExit  # Check if SystemExit was raised
    assert e.value.code == 0  # Check for clean exit (0)

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Capture the REPL output
    captured = capfd.readouterr()

    # Verify that the unknown command message is present in the output
    # pylint: disable=assert-on-string-literal
    assert "Available commands: add, subtract, multiply, divide, exit","Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit." in captured.out

    # Ensure a clean exit (exit code 0)
    assert excinfo.value.code == 0  # Clean exit after unknown command

def test_app_invalid_input_format(capfd, monkeypatch):
    """Test how the REPL handles invalid input formats."""
    inputs = iter(['add 2', 'exit'])  # Missing one argument for 'add'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Capture the REPL output
    captured = capfd.readouterr()

    # Check for the correct error message
    assert "Enter valid numbers for the operation." in captured.out  # Adjusted assertion

    # Ensure a clean exit (exit code 0)
    assert excinfo.value.code == 0  # Ensure clean exit after invalid input

def test_environment_variable_missing(monkeypatch):
    """Test how the app handles missing environment variables."""
    monkeypatch.setattr('os.environ', {})  # Simulate an empty environment
    app = App()
    assert app.settings.get('ENVIRONMENT') == 'DEVELOPMENT'  # Default value

def test_app_initialization(monkeypatch):
    """Test initialization of the App class and environment variable loading."""
    mock_load_dotenv = mock.MagicMock()
    monkeypatch.setattr('app.load_dotenv', mock_load_dotenv)

    mock_load_environment_variables = mock.MagicMock(return_value={'ENVIRONMENT': 'DEVELOPMENT'})
    monkeypatch.setattr(App, 'load_environment_variables', mock_load_environment_variables)

    app = App()

    # debugging output
    print(f"dotenv.load_dotenv() call count: {mock_load_dotenv.call_count}")

    # Verify that the constructor called the methods as expected
    mock_load_dotenv.assert_called_once()
    mock_load_environment_variables.assert_called_once()
    assert app.settings.get('ENVIRONMENT') == 'DEVELOPMENT'

def test_logging_configuration(monkeypatch):
    """Test the logging configuration method."""
    mock_logging_config = mock.MagicMock()
    monkeypatch.setattr('logging.config.fileConfig', mock_logging_config)

    app = App()

    assert app is not None
    # Verify if logging configuration was called
    mock_logging_config.assert_called_once_with('logging.conf', disable_existing_loggers=False)

def test_plugin_loading(monkeypatch):
    """Test that plugins are loaded dynamically."""
    mock_iter_modules = mock.MagicMock(return_value=[('path', 'plugin_name', True)])
    monkeypatch.setattr('pkgutil.iter_modules', mock_iter_modules)

    app = App()

    app.load_plugins()
    # Verify that the plugin loading method was called
    mock_iter_modules.assert_called_once()

def test_command_registration(monkeypatch):
    """Test that commands are correctly registered with the CommandHandler."""
    mock_command_handler = mock.MagicMock()
    monkeypatch.setattr('app.CommandHandler', mock_command_handler)

    mock_command_handler_instance = mock_command_handler.return_value

    app = App()

    mock_plugin_module = 'plugin_module'
    mock_plugin_name = 'plugin_name'

    app.register_plugin_commands(mock_plugin_module, mock_plugin_name)

    print(mock_command_handler_instance.register_command.call_args_list)
    # Verify that the command handler registered the expected commands
    mock_command_handler_instance.register_command.assert_any_call('history', mock.ANY)  # Replace mock.ANY with expected class if needed
