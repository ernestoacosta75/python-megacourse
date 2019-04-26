def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "The second argument must be greater tan zero"

print(divide(1, 0))