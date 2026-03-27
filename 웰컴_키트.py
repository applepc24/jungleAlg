import sys
input = sys.stdin.readline

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

a = 0
for size in sizes:
    a += (size + T - 1) // T

print(a)
print(N // P, N % P)
