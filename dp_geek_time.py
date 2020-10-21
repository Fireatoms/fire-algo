from functools import reduce


def path_counts(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[3][3]


def combinational(n, m):
    n_list = [i for i in range(1, n + 1)]
    m_list = [i for i in range(1, m + 1)]
    m_n_list = [i for i in range(1, n - m + 1)]
    n_factorial = reduce(lambda x, y: x * y, n_list)
    m_factorial = reduce(lambda x, y: x * y, m_list)
    n_m_factorial = reduce(lambda x, y: x * y, m_n_list)
    return n_factorial // (m_factorial * n_m_factorial)


if __name__ == "__main__":
    print(path_counts(4, 4))
    print(combinational(6, 3))