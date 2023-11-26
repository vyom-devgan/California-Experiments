import subprocess

# Define the command to run your script
command = "python Cali_elastic.py"

# Run a for loop from 0.1 to 0.9
for i in range(1, 10):
    alpha = 1.0 - i / 10.0
    l1_ratio = i / 10.0

    # Run the command with alpha and l1_ratio as arguments
    subprocess.run(f"{command} {alpha} {l1_ratio}", shell=True)