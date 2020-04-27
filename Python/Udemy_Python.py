'''
# Error Handling
while True:
    try:
        age = int(input("What is your age: "))
        break
        print(age)
    except:
        print("error")
    else: # runs if try successfully runs
        break
    finally: # runs even if except is run and after try/else
        # can use to log how many time user try to login to system
'''

# generator function saves the state and increments once next is called. It prevent large memeory space uesd

def generator_function(num):
    for i in range(num):
        yield i*2
g = generator_function(100)
next(g)
next(g)
print(next(g))
