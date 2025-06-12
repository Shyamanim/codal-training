import my_module

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False

def display2():
    print('I am display2 from module2')

def call_display1():
    import my_module
    my_module.display1()

call_display1()

# if __name__ == "__main__":
#     call_display1()