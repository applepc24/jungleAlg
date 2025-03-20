a,b = map(int, input().split())

a_str,b_str = str(a),str(b)

a_sli,b_sli = str(a_str)[::-1],str(b_str)[::-1]


if a_sli > b_sli:
    print(a_sli)
else:
    print(b_sli)

# arr = []

# for i in nums:
#     arr.append(i)
#     print(arr)

