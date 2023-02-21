def message():
    print('Welcome in Jackpot game')
    while True:
        answer = input(
            'You can play only if you are above 18 years old, do you understand? Y/N')
        if answer == "Y":
            answer = True
            print('great lets beggin')

        else:
            print('Please bring some adult with you')
        return answer


def user_input():
    while True:
        cash_deposit = input("How much cash would you like to deposit $")
        if cash_deposit.isdigit():
            cash_deposit = int(cash_deposit)
            if cash_deposit > 0:
                break
            else:
                print('Amount must be greater then 0')
        else:
            print('Please enter a number.')
    return cash_deposit


def main():
    msg = message()
    if msg == True:
        balance = user_input()
        print(balance)


main()
