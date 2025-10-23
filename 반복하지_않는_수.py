import sys

# P(n,k) = n*(n-1)*...*(n-k+1)
def P(n, k):
    v = 1
    for t in range(k):
        v *= (n - t)
    return v

# 길이 L인 중복없는 자연수 개수 = 9 * P(9, L-1)
cnt = [0]*11
for L in range(1, 11):
    cnt[L] = 9 * P(9, L-1)

# 누적합
acc = [0]*12
for L in range(1, 11):
    acc[L] = acc[L-1] + cnt[L]

def nth_no_repeat(n: int) -> int:
    # 1) 몇 자리 수인지 결정
    L = 1
    while acc[L] < n:
        L += 1
    idx = n - acc[L-1] - 1  # 길이 L 블록 내 0-based 순번

    # 2) 왼쪽부터 자릿수 채우기 (사전순 unranking)
    rem = list(range(10))   # 아직 안 쓴 숫자들
    ans = []
    for pos in range(L):
        r = L - pos                     # 남은 자리 수(현재 포함)
        block = P(len(rem)-1, r-1)      # 이 자리 하나 고르면 남은 r-1 자리를 채우는 경우의 수
        cand = [d for d in rem if pos > 0 or d != 0]  # 첫 자리는 0 금지
        pick = cand[idx // block]       # 몇 번째 후보인지
        ans.append(pick)
        rem.remove(pick)
        idx %= block

    # 3) 숫자로
    v = 0
    for d in ans:
        v = v*10 + d
    return v

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        print(nth_no_repeat(n))

if __name__ == "__main__":
    main()