# link: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def primitive_era(n):
    # prime num less than n
    is_prime = [True] * n
    if n < 3:
        return None

    is_prime[0] = is_prime[1] = False
    for i in range(2, n):
        if is_prime[i]:
            for j in range(2*i, n, i):
                is_prime[j] = False

    res = [i for i, v in enumerate(is_prime) if v]

    return res


def modified_era(n):
    is_prime = [True] * n
    if n < 3:
        return None

    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i**2, n, i):
                is_prime[j] = False

    return [i for i, v in enumerate(is_prime) if v]


if __name__ == "__main__":
    print(primitive_era(10))
    print(modified_era(10))