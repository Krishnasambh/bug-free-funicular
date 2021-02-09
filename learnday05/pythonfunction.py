def sayhello(city,name="guest"):
    print("hello", name,"from city",city)

def validatecustomer(name, address, zipcode):
    if len(name) > 0:
        print(name,"customer is valid")
    return True
def shoppingcart(items):
    for eachitem in items:
        print(eachitem)

sayhello("austin","david")
sayhello("cathy","roundrock")
sayhello("","sam")

validatecustomer("sameera","somethrer",78681)
shoppingcart(["123"] )


def multiply(x):
    return 3 * x
total = multiply(3)
print(total)



