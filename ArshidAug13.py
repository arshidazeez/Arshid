#!/usr/bin/env python
# coding: utf-8

# In[1]:


def kilometers_to_miles(kilometers):
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles
km = 10
print(f"{km} kilometers is equal to {kilometers_to_miles(km)} miles.")


# In[2]:


def print_numbers_skipping_multiples_of_3(start, end):
    for number in range(start, end + 1):
        if number % 3 != 0:
            print(number)
start = 1
end = 20
print_numbers_skipping_multiples_of_3(start, end)


# In[ ]:




