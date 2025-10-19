'''

In -> bills -> [5, 10, 20]
Out -> bool
- True -> be able to give change to the final customer
- False -> Not be able to give change to the i-th customer

lemonade = 5


Test 1: 

[5, 10, 20]
0 => [0, 0, 0] -> Change to give -> 0
1 => [1, 0, 0] -> Change to give -> 5
2 => [0, 1, 0] -> Change to give -> 15 (Return False (15 - 10 => 5 and 5 != 0))

Test 2
[5, 5, 5, 20]
1 => [1, 0, 0] -> Change to give -> 0
2 => [2, 0, 0] -> Change to give -> 0
3 => [3, 0, 0] -> Change to give -> 0
5 => [0, 0, 1] -> Change to give -> 15 (Return True)


Demonstration 
-> For the ith customer, we always give the highest bill we have for change, until you have no more the highest bill.
-> You add the change to your balance, so that you can give change to i+1-th customer.


Algo
Change = [0, 0, 0]
- for i-th customer:
    - add bill to change
    - compute change
        - Given the highest bill we have, to the lowest,
        - If we don't have enough bills -> Failed
    
Time O(N * B), being N the number of customers and B how many different bills exist (3 in this case)
Space O(1) -> Discounting the input, we only need to store our change for every transaction.

'''



class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        cost = 5
        change = {5:0, 10:0, 20:0}
        possible_bills = [20, 10, 5]
        for bill in bills:

            # Find change:
            change_at = bill - cost
            idx = 0
            while change_at and idx < len(possible_bills):
                if change_at < possible_bills[idx] or change[possible_bills[idx]] == 0:
                    idx += 1
                    continue
                
                # Picking one bill at a time
                # We can always optimize picking max bills as possible
                change_at = change_at - possible_bills[idx]
                change[possible_bills[idx]] -= 1

            if change_at:
                return False


            change[bill] += 1


        return True


            


        
