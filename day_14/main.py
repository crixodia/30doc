def build_table(symbols: str) -> list:
    S = list(symbols)
    T = {}
    for s in symbols:
        T[s] = S.copy()
        S.append(S.pop(0))
    return T


def unit_crypt(text, key, symbols) -> str:
    C = ""
    T = build_table(symbols)
    for i, c in enumerate(text):
        idx = (T[c])[symbols.index(key[i])]
        C = C + symbols[symbols.index(idx)]

    return C


def crypt(text, key, symbols) -> str:
    words = text.split(" ")
    keys = key.split(" ")
    for i in range(len(words)):
        words[i] = unit_crypt(words[i], keys[i], symbols)

    return " ".join(words)


def unit_decrypt(text, key, symbols) -> str:
    C = ""
    T = build_table(symbols)
    for i, c in enumerate(key):
        idx = (T[c]).index(text[i])
        C = C + symbols[idx]

    return C


def decrypt(text, key, symbols) -> str:
    words = text.split(" ")
    keys = key.split(" ")
    for i in range(len(words)):
        words[i] = unit_decrypt(words[i], keys[i], symbols)

    return " ".join(words)


print("crypt:", crypt("AEIS GOD", "GVFH YGI", "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))
print(
    "crypt:",
    crypt(
        "C R I X O D I A",
        "A I D O X I R C",
        "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
    ),
)

print("decrypt:", decrypt("GZNZ EUL", "GVFH YGI", "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))
print(
    "decrypt:",
    decrypt(
        "C Z L M M L Z C",
        "A I D O X I R C",
        "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
    ),
)
