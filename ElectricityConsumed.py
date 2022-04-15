# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:34:24 2022

@author: Seb

        What the code does?
    This code takes customer name,previous and current meter reading of a 
    user and then categorised the user as a domestic user, industrial user
    or a commercial user based on the users electricity consumption.
    
    The code finally displays a message to the user including:
        1. The customer name
        2. Amount of electricity consumed by the customer
        3. Total amount to be paid,with an additional 2% charge
    
"""


# Getting customer name and meter readings

customerName  = str(input("Name of costomer: ")).capitalize()
previousReading = float(input("Previous meter reading,kwh: "))
currentReading = float(input("Current meter reading,kwh: "))

# passing info to the amountToBePaid function

def amountToBePaid(customerName,previousReading,currentReading):
    # check if current reading is less than the previous reading
    # since that can not happen
    if currentReading < previousReading:
        error_msg = f"Hello {customerName},your current meter reading "
        error_msg = error_msg + "can not be less than the previous meter reading!"

        print(error_msg)
        
    else:
        # compute amount of electricity consumed
        electricityConsumed = currentReading - previousReading

        # check and categorize customer based on the comsumption
        if electricityConsumed > 200:
            category = "a commercial user"
            
            if electricityConsumed <= 201:

                # amount to pay for first 201
                amountToPay = 0.9*electricityConsumed
                twoPersent = (2/100)*amountToPay #additional 2%
                totalAmountToBePaid = twoPersent + amountToPay

            else:

                # amount to pay if comsumption is more than 201

                amountToPay = (0.9*201) + 1.5*(electricityConsumed - 201)
                twoPersent = (2/100)*amountToPay  #additional 2%
                totalAmountToBePaid = twoPersent + amountToPay

        elif electricityConsumed > 100:
            category = "an industrial user"
            
            if electricityConsumed <= 120:

                # amount to pay for first 120 kwh
                amountToPay = 0.5*electricityConsumed
                twoPersent = (2/100)*amountToPay   #additional 2%
                totalAmountToBePaid = twoPersent + amountToPay

            else:

                # amount to pay if comsumption is more than 120 kwh

                amountToPay = (0.5*120) + 0.75*(electricityConsumed - 120)
                twoPersent = (2/100)*amountToPay   #additional 2%
                totalAmountToBePaid = twoPersent + amountToPay

        else:
            # domestic since all the above conditions faild
            category = "a domestic user"
            if electricityConsumed <= 60:

                # amount to pay for first 60 kwh

                amountToPay = 0.3*electricityConsumed
                twoPersent = (2/100)*amountToPay   #additional 2%
                totalAmountToBePaid = twoPersent + amountToPay

            else:

                # amount to pay if comsumption is more than 60 kwh
                amountToPay = (0.3*60) + 0.5*(electricityConsumed - 60)
                twoPersent = (2/100)*amountToPay    #additional 2%
                totalAmountToBePaid = twoPersent + amountToPay
        
        # formatting the message display
        msgToCustomer = f"\n Hello {customerName},based on your comsumption,"
        msgToCustomer = msgToCustomer + f"{electricityConsumed}kwh,you've been"
        msgToCustomer = msgToCustomer + f" categorised as {category} and "
        msgToCustomer = msgToCustomer + "you're to pay a total amount of"
        msgToCustomer = msgToCustomer + f" {totalAmountToBePaid:.2f} GHC"
        
        # dislpay message to user
        print(msgToCustomer)


# calling the amountToBepPaid function to do the needful
amountToBePaid(customerName, previousReading, currentReading)















