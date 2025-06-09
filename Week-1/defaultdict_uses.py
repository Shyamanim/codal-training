#%% md
"""A default dictionary is used to provide a default value for a nonexistent key in the dictionary.
 Thus, now there is no need of checking if the key exists before using it(KeyError is avoided).
"""
#%%
from collections import defaultdict

# A defaultdict is defined as :
# defaultdict(default_factory)
# where the default_factory function returns the type of the default value, may be a list, string or int.

d1 = defaultdict(list)

for i in range(5):
    d1[i].append(i)

print("Dictionary with values as list:")
print(d1)
print(d1[6])

d2 = defaultdict(int)
print(d2[1])

d3 = defaultdict(str)
print(d3[2])

d4 = defaultdict(lambda: "not present")
d4["a"] = 1
d4["b"] = 2

print(d4.__missing__('a'))
print(d4.__missing__('d'))