import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dnas = [input().strip() for _ in range(n)]

result_dna = ""
total_distance = 0

for i in range(m):
    count = {"A" :0 , "C": 0, "G":0, "T":0}
    for dna in dnas:
        count[dna[i]] += 1
    
    max_char = min(count.items(), key = lambda x:(-x[1], x[0]))[0]
    result_dna += max_char

for dna in dnas:
    for a,b in zip(dna, result_dna):
        if a != b:
            total_distance += 1

print(result_dna)
print(total_distance)