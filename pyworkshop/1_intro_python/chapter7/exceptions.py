# this will throw an error
try:
    int("a")
except Exception as e:    
    print("oops, you can't do that!", e)

print("this is the end of my program")