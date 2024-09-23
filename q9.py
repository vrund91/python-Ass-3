def outer(a,b):
    def inner(x,y):
        return x + y
    
    addition = inner(a,b)

    result = addition + 5

    return result

a = int(input("Enter a:"))
b = int(input("Enter b:"))

print("Addition is:",outer(a,b))