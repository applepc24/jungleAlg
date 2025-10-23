import sys
input = sys.stdin.readline

n = int(input())

students = []
for _ in range(n):
    x,a,b,c,d = map(int, input().split())
    students.append((x,a,b,c,d))

kor = [(s[1], s[0]) for s in students]
eng = [(s[2], s[0]) for s in students]
math = [(s[3], s[0]) for s in students]
sci = [(s[4], s[0]) for s in students]

kor.sort(key = lambda x:(-x[0], x[1]))
eng.sort(key = lambda x:(-x[0], x[1]))
math.sort(key = lambda x:(-x[0], x[1]))
sci.sort(key = lambda x:(-x[0], x[1]))

award = set()


def pick(sub_list):
    for score, sid in sub_list:
        if sid not in award:
            award.add(sid)
            return sid
    return -1

print(pick(kor), pick(eng),pick(math),pick(sci))

