#!/usr/bin/env python


class Solution:
    def prime_nums(self, n):
        prime_flag = [True] * (n + 1)
        for i in range(2, n+1):
            if prime_flag[i]:
                j = 2 * i
                while j < n + 1:
                    prime_flag[j] = False
                    j += i

        return [i for i in range(2, n+1) if prime_flag[i]]

    def is_prime(self, n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


if __name__ == "__main__":
    sl = Solution()
    primes = sl.prime_nums(100)
    # for i in primes:
    #     print(sl.is_prime(i))
    print(sl.is_prime(999))