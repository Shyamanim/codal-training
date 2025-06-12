#circular import error:
# import my_module2
# my_module2.is_even(15)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

def display1():
    print('I am display1 from module1')

def call_display2():
    import my_module2
    my_module2.display2()

call_display2()

#solution:
# if __name__ == "__main__":
#     call_display2()
