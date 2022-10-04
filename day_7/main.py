import re


def criteria(s: str) -> str:
    if len(s) <= 3:
        return s[0]

    return s[0].capitalize()


def acronimo(s: str) -> str:
    words = re.split("[-_ ]", s)

    acron = map(criteria, words)
    return "".join(list(acron))


if __name__ == "__main__":
    samples = [
        "Infrastructure as a service",
        "One-Time Password as a service",
        "Liquid-crystal display",
    ]
    for s in samples:
        print(acronimo(s))
