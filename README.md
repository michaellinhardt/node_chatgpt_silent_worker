# ChatGPT Terminal Interface

This project provides a Python terminal interface for interacting with OpenAI's ChatGPT.

## Features

- Get script suggestions from ChatGPT
- Write and execute generated scripts
- Extensible command system

## Installation

1. Clone the repository:

`git clone https://github.com/yourusername/chatgpt-terminal.git
cd chatgpt-terminal`

2. Install the required dependencies:

`pip install requests`
```pip install openai```

3. Set up the ChatGPT API key as an environment variable:

### For Linux and macOS

```export CHATGPT_API_KEY="your-chatgpt-api-key-here"```

### For Windows

Command Prompt:

```setx CHATGPT_API_KEY "your-chatgpt-api-key-here"```

### PowerShell

```[Environment]::SetEnvironmentVariable("CHATGPT_API_KEY", "your-chatgpt-api-key-here", "User")```

Replace your-chatgpt-api-key-here with your actual ChatGPT API key.

4. Run the script:

`python script.py`

## Usage

Enter one of the following commands in the terminal:

- `!help`: Display the help text.
- `!script`: Generates a script with the provided instruction.
- `!help`: Displays the help text.

## For example

`!script write a script that reads column A from an excel file and adds in column B the value A/2`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)