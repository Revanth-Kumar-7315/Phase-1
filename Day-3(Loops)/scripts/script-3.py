String = input("Enter a string : ").strip()

for i in String:
    if i in ["a", "e", "i", "o", "u"] or i in ["A", "E", "I", "O", "U"]:
        print(i)
