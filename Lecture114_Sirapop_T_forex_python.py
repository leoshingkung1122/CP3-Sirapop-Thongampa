from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
import datetime

c = CurrencyRates()
c_code = CurrencyCodes()

while True:
    try:
        input_year  = int(input("What year you want to configure?  : "))
        input_month = int(input("What month you want to configure? : "))
        input_date  = int(input("What date you want to configure?  : "))
        datetime_configure = datetime.date(input_year,input_month,input_date)
        print("Is this the date which you have configured?")
        print(datetime_configure)
        decision_next_step = input("Yes or No : ")

        if decision_next_step.capitalize() == "Yes":
            input_first_money_type  = input("What currency unit you want to exchange(from) : ")
            input_second_money_type = input("What currency unit you want to exchange(to)   : ")
            input_amount            = int(input("Amount of the excahange                       : "))
            result = c.convert(input_first_money_type.upper(),input_second_money_type.upper(),input_amount,datetime_configure)
            print("At the date","[",datetime_configure,"]")
            print("The currency from",input_first_money_type.upper(),"to",input_second_money_type.upper())
            print(">>> form",input_first_money_type.upper(),"[",c_code.get_symbol(input_first_money_type.upper()),"]"
                  ,"to",input_second_money_type.upper(),"[",c_code.get_symbol(input_second_money_type.upper()),"]"
                  ,">>",result,c_code.get_symbol(input_second_money_type.upper()))

        if decision_next_step.capitalize() == "No":
            print("The system will send you at the first menu.")
    except:
        print("Error!! The system will send you to the first menu.")

