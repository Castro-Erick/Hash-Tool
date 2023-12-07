import subprocess

PS_COMMAND = 'Get-FileHash'
HASH_ALGORITHMS = ["MD4", "MD5", "SHA1", "SHA256", "SHA512"]

print("Type \"quit\" at any point to exit the program.")

while True:
    file_path = input("\nEnter an existing file path: ")
    if file_path.lower() == "quit":
        break

    try:
        for algorithm in HASH_ALGORITHMS:
            command_string = ['certutil', '-hashfile', file_path, algorithm]
            Result = subprocess.run(command_string, check=True, capture_output=True, text=True)

            output = Result.stdout.splitlines()
            hash_val = output[1].strip() if len(output) > 1 else "N/A"

            print(f'\n{algorithm}: {hash_val}')

    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')