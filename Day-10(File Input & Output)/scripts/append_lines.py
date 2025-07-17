# Append a line to an existing file
def append_a_line(filename, line):
    with open(filename, "a") as f:
        f.write(line)


if __name__ == "__main__":
    filename = "Main_2.txt"
    line = "7. Seventh Line\n"
    append_a_line(filename, line)
