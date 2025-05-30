import sys
input = sys.stdin.readline

n, m = map(int, input().split())

group_to_member = dict()
member_to_group = dict()

for _ in range(n):
    group_name = input().strip()
    member_count = int(input())
    members = [input().strip() for _ in range(member_count)]

    group_to_member[group_name] = members
    for member in members:
        member_to_group[number] = group_name

