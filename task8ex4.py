#try and except block is not required when there is no error
try:
    age=int(input("Enter age:"))
except:
    print("enter valid")
finally:
    print("Done")
