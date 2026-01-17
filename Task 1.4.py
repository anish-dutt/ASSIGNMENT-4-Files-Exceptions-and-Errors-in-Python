file = input("Enter the name of the file (use 'sample.txt'): ")
filer = file.lower()
try:
    with open(filer.strip(), 'r') as file:
        print("Reading file content:")
        line_num = 1
        for line in file:
            print(f"Line {line_num}: {line.rstrip()}")
            line_num += 1
except FileNotFoundError:
    print(f"Error: The file '{file}' was not found.")