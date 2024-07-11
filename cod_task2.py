def add():
 return a+b
def sub():
 return a-b
def mul():
 return a*b
def div():
 return a/b
def mod():
 return a%b

a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

def main():
 while True:
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Modulus")
  print("6. Exit")
  choice=int(input("Enter your choice: "))

  if choice==1:
    print(add())
  elif choice==2:
    print(sub())
  elif choice==3:
    print(mul())
  elif choice==4:
    print(div())
  elif choice==5:
    print(mod())
  elif choice==6:
    print("Exiting...")
    break
  else:
    print("Invalid choice")
if __name__ == "__main__":
 main()