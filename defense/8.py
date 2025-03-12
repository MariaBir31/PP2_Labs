x = "good"

def myfunc():
    global x
    x = "fantastic"

print("Print is " + x)
myfunc()

print("Python is " + x)