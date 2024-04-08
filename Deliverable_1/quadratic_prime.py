import timeit
from typing import Tuple


def main():
    max_primes, product_ab = get_quadratic_prime()
    print(f"Maximum consecutive primes is: {max_primes}")
    print(f"Product of a and b is: {product_ab}")


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_consecutive_primes(a: int, b: int) -> int:
    n = 0

    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n


def get_quadratic_prime() -> Tuple[int, int]:
    max_primes = 0
    product_ab = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            prime_count = count_consecutive_primes(a, b)
            if prime_count > max_primes:
                max_primes = prime_count
                product_ab = a * b

    return max_primes, product_ab


if __name__ == "__main__":
    # Define the code snippet to be timed
    code_snippet = "main()"

    # Time the execution of the main() function
    time_taken = timeit.timeit(code_snippet, number=10)  # Run once for longer calculations

    print(f"Execution time: {time_taken:.5f} seconds")
