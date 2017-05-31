
# 0(1)
# Means the size of the data et is irrelevant. Number of steps/space will remain constant


# function first_element(the_list):
# 	return the_list[0];


# a_list = [1,2,4,6,45,234,523,5,3245,342,432,4532,234,1,14,546,543456];
# a_list = [1];
# a_list = range(1,100000000000);

# function first_element_minus_one(the_list);
# 	element = the_list[0] - 1;
# 	return element;


# # O(N) - grows linearly. I.e, the number os steps inrease proportionate to however many elements there are. This creates a striaght, diagonal line

# def loop_through_me(the_list):
# 	for elem in a_list:
# 		# do something
# 		pass;


# # O(N^2) - Represents an algorithm whose performance is directly proportional to the number of elements squared. VERY COMMON. Loop insde a loop_through_me (same as n * n)

# def oh_squared(the_list):
# 	for elem in the_list:
# 		for elem2 in the_list:
# 			# do something
# 			pass;



# For every new inside loop, you add a number to the big O
# 3 nested loop = O(N^3)
# 4 bested loop = O(N^4)

# 0(2^N) - Represents an algorithm that doubles with each new element.
# i.e., you add one new element, it takes twice as long

def fib(num):
	if(num <= 1):
		return num;
	return fib(num - 2) + fib(num - 1);



print fib(10)






