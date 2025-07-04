# 6. Remove duplicate characters from a string
def duplicate_remover(string):
    seen = []
    for i in string:
        if i == " ":
            seen.append(i)
        elif i not in seen:
            seen.append(i)
    return "".join(seen)
