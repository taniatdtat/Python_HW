def dec_reverse_args(foo):   
    def wrapper (*args):
        arr = []
        for x in args:
            arr.append(x)
        arr.reverse()
        return (foo(*arr))
    return wrapper


def dec_print_args (foo):
    def wrapper (*args):
        foo(*args)
        print(*args)
    return wrapper

def dec_error (foo):
    def wrapper (*args):
        try:
            foo(*args)
        except Exception:
            print ("Error")
    return wrapper

@dec_reverse_args
def foo_1(*args):
    print(*args)

@dec_print_args
def foo_2(*args):
    sum = 0
    for x in args:
        sum +=x
    print(x)
    
@dec_error
def foo_3 (*args):
    print(args[0]*args[1])



foo_1(1,2,3,4,5,"adv")
foo_2( 1,3,5,7)
foo_3( "b","a")

            
    
