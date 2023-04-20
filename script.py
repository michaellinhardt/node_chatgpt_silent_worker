import sys
import os
import subprocess
import requests
from getpass import getpass

CHATGPT_API_KEY = "your-chatgpt-api-key-here"

# Function to send a request to ChatGPT with the given prompt
def chatgpt_request(prompt):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {"Authorization": f"Bearer {CHATGPT_API_KEY}"}
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "n": 1,
        "stop": None,
        "temperature": 0.5,
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["text"].strip()

def main():
    print("Welcome to the ChatGPT Terminal Interface!")
    
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
        
        else:
            print("Invalid command. Type !help for available commands.")

if __name__ == "__main__":
    main()
