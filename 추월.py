n = int(input())

in_car = [input().strip() for _ in range(n)]
out_car = [input().strip() for _ in range(n)]

in_tunnel = {car: i for i, car in enumerate(in_car)}

out_tunnel = []
for car in out_car:
    tunnel = in_tunnel[car]
    out_tunnel.append(tunnel)

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if out_tunnel[i] > out_tunnel[j]:
            count += 1
            break

print(count)