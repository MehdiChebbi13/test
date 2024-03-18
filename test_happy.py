import sys

MOD = 998244353

def main():
    user_input=input()
    integer_list = user_input.split()
    integer_list = [int(i) for i in integer_list]
    N=integer_list[0]
    M=integer_list[1]
    strings=[]
    dp = [[0 for _ in range(26)] for _ in range(N + 1)]
    for i in range(26):
        dp[1][i] = 1

    for len in range(2, N + 1):
        for new_char in range(ord('a'), ord('z') + 1):
            for last_char in range(ord('a'), ord('z') + 1):
                if strings.append(chr(last_char) + chr(new_char)):
                    dp[len][new_char - ord('a')] += (dp[len - 1][last_char - ord('a')] * 2) % MOD
                else:
                    dp[len][new_char - ord('a')] += dp[len - 1][last_char - ord('a')]
                dp[len][new_char - ord('a')] %= MOD
        print (dp)

    result = 0
    for count in dp[N]:
        result = (result + count) % MOD

    print(result)

if __name__ == '__main__':
    main()