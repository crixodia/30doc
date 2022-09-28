
def count_letters(s:str) -> int:
    # Filter all letters from string
    L = filter(str.isalpha, s)
    return len(list(L))


def count_digits(s:str) -> int:
    # Filter all digist from string
    D = filter(str.isdigit, s)
    return len(list(D))

def count_custom(s:str, c) -> int:
    # Filter given a custom char
    # that is why we use lambda here
    C = filter(lambda x: x == c, s)
    return len(list(C))

if __name__ == '__main__':
    s = input("s: ")
    c = input("c: ")

    print("letters:", count_letters(s))
    print("digits:", count_digits(s))
    print("custom:", count_custom(s, c))
