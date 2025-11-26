import sys 

def add(a,b):
    return a + b


if __name__ =="__main__":
    if len(sys.argv)==3:
    script_name = sys.argv[0]
    x=sys.argv[1]
    y=sys.argv[2]
    

    print("Sum :",add(x,y))
