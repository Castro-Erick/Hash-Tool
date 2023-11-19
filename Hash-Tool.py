import subprocess

PS_Command = 'Get-FileHash'

print("Type \"quit\" at any point to exit the program.")

while True:
    hash_func = input("Enter the Hash Function you would like to use: ")
    if hash_func.lower() == "quit":
        break

    file_path = input("Enter an existing file path: ")
    if file_path.lower() == "quit":
        break

    command_string = ['certutil', '-hashfile', file_path, hash_func.upper()]

    try:
        Result = subprocess.run(command_string, check=True, capture_output=True, text=True)
    
        output = Result.stdout

        print(output)

    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')