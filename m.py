symbols = [input().lower() for i in range(int(input()))]

memo = {}
def num_ways(word):
	if word not in memo:
		total = 0
		for i in symbols:
			if word[:len(i)] == i:
				new_word = word[len(i):]
				if len(new_word) == 0:
					total += 1
				else:
					total += num_ways(new_word)
		memo[word] = total
	return memo[word]

for i in range(int(input())):
	print(num_ways(input().lower()))