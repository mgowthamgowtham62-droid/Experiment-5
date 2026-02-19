# This code creates 'sample.txt' inside the Jenkins Workspace
with open("sample.txt", "w") as f:
    f.write("This is a test file for Experiment 5.\n")
    f.write("Created via Python script.")

print("Success: sample.txt has been created.")