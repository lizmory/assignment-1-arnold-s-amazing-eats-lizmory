# This is the script you will use for your Assignment #1.
# Adriana Lizmory Cuellar Salazar (Liz Cuellar)
# Student Number 8672918

def PrintCompleteName(name, lastName ): 
    print(f"\n\nClient: {name} {lastName}")

def PrintAdressData(streetNumber, streetName, numeroUnidad, telephoneNumber):
    print(f"Adress: {streetNumber}, {streetName}, {numeroUnidad}, {telephoneNumber}")

def PrintCityData(city, province, postalCode):
    print(f"City: {city}, Province: {province}, Postal code: {postalCode}")

def PrintSpecialInstructions(instructions):
    print(f"Special instructions: {instructions}")

def StudentReceiptOfPayment(article, units, totalPrice, studentDiscount, subTotal, tax, total ):
    print("     Article           Order quantity          Total price")
    print(f"     {article}                  {units}                ${totalPrice:.2f} ")
    print(f"\n10% student discount:   ${studentDiscount:.2f}")
    print(f"Subtotal:               ${subTotal:.2f}")
    print(f"Tax(13%):               ${tax:.2f}")
    print(f"Total:                  ${total:.2f}")

def ReceiptOfPayment(article, units, totalPrice, tax, total ):
    print("     Article           Order quantity          Total price")
    print(f"      {article}               {units}                    ${totalPrice:.2f} ")
    print(f"Tax(13%):               ${tax:.2f}")
    print(f"Total:                  ${total:.2f}")


print("Welcome to Arnold's Food Ordering Program")
print("Please enter your information below")
name = input("name: ")
lastName = input("last name: ")
print("\nAddress data for order delivery ") 
streetNumber= input("Street number: ")
streetName = input("Street name: ")
numeroUnidad = input("Unit number: ") 
city = input("City: ")
province = input("Province: ")
postalCode  = input("Postal code: ")
specialInstructions = input("Special instructions: ")
telephoneNumber= input("Telephone number: ")


totalPrice = 0.00 # is the unit price per number of dinners, before discount and tax
discount = 0.00 # this discount only applies if is a student
subTotal =0.00 # is the total after student discount and before tax
hst = 0.00 # tax
totalPay = 0.00 # subtotal plus tax.

exit = "n"

while exit =="n" or exit =="N":
    print()
    print("In the following menu you must choose your dinner.")
    print("Please, choose a number (1/2) according to the option you want")
    option = ""
    while option !="1" and option !="2":
        print("1) food_1 --> $10")
        print("2) food_2 --> $15")
        option= input("dinner: ")
        if option == "1":
           dinner = "food_1"
           total = 10.00 # represents the value per unit of item or dinner.
        elif option =="2" : 
           dinner = "food_2"
           total = 15.00 # represents the value per unit of item or dinner.
        else:
            print("Please, choose a valid option")
    
       
    numberDinners = int(input("How many dinners do you want to order?: "))
    totalPrice = total*numberDinners 
    print("Summary of your order:")
    print(f"Chosen dinner {dinner} x {numberDinners} units")
    option = input("Do you confirm your order?(Y/N): ")
    if option !="y" and option !="Y" and option !="n" and option !="N":
        print("Please, choose a valid option.")
    
    elif option =="y" or option =="Y":
        option2 = ""
        while option2 !="y" and option2 !="Y" and option2 !="n" and option2 !="N":
            option2 = input("Are you a student?(Y/N): ")
            if option2 =="Y" or option2 =="y":
                 discount = totalPrice * 0.1 # 10% discount calculation
                 subTotal= totalPrice - discount # total after student discount and before tax
                 hst = subTotal * 0.13 # HST applies then student discount applies.
                 totalPay = subTotal + hst # subtotal plus tax
                 PrintCompleteName(name, lastName)
                 PrintAdressData(streetNumber, streetName, numeroUnidad, telephoneNumber)
                 PrintCityData(city, province, postalCode)
                 PrintSpecialInstructions(specialInstructions)
                 print()
                 StudentReceiptOfPayment(dinner,numberDinners, totalPrice, discount, subTotal, hst, totalPay) 
                 exit ="y"
                 
            elif option2 =="n" or option2 =="N":
                 hst = totalPrice*0.13 # HST applies without any discount.
                 totalPay = totalPrice + hst # the sum of the gross total with the hst tax is made and the total to be paid is obtained
                 PrintCompleteName(name, lastName)
                 PrintAdressData(streetNumber, streetName, numeroUnidad, telephoneNumber)
                 PrintCityData(city, province, postalCode)
                 PrintSpecialInstructions(specialInstructions)
                 ReceiptOfPayment(dinner, numberDinners, totalPrice, hst, totalPay) # The method that prints receipt for NO students is called 
                 exit ="y" # This statement stops the while loop top-line 6

                 
            else:
                print("Please, choose a valid option")
             
            
    else:
        print("please reorder")
