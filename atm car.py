print("Wel To ATM")
card=input("incert your card")
if card=="debit card":
    print("next")
    lan=input("select your language : ")
    if lan=="english" or lan=="hindi":
        print("next")
        pin=int(input("enter your pin number : "))
        if pin>=0 and pin<=9999:
            print("next")
            tranjection=input("type of transaction")
            if tranjection=="withdraw" or tranjection=="deposite":
                print(" go to next")
                account=input("select your account")
                if account=="saving" or account=="current":
                    print("next")
                    amount=int(input("enter ammount"))
                    if amount>=100 and amount<=400000:
                        print("transaction has been procide")
                        a="thankyou for using"
                        print(a)
                    else:
                            print("Not have cash")
                else:
                    print("you didn't have another account")

            else:
                print("choose your type")
        else:
            ("pin incorrect")
    else:
        print("enter your language")
else:
    print("inset your car agin")