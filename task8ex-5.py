try:
    n=int(input("Enter a number:"))
    n=int(n)
except ValueError:
    print("Not valid")
except:
 print("An error")
else:
    print("Successfull!")
finally:
    print("END!")