# This is a Python script that writes a "Hello World" message to a text file called "success.txt".

# We start by importing the "os" and "datetime" modules. The "os" module will allow us to create and write to the text file. The "datetime" module will allow us to timestamp our log entries.

import os
import datetime

# Next, we define a function called "write_to_log" which takes two arguments - a message to be written to the log, and the name of the log file.

def write_to_log(message, logfile):

    # We use the "with" keyword to open the