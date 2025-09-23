

def normalize(text: str) -> str:
 
    result = []
    for ch in text:
        if ch.isalpha():  # behåller bara bokstäver
            result.append(ch.lower())
    return "".join(result)

# print(normalize("Hello, World! 123!?"))  "helloworld"