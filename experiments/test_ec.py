# Common number pattern problems

def fizz_buzz(n):
    """
    Classic FizzBuzz: Print numbers 1 to n, but:
    - Print 'Fizz' for multiples of 3
    - Print 'Buzz' for multiples of 5
    - Print 'FizzBuzz' for multiples of both 3 and 5
    """
    print("=== FizzBuzz ===")
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def simple_numbers(n):
    """
    Simple version: Just print numbers 1 to n
    """
    print("=== Simple Numbers ===")
    for i in range(1, n + 1):
        print(i)


def even_odd(n):
    """
    Print 'Even' for even numbers, 'Odd' for odd numbers
    """
    print("=== Even/Odd ===")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print("Even")
        else:
            print("Odd")


def prime_check(n):
    """
    Print 'Prime' or 'Not Prime' for each number
    """

    def is_prime(num):
        if num < 2:
            return False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                return False
        return True

    print("=== Prime Check ===")
    for i in range(1, n + 1):
        if is_prime(i):
            print("Prime")
        else:
            print("Not Prime")


# Example usage
if __name__ == "__main__":
    n = 15  # Change this value as needed

    fizz_buzz(n)
    print("hey there")

