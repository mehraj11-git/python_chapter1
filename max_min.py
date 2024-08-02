number = [1,34,67]
print(max(number))
print(min(number)) 

def greatest_number(l):
    return max(l) - min(l)
     
print(greatest_number(number))