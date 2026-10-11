encoded_text = input()
decoded_text = ""

for i in range(0, len(encoded_text), 2):
    char = encoded_text[i]  
    count = int(encoded_text[i + 1])  

    decoded_text += char * count

print(decoded_text)