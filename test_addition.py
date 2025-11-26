from addition import add

def tests_add_positive_numbers():
    assert add(2,3)==5

def tests_add_negative_numbers():
    assert add(-4, -6)==-10

def tests_add_zero():
    
    assert add(0,5)==5 