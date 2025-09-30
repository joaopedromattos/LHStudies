class ATM:

    def __init__(self):
        self.stock = [0] * 5
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.stock[i] = self.stock[i]  + banknotesCount[i]
            

    def withdraw(self, amount: int) -> List[int]:
        print(f"[WITHDRAW] - {amount}")
        original_stock = copy.copy(self.stock)
        withdraw_bills = [0] * 5
        remaining = amount
        cur_bill = 4
        bill_values = [20, 50, 100, 200, 500]
        while remaining > 0 and cur_bill > -1 :
        
            if remaining < bill_values[cur_bill]:
                print(f'remaining is {remaining} and current bill is {bill_values[cur_bill]}')
                cur_bill -= 1
                continue
        
            if self.stock[cur_bill] == 0:
                cur_bill -= 1
                continue
            
            # Taking as many bills as I can
            how_many_bills = min(remaining // bill_values[cur_bill], self.stock[cur_bill])
            self.stock[cur_bill] -= how_many_bills
            withdraw_bills[cur_bill] += how_many_bills
            remaining = remaining - (bill_values[cur_bill] * how_many_bills)
            print(f"Taking {how_many_bills} x {bill_values[cur_bill]} - remaining value {remaining}")

        print(f"Final stock status - {self.stock}")
        if remaining == 0:
            return withdraw_bills
        
        if remaining != 0 or cur_bill < 0:
            self.stock = original_stock
            return [-1]
		


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)