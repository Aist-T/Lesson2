# Месяц-сезон
def month_to_season(month):
    if 1 <= month <= 2 or 12 == month :
        print ("зима")
    elif 6 <= month <= 8:
        print ("лето")
    elif 9 <= month <= 11:
        print ("осень")
    elif 3 <= month <= 5:
        print ("весна")
    else:
        print ("Не верный месяц")
month=int(input("введите номер месяца :")) 
month_to_season(month)   
