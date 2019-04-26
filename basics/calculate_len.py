def calcolate_len(anString):
    if(anString.isalpha()):
        return len(anString)        
    elif (anString.isalnum()):
        return "It is not an string"
    elif (anString.isdigit()): 
        return "It is not an string"        

anString = input("Enter an string: ")
print(calcolate_len(anString))       