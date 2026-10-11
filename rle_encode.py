text = input()

if text:
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            print(f"{current_char}{count}", end="")
            current_char = char
            count = 1

    print(f"{current_char}{count}")