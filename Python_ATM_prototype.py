#Add a loop for log in details
print("Hello and welcome to Guanzon Bank")
print("")

tries = 0

print("Log in details")
while True:
  if tries == 3:
    print("")
    print("Maximum amount of tries reached!")
    quit()
  log_in = (input("Account Number: "))
  if len(log_in) != 9:
    print("Please enter a real account number (9-digits)")
    continue
  else: 
    log_in_pin = int(input("Account Pin: "))
    if log_in_pin != 123456:
      print("Either your account number or pin is invalid! Please try again!")
      tries += 1
    else:
      break
#Fix what happens
 
balance = 100000

def Check_Balance(a_1):
  a_1 = str(a_1)
  print("")
  return ("Your balance is PHP " + a_1)

def Withdraw(a):
  global balance
  balance = balance
  if balance >= a:
   balance -= a
   a = str(a)
   print("")
   return ("You have successfully withdrawn PHP " + a)
  elif balance < a:
   print("")
   return("You have insufficient funds!")

def Transfer(b):
  global balance
  balance = balance
  if balance >= b:
    print("")
    transfer_1 = input("Enter account number to which you will be transferring money to (9-digits): ")
    if len(transfer_1) != 9:
      print("")
      return("This is not a real account please make sure you entered in 9 digits")
    transfer_1 = int(transfer_1)
    if transfer_1 == 123456789:
      print("")
      return("Why are you trying to tranfer money to yourself please select deposit for that.")
    else:
      balance -= b
      b = str(b)
      print("")
      return ("You have successfully transferred PHP " + b + " to SpongeBob SquarePants!")
  elif balance < b:
    print("")
    return ("You have insufficient funds!")

def Deposit(z):
  global balance 
  balance = balance
  balance += z
  z = str(z)
  print("")
  return ("You have successfully deposited PHP " + z + " into your account")

while True:
  print("")
  print("1-Check Balance")
  print("2-Withdraw")
  print("3-Transfer")
  print("4-Deposit")
  print("5-Exit")
  print("")

  Transaction_pick = (input("Pick a transaction: "))
  Transaction_pick = int(Transaction_pick)

  if Transaction_pick == 1:
    print(Check_Balance(balance))
  elif Transaction_pick == 2:
    print("")
    Withdrawal = int(input("How much would you like to withdraw?: "))
    print(Withdraw(Withdrawal))
  elif Transaction_pick == 3:
    print("")
    Transferral = int(input("How much would you like to transfer?: "))
    print(Transfer(Transferral))
  elif Transaction_pick == 4:
    print("")
    Deposit_input = int(input("Enter amount you want to deposit: "))
    print(Deposit(Deposit_input))
  elif Transaction_pick == str:
    print("")
    print("Invalid command")
    continue
  elif Transaction_pick <= 0 or Transaction_pick > 5:
    print("")
    print("Please pick a transaction from 1-5")
    continue
  else:
    print("")
    print("Thank you for using Guanzon Bank! Have a great day ahead!")
    break

  