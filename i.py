# solved

costs = {}
info = {}

def get_cost(name):
	if name not in costs:
		costs[name] = 0
		for i in info[name]:
			costs[name] += get_cost(i)*info[name][i]

	return costs[name]

for i in range(int(input())):
	name, cost = input().split(" ")
	cost = int(cost)
	costs[name] = cost

for i in range(int(input())):
	part_info = input().split(" ")
	name = part_info[0]
	parts = {}
	for j in range(2, int(part_info[1])*2+2, 2):
		part_name = part_info[j]
		part_num = int(part_info[j+1])
		if part_name not in parts:
			parts[part_name] = 0
		parts[part_name] += part_num
	info[name] = parts

print(get_cost("Capstone"))
