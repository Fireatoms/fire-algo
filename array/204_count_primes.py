# link: https://leetcode.com/problems/count-primes/
# reference: https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# https://www.geeksforgeeks.org/sieve-eratosthenes-0n-time-complexity/


class Solution:
    """
    Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
Initially, let p equal 2, the first prime number.
Starting from p2, count up in increments of p and mark each of these numbers greater than or equal to p2 itself in the list. These numbers will be p(p+1), p(p+2), p(p+3), etc..
Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.
    """
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                for j in range(p * p, n, p):
                    is_prime[j] = False

        return sum(is_prime)

