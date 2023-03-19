# Write a Python function to sum all the numbers in a list.



# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20

# Code

def num(l):
   total_sum = 0
   for x in l:
      total_sum = total_sum + x
   return total_sum
my_list = [3, 1, 26, 9 ,33, 0,8]
print("sum of my_list : ",num(my_list))