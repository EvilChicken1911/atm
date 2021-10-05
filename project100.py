class Atm:
    def __init__ (self, cardNum, pin):
        self.cardNum = cardNum
        self.pin = pin
    def checkBalance(self):
        print("Your balance is 200")
    def withdrawl(self, amount):
        newAmount = 200-amount
        print("You have withdrawn " + str(amount) + "Your new balance is " + str(newAmount))

def main():
    cardNum = input("what is your card number?")
    pin = input("What is your pin")
    newUser = Atm(cardNum, pin)
    print("choose your activity")
    print("1. balance inquiry 2. withdrawl")
    activity = int(input("Choose your activity"))
    if activity == 1:
        newUser.checkBalance()
    elif activity == 2:
        amountwithdrawl = int(input("How much do you want to withdrawl"))
        newUser.withdrawl(amountwithdrawl)
    else:
        print("Invalid card number or pin")

if __name__ == "__main__":
    main()