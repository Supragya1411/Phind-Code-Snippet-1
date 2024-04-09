import subprocess

# Command to create a directory, using -p to avoid errors if the directory already exists
command = "mkdir -p virtual-photo-booth"

# Execute the command
subprocess.run(command, shell=True)
