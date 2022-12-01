def dec_1 (foo):
    def wrapper (*args,**kwargs):
        arr = []
        for x in args:
            arr.append(x)
        arr.reverse()
        return (foo(*arr))
    return wrapper

@dec_1
def foo(*args):
    return args

print (foo(1,2,3,4,5,"adv"))
            
    
