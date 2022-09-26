import sys


def fib_memo(n: int) -> list:
    """
    Returns a list of the n first numbers of the Fibonacci sequence.
    The first number is 1.

    Args:
        n (int): The number of numbers to return.

    Returns:
        list: The n first numbers of the Fibonacci sequence.

    Raises:
        ValueError: If n is less than 0.

    Examples:
        >>> fib_memo(1)
        [1]
        >>> fib_memo(2)
        [1, 1]

    """
    memo = [0, 1]
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n <= 1:
        return memo[1:n+1]
    for i in range(2, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[1:]


def nth_fib(n: int) -> int:
    """
    Returns the nth number of the Fibonacci sequence.
    The first number is 1.

    Args:
        n (int): The number of numbers to return.

    Returns:
        int: The nth number of the Fibonacci sequence.

    Raises:
        ValueError: If n is less than 0.

    Examples:
        >>> nth_fib(1)
        1
        >>> nth_fib(2)
        1

    """
    return fib_memo(n)[-1]


def sum_fib(n: int) -> int:
    """
    Returns the sum of the n first numbers of the Fibonacci sequence.
    The first number is 1.

    Args:
        n (int): The number of numbers to return.

    Returns:
        int: The sum of the n first numbers of the Fibonacci sequence.

    Raises:
        ValueError: If n is less than 0.

    Examples:
        >>> sum_fib(1)
        1
        >>> sum_fib(2)
        2

    """
    return sum(fib_memo(n))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <n> [list|sum|nth|all]")
        sys.exit(1)

    n = int(sys.argv[1])
    opt = sys.argv[2] if len(sys.argv) > 2 else "all"
    if opt == "all":
        print("list:", fib_memo(n))
        print("nth:", nth_fib(n))
        print("sum:", sum_fib(n))
    elif opt == "list":
        print(fib_memo(n))
    elif opt == "sum":
        print(sum_fib(n))
    elif opt == "nth":
        print(nth_fib(n))
    else:
        print("Usage: python main.py <n> [list|sum|nth|all]")
        sys.exit(1)
