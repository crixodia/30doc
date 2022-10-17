import numpy as np


def hill(text, key, symb):
    n = int(np.sqrt(len(key)))

    T = map(lambda c: symb.index(c), text)
    T = np.array(list(T))
    T = T.reshape(n, int(len(text) / n))

    K = map(lambda c: symb.index(c), key)
    K = np.array(list(K)).reshape(n, n)

    print("K:\n", K, "\n\nT:")
    print(T, "\n\nK * T:")

    C = np.dot(K, T)

    print(C, f"\n\n(K * T) mod {len(symb)}:")

    C = np.mod(C, len(symb)).flatten()

    print(C, "\n")

    return np.dot(K, T)


def unhill(C, key, symb):
    n = int(np.sqrt(len(key)))

    K = map(lambda c: symb.index(c), key)
    K = np.array(list(K)).reshape(n, n)
    K = np.linalg.inv(K)  # Inversa

    M = np.dot(K, C)
    M = np.mod(M.round(5), 26)
    M = M.flatten().astype(int)

    M = "".join(map(lambda c: symb[c], M.tolist()))
    return M


if __name__ == "__main__":
    symb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Criptograma:", hill("ACT", "GYBNQKURP", symb).flatten())
    print("Mensaje:", unhill(np.array([[67], [222], [319]]), "GYBNQKURP", symb))
