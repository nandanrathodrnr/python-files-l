class A:
    def is_prime(self,n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    


class B(A):
    def is_neon(self,a):
        if a==0 or a==1 or a==9:
            print('neon number')
        else:
            print("not neon number")
    
 
class C(A):
    def is_x(self):
        def x(self,name):
        name =str(input("Enter name : "))
        length = len(name)
        for i in range(length):
            for j in range(length):
                if i==j or i+j==length-1:
                    print(name[i],end=" ")
                else:
                    print(" ",end= " ")
print()
    
class D(A):
    def is_rev(self):
        name="nandan"
        print(name[::-1])
        
class E(B,C):
    def is_bank(self):
        def withdraw(self,account, amount):
            if self.amount > self.account['balance']:
                print("Insufficient funds!")
            else:
                self.account['balance'] -= amount
                self.account['transactions'].append(f"Withdrawal: ${self.amount}")
                print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

    def deposit(self,account, amount):
        self.account['balance'] += amount
        self.account['transactions'].append(f"Deposit: ${self.amount}")
        print(f"Deposit successful. Remaining balance: ${self.account['balance']}")

    def get_balance(self,account):
        return self.account['balance']

    def get_transaction_history(self,account):
        return self.account['transactions']

    # Create an account dictionary
    account = {
        'balance': 1000,
        'transactions': []
    }
    #login
    mail=["sathvik","tagore","zeeshan"]
    password=[123,456,789]
    umail=str(input("enter mailid "))
    upassword=int(input("enter password ")) 
    for i in range(0,3):
        if(mail[i] == umail):
            if(password[i] == upassword):
                print("Login successfull")
            # Dictionary to map user choices to functions
                choices = {
                    '1': deposit,
                    '2': withdraw,
                    '3': get_balance,
                    '4': get_transaction_history
                }

                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '5':
                        print("Exiting program.")
                        break

                    if choice in choices:
                        if choice == '1' or choice == '2':
                            amount = float(input("Enter amount: "))
                            choices[choice](account, amount)
                        else:
                            print(choices[choice](account))
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid mailid or password")
                
obj2=D()
obj1=E()
obj2.is_rev()
obj2.is_prime(11)
obj1.is_x()
obj1.is_bank()          
                
                
                
        