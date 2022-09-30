from lib2to3.pygram import Symbols
import sys

SYMBOLS = "0123456789"


def is_valid_card(number: str) -> bool:
    number = number.strip().replace(" ", "")

    # Logitud de número de tarjeta de crédito
    if len(number) != 16:
        return False

    # Fórmula de Luhn
    digits = list(map(int, number))
    A = digits[::2]  # Dígitos con índice par
    B = digits[1::2]  # Dígitos con índice impar

    A = list(map(lambda x: 2*x, A))  # El factor se puede modificar
    A = list(map(lambda x: sum(divmod(x, 10)), A))

    return sum(list(A) + B) % 10 == 0


def luhn_check_n(s: str, symbols: list = SYMBOLS) -> int:
    # Generación de caracter de comprobación de Luhn
    N = len(symbols)
    s = s.strip().replace(" ", "")

    chars = list(map(symbols.index, s))
    A = chars[::2]
    B = chars[1::2]

    A = list(map(lambda x: 2*x, A))
    A = list(map(lambda x: sum(divmod(x, N)), A))

    check = (N - sum(list(A) + B)) % N
    return 0 if check == N else check


def luhn_encode_n(s: str, symbols: list = SYMBOLS) -> str:
    # Creación de string con carácter de comprobación al Final
    return s + symbols[luhn_check_n(s, symbols)]


def luhn_n(s: str, symbols: list = SYMBOLS) -> bool:
    # Validación generalizada de Luhn (Luhn N)
    N = len(symbols)
    s = s.strip().replace(" ", "")

    chars = list(map(symbols.index, s))
    A = chars[::2]
    B = chars[1::2]

    A = list(map(lambda x: 2*x, A))
    A = list(map(lambda x: sum(divmod(x, N)), A))

    return sum(list(A) + B) % N == 0


if __name__ == "__main__":
    if len(sys.argv) == 2:  # Validación de tarjetas de crédito
        print(f"{sys.argv[1]} -> {is_valid_card(sys.argv[1])}")
    elif len(sys.argv) == 3:   # Luhn generalizado
        # Descubrí que puedo generar números de cédula válidos de mi País -> Ecuador LOL
        symbols = sys.argv[1]
        s = sys.argv[2]

        print(f"symbols: {symbols}")
        print(f"string: {s}")
        print(f"check char: {luhn_check_n(s, symbols)}")
        print(f"encoded string: {luhn_encode_n(s, symbols)}")
        print(f"is valid: {luhn_n(luhn_encode_n(s, symbols), symbols)}")
    else:
        print("Usage: python main.py <credit_card_number>")
        print("Usage: python main.py <symbols> <no_encoded_string>")
