# not solved

# I had something that almost worked (although it probably was too slow)
# but I changed things to try to get it working and now it doesn't work at all

import math

class Restrictions:
	def __init__(self, max_vals):
		self.max_vals = max_vals
		self.val = [0 for i in max_vals]
	def next(self, bit=0):
		self.val[bit] += 1
		if self.val[bit] > self.max_vals[bit]:
			self.val[bit] -= self.max_vals[bit]
		self.next(bit+1)

N = int(input())
R = int(input())

restrictions = []

for i in range(R):
	_, num = input().split(" ")
	num = min(int(num), N)
	restrictions.append(num)

def total_combs(restrictions):
	total_this = 1

	letters_left = 36
	spots_left = N
	for max_num in restrictions:
		total_this *= math.comb(spots_left, max_num)
		spots_left -= max_num
		letters_left -= 1
		if (spots_left < 0):
			return 0
	total_this *= letters_left**spots_left
	return total_this

def get_restrictions(restrictions, l=None):
	if l is None:
		l = set()
	if all(i==0 for i in restrictions):
		l.append(restrictions)

total = 0
r = Restrictions(restrictions)
while True:
	total += total_combs(r.val)
	try:
		r.next()
	except:
		break

print(total)

