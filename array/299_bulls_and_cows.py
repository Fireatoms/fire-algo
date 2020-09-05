# link: https://leetcode.com/problems/bulls-and-cows/


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l = len(secret)
        na = 0
        nb = 0
        secret_dict = {}
        guess_dict = {}
        for i in range(l):
            if secret[i] == guess[i]:
                na += 1
            else:
                secret_dict[secret[i]] = secret_dict.get(secret[i], 0) + 1
                guess_dict[guess[i]] = guess_dict.get(guess[i], 0) + 1

        for g in guess_dict:
            if g in secret_dict:
                nb += min(guess_dict[g], secret_dict[g])

        return str(na) + 'A' + str(nb) + 'B'