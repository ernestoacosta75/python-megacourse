def converter(original_unit, coefficient):
    return original_unit * coefficient

def returning():
    return 10

def printing():
    print(100)

original_unit = int(input("Enter the original unit: "))
coefficient = float(input("Enter the coefficient: "))
print(converter(original_unit, coefficient))