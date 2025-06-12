#%% md
 #It is an assignment operator (in python 3.8) which also returns the value which was assigned.
#Can be used inside expressions like if statements, while loops, and list comprehensions.
#%%
# without Walrus Operator
foods = list()
while True:
  food = input("What food do you like?: ")
  if food == "quit":
    break
  foods.append(food)

# with Walrus Operator (reduced lines of code)
foods1 = list()
while (food := input("What food do you like? (type 'quit' to stop): ")) != "quit":
    foods1.append(food)

#%%
# walrus operator with if statement:
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    if (n := len(list1)) > 10:
      print(f"List is too long ({n} elements)")