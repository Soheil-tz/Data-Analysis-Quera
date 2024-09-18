input = input("Enter a list element separated by space ")
new_listone = input.split()
result1 = [element1.lower().capitalize() == "True" for element1 in new_listone]
n  = len(new_listone)
print(new_listone)
print("Converted list : ", result1)
'''
for i in x :
    if i==True :
        print("True")
        break
    else :
        print("False")
        break
'''    

