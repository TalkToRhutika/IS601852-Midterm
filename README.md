# Advanced Python Calculator Application

## Table of Contents
- [Advanced Python Calculator Application](#advanced-python-calculator-application)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Core Functionalities](#core-functionalities)
  - [Plugin System](#plugin-system)
  - [Calculation History Management (with Pandas)](#calculation-history-management-with-pandas)
  - [Professional Logging Practices](#professional-logging-practices)
  - [Advanced Data Handling with Pandas](#advanced-data-handling-with-pandas)
  - [Design Patterns for Scalable Architecture](#design-patterns-for-scalable-architecture)
  - [Testing and Code Quality](#testing-and-code-quality)
  - [Version Control Best Practices](#version-control-best-practices)
  - [Documentation](#documentation)
  - [Video Showcase](#video-showcase)
  - [Cloning the Repository](#cloning-the-repository)

## Project Overview
This project is an advanced Python-based calculator application, provides a command-line interface (REPL) that supports basic arithmetic operations, manages calculation history, and allows for plugin integration for real-time user interaction. It utilizes Pandas for advanced data management and includes professional logging practices to track application behavior.

## Core Functionalities
The application features a REPL(Read-Eval-Print Loop) to support:
- Execute arithmetic operations: addition, subtraction, multiplication, and division.
- Manage calculation history through commands to show, save, clear, and delete history entries.
- Access extended functionalities via dynamically loaded plugins.

## Plugin System
Create a flexible plugin system for seamless integration of new commands or features:
- Dynamically load and integrate plugins without altering the core application.
- Include a menu command in the REPL to list all available plugin commands.

## Calculation History Management (with Pandas)
Pandas is utilized to manage calculation history effectively. Users can:
- Load and display history from a CSV file.
- Save the current history to a CSV file.
- Clear or delete specific history entries, with these changes reflected in the CSV file.

## Professional Logging Practices
A comprehensive logging system is established to record:
- Detailed application operations and data manipulations.
- Errors and informational messages.
- Different log message severity levels (INFO, WARNING, ERROR) for effective monitoring.

Dynamic logging configuration is supported through environment variables, allowing customization of logging levels and output destinations.

## Advanced Data Handling with Pandas
Pandas is employed for:
- Efficient data reading and writing to CSV files.
- Management of calculation history, ensuring robust data handling.

## Design Patterns for Scalable Architecture
Key design patterns are incorporated to address software design challenges:
- **Facade Pattern**: Simplify complex Pandas data manipulations.
- **Command Pattern**: Structures RELP commands for efficient management.
- **Factory Method, Singleton, and Strategy Patterns**: Enhance code flexibility and scalability.

## Testing and Code Quality
The application achieves a minimum of 90% test coverage using Pytest. Code quality is maintained and verified against PEP 8 standards validated by Pylint.

## Version Control Best Practices
Use logical, well-structured commits. Clearly document feature development and corresponding tests.

## Documentation
Comprehensive documentation is compiled in this README.md, covering setup instructions, usage examples, and an in-depth analysis of architectural decisions, with emphasis on the implementation and impact of chosen design patterns and logging strategy.

## Video Showcase
A video has been created to showcase the features and functionalities of this calculator application. You can watch the video [here](https://drive.google.com/file/d/1QwZ0yXbqtH3Y802n7kaqVLQK9bEFmy9A/view?usp=sharing).

## Cloning the Repository
To clone the repository, use the following command:
```bash
git clone https://github.com/your-username/calculator-app.git