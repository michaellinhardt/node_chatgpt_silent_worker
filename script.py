import sys
import os
import subprocess
import openai
from getpass import getpass

CHATGPT_API_KEY = os.environ.get("CHATGPT_API_KEY")

# Check if the API key is set, and output an error and stop the script if not
if CHATGPT_API_KEY is None:
    print("Error: The ChatGPT API key is not set. Please set the 'CHATGPT_API_KEY' environment variable.")
    print("Visit the project repository for instructions: https://github.com/yourusername/chatgpt-terminal")
    sys.exit(1)

# Set up the OpenAI library with your API key
openai.api_key = CHATGPT_API_KEY

# Function to send a request to ChatGPT with the given prompt
def chatgpt_request(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    text = response.choices[0].text.strip()

    # Remove the "message." part from the response
    if text.startswith("message."):
        text = text[len("message."):].strip()

    return text

def main():
    print("Welcome to the ChatGPT Terminal Interface!")

    conversation_history = []

    while True:
        user_input = input("> ")

        # Display help text
        if user_input == "!help":
            print("This script accepts the following commands:")
            print("!script - Generates a script with the provided instruction.")
            print("!help - Displays this help text.")
        
        # Generate and execute a script based on the user's instruction
        elif user_input.startswith("!script"):
            instruction = user_input[len("!script"):].strip()
            
            # Check if an instruction is provided
            if not instruction:
                print("Error: The !script command requires an argument.")
                continue
            
            print("Generating script...")
            prompt = f"Write a Python script with detailed commentary. Implement in the script a simple log output that writes in a txt file in the same folder. The log file purpose is to track and understand what happens when the script is executed. Only output the script without anything else. I will now describe what the script should do: {instruction}"
            generated_script = chatgpt_request(prompt)
            
            print("Saving generated script as 'silentWorker.py'...")
            with open("silentWorker.py", "w") as f:
                f.write(generated_script)
            
            print("Executing 'silentWorker.py'...")
            os.system("python silentWorker.py")
            print("Execution finished.")
        
        # Re-execute the last generated silentWorker.py
        elif user_input == "!rexec":
            if os.path.exists("silentWorker.py"):
                print("Re-executing 'silentWorker.py'...")
                os.system("python silentWorker.py")
                print("Execution finished.")
            else:
                print("Error: 'silentWorker.py' not found. Generate a script first using the !script command.")

        # Chat with ChatGPT
        else:
            message = user_input.strip()

            if not message:
                continue  # Do not print log output in the terminal when user doesn't type a command

            conversation_history.append(f"User: {message}")

            context = "\n".join(conversation_history)
            response = chatgpt_request(context)
            conversation_history.append(f"ChatGPT: {response}")

            print("\nResponse from ChatGPT:")  # Added a blank line before the response
            print(response)

if __name__ == "__main__":
    main()
