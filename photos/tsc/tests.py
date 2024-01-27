
print("sankar 01")

class bank:
    bal = 0
    def deposit(self,amt):
        self.bal += amt
        return self.bal
    def withdraw(self,amt):
        if self.bal >= amt:
            self.bal -= amt

        else:
            print("not availanble")
        return self.bal

acc = bank()
acc.deposit(1000)
print(acc.withdraw(250))


# Create your tests here.
