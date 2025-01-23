#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_of_evens(n):
    total = 0
    for i in range(2, n + 1, 2): 
        total += i
    return total

# Input from the user
n = int(input("Enter a positive integer n: "))

# Call the function and display the result
result = sum_of_evens(n)
print(f"The sum of all even numbers between 1 and {n} is: {result}")


# In[ ]:




