# Read a file and count how many lines are in it
def count_lines_in_file(filename):
    with open(filename, "r") as f:
        return len(f.readlines())


if __name__ == "__main__":
    filename = "Main.txt"
    print(f"Total lines: {count_lines_in_file(filename)}")
