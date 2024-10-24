 #1 #UZ Foydalanuvchidan bank hisobiga kiritish yoki yechish miqdorini so'rang. Agar hisobda yetarli mablag' bo'lmasa, xato xabarini ko'rsating. Hisob qoldig'ini ekranga chiqaring.
    #ENG Ask the user for the amount to deposit or withdraw from the bank account. If there are insufficient funds in the account, display an error message. Display your account balance.
ask = input("Hi, Would you like pay your the blance or withdrawal  ? You check PAY or Withdrawal ")
balance = 1_000_000
if ask.lower()=="PAY".lower():
    ask_pay = int(input("Please enter money ! "))
    print(f"You payed {ask_pay} sum 💳 ")
if ask.lower()=="Withdrawal".lower():
    ask_Withdrawal = int(input("Please enter money ! "))
    if ask_Withdrawal >1_000_000:
        print("Sory yor have not  enough !")  
    else: 
        print(f"You have withdrawn {ask_Withdrawal} thousand funds")  
        

