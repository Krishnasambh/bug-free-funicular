# unlimited arguments

def validation(*args):
    for eacharg in args:
        print(eacharg)

validation("sam","austin",78681)


# usage of kwargs*

def greet(**kwargs):
    for key,value in kwargs.items():
     print(key,value)
greet(name ="rishi",city="roundrock")