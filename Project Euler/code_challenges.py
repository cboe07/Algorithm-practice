# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



def challenge():
	for i in range(1, 1000000):
		for j in range (1,21):
			if i % j == 0:
				return i
			else break
				
			

print challenge();
