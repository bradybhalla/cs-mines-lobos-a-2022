from functools import reduce

N, T = map(int, input().split(" "))

nums = [int(input()) for i in range(N)]

total = 0
for i in range(1,2**N):
	mask = "{:b}".format(i)
	mask = "0"*(N-len(mask)) + mask
	used_nums = [nums[i] for i in range(N) if mask[i]=="1"]
	total += (-1)**(len(used_nums)-1)*(T//reduce(lambda x, y: x * y, used_nums))

print(total)