const fs = require("fs");
const readline = require("readline");
const { exec } = require("child_process");
const axios = require("axios");

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const CHATGPT_API_KEY = "your-chatgpt-api-key-here";

const helpText = `
Usage: node script.js [command] [argument]

Commands:
  !help         Display this help text.
  !script       Concatenate the instruction with a predefined message and send it to ChatGPT.
                Requires an argument (instruction).
  !rerun        Re-execute the previously generated silentWorker.js file.

Examples:
  !script write a script that reads column A from an excel file and add in column B the value A/2
`;

const sendToChatGPT = (instruction) =>
  axios.post(
    "https://api.openai.com/v1/engines/davinci-codex/completions",
    { prompt: instruction, max_tokens: 200, n: 1, stop: null, temperature: 0.7 },
    { headers: { "Content-Type": "application/json", Authorization: `Bearer ${CHATGPT_API_KEY}` } }
  );

const executeScript = (scriptPath) =>
  new Promise((resolve, reject) => {
    exec(`node ${scriptPath}`, (error, stdout, stderr) => {
      if (error) reject(error);
      if (stderr) reject(new Error(stderr));
      resolve(stdout);
    });
  });

function processCommand(input) {
  console.log("loading...");
  const [command, ...args] = input.trim().split(" ");

  if (command === "!help") {
    console.log(helpText);
    rl.prompt();
  } else if (command === "!script") {
    if (args.length === 0) {
      console.error("Error: !script command requires an argument.");
      rl.prompt();
    } else {
      const instruction = args.join(" ");
      const message = `Write a NodeJS script with detailed commentary. Implement in the script a simple log output that write in a txt file in the same folder. The log file purpose is to track and understand what happen when the script is executed. Only output the script without anything else. I will now describe what should do the script: ${instruction}`;

      sendToChatGPT(message)
        .then((response) => {
          const script = response.data.choices[0].text.trim();
          fs.writeFileSync("silentWorker.js", script);
          return executeScript("silentWorker.js");
        })
        .then((stdout) => {
          console.log(stdout);
          rl.prompt();
        })
        .catch((error) => {
          console.error(`Error: ${error.message}`);
          rl.prompt();
        });
    }
  } else if (command === "!rerun") {
    executeScript("silentWorker.js")
      .then((stdout) => {
        console.log(stdout);
        rl.prompt();
      })
      .catch((error) => {
        console.error(`Error: ${error.message}`);
        rl.prompt();
      });
  }
}

rl.on("line", processCommand);
rl.prompt();
