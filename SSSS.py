# %% [markdown]
# 

# %% [markdown]
# #  Numbers

# %% [markdown]
# Compute the number of bytes in one Gigabyte (1kb = 1024 bytes, 1mb = 1024 kb, 1gb = 1024 mb)

# %%
number = 1
bytes_in_gb = (number*(1024 * 1024 * 1024))
print(bytes_in_gb)

# %% [markdown]
# You bought 500 shares of stock A at $\$$600 on day 0 and you sold it at  $\$$1000 on day 700.
# The daily discount rate is 0.0001%. How much profit did you make in terms of net present value.

# %%
int_price = 600
final_price = 1000
shares = 500
days = 700
daily_discount_rate = 0.000001  

profit = (final_price - int_price) * shares
npv_profit = profit / ((1 + daily_discount_rate) ** days)
print(npv_profit)

# %% [markdown]
# For any value of x, create a variable called even_check that is True if x is even and False if x is odd. 

# %%
x = 10 #or any number
even_check = (x % 2 == 0)
if even_check:
    print("Even")
else:
    print("Odd")

# %% [markdown]
# You have num_shirts t-shirts, num_shorts pairs of shorts and num_shoes pairs of shoes.  Create a variable called num_outfits that stores the total number of different outfits you can make.

# %%
num_shirts = 6
num_shorts = 7
num_shoes = 4

num_outfits = num_shirts * num_shorts * num_shoes
print(num_outfits)


# %% [markdown]
# # String Practice
# 
# Create variable called "name" that stores your full name. Find whether your name has an even or odd number of letters.

# %%
name = "Saurabh Shah"

length = len(name.replace(" ", ""))

if length % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# %% [markdown]
# Correct the following variable so it is equal to "spammy"

# %%
s = "spaxxy"
s = s.replace("x","m")
print(s)

# %% [markdown]
# Figure out a way to slice and combine the strings s1, s2, and s3 so that the variable consec_ints = "123456789".

# %%
s1 = "12345"
s2 = "34567"
s3 = "789"

consec_ints = s1 + s2[3:] + s3[1:]
print(consec_ints)



# %% [markdown]
# #  List Practice
# 
# 

# %% [markdown]
# Add the first and last elements of the list L. Store the result in a variable called sum_first_last. Your code should work if I change L.

# %%
L = [5,1,43,2,4,56,7,90, 67]
sum_first_last = L[0] + L[-1]
print(sum_first_last)


# %% [markdown]
# Slice and combine the elements of the list L in a way to print out "spam".

# %%
L = [1,"s", 2, 3, "p", "a", 34,1,"m"]
word = L[1]+L[4]+L[5]+L[8]
print (word)


# %% [markdown]
# Create a variable called num_L which store the number represented by the list of strings in L.  For the example num_L should be 145. You may assume 3 digit numbers.

# %%
L = ["3","6","9" ]
num_L = int("".join(L))
print(num_L)


# %% [markdown]
# Create a list L of numbers of odd length.  Complete the following tasks:
# 
#  - Find the median element
#  - Slice out all element indexed lower than the median element

# %%
L = [1, 3, 5, 7, 9, 11, 13]

mid_index = len(L) // 2
median_element = L[mid_index]
print("Median element:", median_element)

L_sliced = L[mid_index:]
print("Sliced list:", L_sliced)



