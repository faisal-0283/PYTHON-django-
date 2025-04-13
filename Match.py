#DAY MATCH

day=4
match day:
    # case 1:
    #     print("Monday")
    # case 2:
    #     print("Tuesday")    
    # case 3:
    #     print("Wednesday")    
    # case 4:
    #     print("Thursday")
    # case 5:
    #     print("Friday")
    # case 6:
    #     print("Saturday")
    # case 7:
    #     print("Sunday")          



    #     #Default value
    # case 5:
    #     print("Friday")
    # case 6:
    #     print("Saturday")
    # case _:
    #     print("Looking forward to the weekend")   




    case 1|2|3|4|5:
        print("Today is weekday")
    case 6|7:
        print("I love weekend")      




day = 4
Month = 5
match day:
    case 1|2|3|4|5 if Month == 4:
        print("A Weekday in APril")
    case 6|7 if Month == 5:
        print ("A Weekend in May")
    case _:
        print("No Match")        
    
            