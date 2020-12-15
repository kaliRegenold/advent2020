# Author: Kali Regenold

def fun1(expenses):
    # Find two values that add to 2020 and return their product
    for i in range(0,len(expenses)):
        for j in range(i+1, len(expenses)):
            if expenses[i] + expenses[j] == 2020:
                print(expenses[i]*expenses[j])
                return

def fun2(expenses):
    # Find three values that add to 2020 and return their product
    for i in range(0,len(expenses)):
        for j in range(i+1, len(expenses)):
            for k in range(j+1, len(expenses)):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    print(expenses[i]*expenses[j]*expenses[k])
                    return

if __name__ == "__main__":
    # Read expenses into a list separated by newline
    with open('1.in', 'r') as f:
        expenses = f.readlines()
    expenses = [int(x.strip()) for x in expenses]
    fun1(expenses)
    fun2(expenses)
