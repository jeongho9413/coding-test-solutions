"""
B - Cut and Count
https://atcoder.jp/contests/abc098/tasks/abc098_b

data structure:
    bit mask / set
algorithm:
    -
time complexity:
    O(N) / O(26N)
space complexity:
    -
""" 
def main() -> None:
    N = int(input())
    S = input().strip()

    # 1) prefix 집합
    pref = [set() for _ in range(N)]
    seen = set()
    for i, ch in enumerate(S):
        seen.add(ch)
        pref[i] = seen.copy()
    print(f"pref: {pref}")

    # 2) suffix 집합
    suff = [set() for _ in range(N)]
    seen = set()
    for i in range(N - 1, -1, -1):
        seen.add(S[i])
        suff[i] = seen.copy()
    print(f"suff: {suff}")

    # 3) 최대 공통 문자 수
    ans = 0
    for i in range(N - 1):
        ans = max(ans, len(pref[i] & suff[i + 1]))

    print(ans)

if __name__ == "__main__":
    main()
