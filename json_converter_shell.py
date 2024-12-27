import json
import os


# Load shell script from JSON file
def convert_shell_script(json_file, output_shell_file):
    try:
        # Open and read the JSON file
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Assume the shell script is stored in a key, e.g., "script"
        if 'script' not in data:
            raise KeyError("The JSON file does not contain a 'script' key.")

        shell_script = data['script']

        # Write the shell script to a file
        with open(output_shell_file, 'w') as f:
            f.write(shell_script)
            f.close()

        # Make the file executable
        os.chmod(output_shell_file, 0o755)

        print(f"Shell script has been written to {output_shell_file} and made executable.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
json_file = 'test.json'  # Input JSON file
output_shell_file = 'script.sh'  # Output shell script file

convert_shell_script(json_file, output_shell_file)
