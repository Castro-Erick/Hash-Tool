import subprocess

PS_Command = 'Get-FileHash'

File_Path = input("Enter an existing file path: ")

Command_String = ['certutil', '-hashfile', File_Path, 'SHA256']

try:
    Result = subprocess.run(Command_String, check=True, capture_output=True, text=True)
    
    Output = Result.stdout

    print(Output)

except subprocess.CalledProcessError as e:
    print(f'Error: {e}')