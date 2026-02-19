# file_manager.py
import datetime

filename = "sample.txt"

# Creating and writing to the file
with open(filename, "w") as f:
    f.write(f"File created by Python script on: {datetime.datetime.now()}\n")
    f.write("This is Experiment 5: File Handling Operations.")

print(f"Successfully created {filename}")