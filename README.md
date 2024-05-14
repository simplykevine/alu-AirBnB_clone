# Airbnb Command-Line Interface (AirbnbCLI)

## Description
This project provides a Python command-line interpreter (AirbnbCLI) for managing Airbnb data, specifically users, places, cities, and other relevant entities. It serves as the foundation for building a more comprehensive Airbnb-like web application.

This project is a comprehensive command-line interpreter application designed to streamline tasks and automate processes. Built with Python, it offers a user-friendly interface and a suite of powerful commands to enhance productivity.

## Command Interpreter
AirbnbCLI allows you to create, retrieve, update, and delete Airbnb objects using text-based commands. This makes it a powerful tool for developers and users who prefer a code-driven approach to data management.

### Getting started
1. **Installation**:

  - Clone this repository using Git:

    Bash
    git clone [https://github.com/your-username/airbnb_cli.git](https://github.com/simplykevine/alu-AirBnB_clone.git)

  - Install the package in development mode to make changes immediately reflected:

    Bash
    cd airbnb_cli
    pip install -e .

2. **Running the Interpreter**:

  - To start the command interpreter, navigate to the project directory and run:

    From the project directory, execute:

    Bash
    python cli.py

	This will start the AirbnbCLI and display its welcome message and prompt.

  - **Using the Command Interpreter**:

    -- Once the interpreter starts, you can use the following commands:

	--- help: Displays all available commands and their descriptions.
	--- run <command>: Executes the specified command.
	--- quit: Exits the command interpreter.

    -- Examples
	--- To get help:
	(cmd) help

	--- To execute a command:
	(cmd) run echo "Hello, World!"

	--- To exit the interpreter:
	(cmd) quit

    -- **Other commands**:
	-- create_user <username> <email>: Creates a new user.
	-- get_user <user_id>: Retrieves a user by ID.
	-- list_users: Lists all users.
	-- update_user <user_id> <attribute> <new_value>: Updates a specific user attribute.
	-- delete_user <user_id>: Deletes a user.

	(Similar commands exist for other object types like places and cities)

	-- help: Provides a list of available commands.
	-- exit: Exits the command interpreter.

    -- Example Usage:

	*** (airbnb) create_user john_doe john.doe@example.com
	*** (airbnb) get_user 1
	*** (airbnb) update_user 1 email jane.doe@example.com
	*** (airbnb) list_users
	*** (airbnb) help
	*** (airbnb) exit

  - Additional Notes

For more complex operations or additional functionalities, consider extending the command set by defining new methods in the AirbnbCLI class.
Explore implementing additional object types and functionalities related to Airbnb data management.

## Authors

Refer to the [AUTHORS](https://github.com/simplykevine/alu-AirBnB_clone/blob/master/AUTHORS) file at the root of the repository for a list of contributors.

## License

This project is licensed under the African Leadership University.
