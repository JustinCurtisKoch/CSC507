import time

input_file = "sh-CSC507-Mod2-PM.txt"

def method1(input_file, output_file):
    """Line-by-line read and double numbers"""
    start = time.time()

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line.isdigit():
                number = int(line) * 2
                outfile.write(f"{number}\n")

    elapsed = time.time() - start
    print(f"Method 1: {int(elapsed // 60)} minutes {int(elapsed % 60)} seconds")


def method2(input_file, output_file):
    """Read entire file into memory and double numbers"""
    start = time.time()

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line in lines:
            line = line.strip()
            if line.isdigit():
                number = int(line) * 2
                outfile.write(f"{number}\n")

    elapsed = time.time() - start
    print(f"Method 2: {int(elapsed // 60)} minutes {int(elapsed % 60)} seconds")


def method3(input_file, output_file):
    """Read half file into memory, process, then second half"""
    start = time.time()

    # Count total lines first
    with open(input_file, 'r') as infile:
        total_lines = sum(1 for _ in infile)
    half_point = total_lines // 2

    with open(input_file, 'r') as infile:
        # Read first half into memory
        first_half = [infile.readline().strip() for _ in range(half_point)]

        # Read second half into memory
        second_half = [line.strip() for line in infile]

    with open(output_file, 'w') as outfile:
        for line in first_half:
            if line.isdigit():
                number = int(line) * 2
                outfile.write(f"{number}\n")

        for line in second_half:
            if line.isdigit():
                number = int(line) * 2
                outfile.write(f"{number}\n")

    elapsed = time.time() - start
    print(f"Method 3: {int(elapsed // 60)} minutes {int(elapsed % 60)} seconds")


if __name__ == "__main__":
    print("Running all three methods sequentially:\n")

    method1(input_file, "output_method1.txt")
    method2(input_file, "output_method2.txt")
    method3(input_file, "output_method3.txt")

    print("\nAll methods complete.")