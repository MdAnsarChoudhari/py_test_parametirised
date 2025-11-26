import sys 

def add(a,b):
    return a + b


if __name__ =="__main__":
    script_name = sys.argv[0]
    x=sys.argv[1]
    y=sys.argv[2]
    

    print("Sum :",add(x,y))