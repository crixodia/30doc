
def cesar(text: str, key: int, decrypt=False) -> str:
    factor = -1 if decrypt else 1
    cipher = map(lambda x: chr(ord(x) + factor * key), text)
    return "".join(cipher)


if __name__ == "__main__":
    print("Hola mundo", 3, "->", cesar("Hola mundo", 3))
    print("Krod#pxqgr", 3, "->", cesar("Krod#pxqgr", 3, True))
    print("1234567890", 8, "->", cesar("1234567890", 8))
