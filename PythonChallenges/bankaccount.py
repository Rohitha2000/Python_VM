balance = 0

def make_account():
    print("Account created Successfully ")
    return {'balance': 0}

def deposit(account, amount):
  account['balance'] += amount
  return "Amount Deposited Successfully ..." + str(account['balance'])

def withdraw(account, amount):
   account['balance'] -= amount
   return "Amount Withdrawn Successfully ..." + str(account['balance'])

a= make_account()

print(deposit(a, 29000))

print(withdraw(a, 1200))



