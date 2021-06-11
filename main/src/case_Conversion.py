
def swap_case(name,binary):
    x=input(name)
    y=input(binary)
    new_str = " "
    for y in range(len(x)):
        if x[y].isupper():
             new_str+=x[y].lower()
        elif x[y].islower():
            new_str+=x[y].isupper()
        new_str+=x.swapcase() 

    return new_str           
