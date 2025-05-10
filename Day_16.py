#!/usr/bin/env python
# coding: utf-8

# # Function Arguments and return statement
# There are four types of arguments that we can provide in a function:
# 1. Default Arguments
# 2. Keyword Arguments
# 3. Variable length Arguments
# 4. Required Arguments
# ### Default arguments:
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

# In[1]:


def name(fname="Samarth", mname="Nagesh",lname="More"):
    print("Full Name:",fname,mname,lname)
name("Narayan")


# In[2]:


def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")


# ### Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

# In[8]:


def average(a=10, b=12):
    print("Average:",(a+b)/2)
average()


# In[10]:


def average(a=10, b=12):
    print("Average:",(a+b)/2)
average(a=21,b=9)


# In[12]:


def name(fname, mname, lname):
    print("Full Name:", fname, mname, lname)

name(mname = "Nagesh", lname = "More", fname = "Samarth")


# ### Required arguments:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
# #### Example 1: when number of arguments passed does not match to the actual function definition.

# In[16]:


def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")
#It will show Error: name() missing 1 required positional argument: 'lname'


# ##### Example 2: when number of arguments passed matches to the actual function definition.

# In[18]:


def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Samarth", "Nagesh", "More")


# ## Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
# There are two ways to achieve this:
# ### Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
# #### Example:

# In[30]:


def name(*name):
    print("Full Name,", name[0], name[1], name[2])

name("Samarth", "Nagesh", "More")


# ### Keyword Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.
# #### Example:

# In[40]:


def name(**name):
    print("Full Name:", name["fname"], name["mname"], name["lname"])

name(mname = "Samarth", lname = "Nagesh", fname = "More")


# ## return Statement
# The return statement is used to return the value of the expression back to the calling function.
# #### Example:

# In[41]:


def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))


# In[46]:


def myfunction():
    return 3+3

print(myfunction())


# In[ ]:




