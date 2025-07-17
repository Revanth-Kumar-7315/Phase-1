# Write a list of strings into a file
def write_lines(filename, lines):
    with open(filename, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    filename = "Main_2.txt"
    lines = ["5. Fifth Line\n", "6. Sixth Line\n"]
    write_lines(filename, lines)
