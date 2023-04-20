
# NodeJS ChatGPT Terminal Interface

This project provides a NodeJS terminal interface for interacting with OpenAI's ChatGPT.

## Note from Mike

"Everything is written by ChatGPT, even this README file.
You can find in each commit description, the chat typed for the cahnges obtained."

## Features

- Get script generated from ChatGPT
- Write and execute generated scripts
- Re-execute previously generated scripts
- Extensible command system

## Installation

1. Clone the repository:

```git clone <https://github.com/michaellinhardt/node_chatgpt_silent_worker>
cd node_chatgpt_silent_worker```

2. Install the required dependencies:

```npm install```

Add your ChatGPT API key to script.js:

```const CHATGPT_API_KEY = "your-chatgpt-api-key-here";```

Run the script:

```node script.js```

## Usage

Enter one of the following commands in the terminal:

!help: Display the help text.
!script: Concatenate the instruction with a predefined message and send it to ChatGPT. Requires an argument (instruction).
!rerun: Re-execute the previously generated silentWorker.js file.

For example:

```node script.js !script reads column A from an excel file and add in column B the value A/2```