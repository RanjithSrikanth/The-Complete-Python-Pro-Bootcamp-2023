####*args - tuple
def add(*args):
    print(args[3])
    j = 0
    for i in args:
        j += i
    return j

print(int(add(5, 5, 5, 5)))


####**kwargs - dictionary


def calculate(**kwargs):
    print(kwargs)
    # for k,v in kwargs.items()
    #     c = k + k+1
    print(kwargs["n1"] + kwargs["n2"] )


calculate(n1 = 6, n2 = 7, n3= 9)

class car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        # self.model = kwargs["model"]       //use kwargs.get("model") returns None

my_car = car(make="Nissan", model="Redi-go")
print(my_car.model)