import  datetime

today =datetime.date.today()

formated = today.strftime("%d-%m-%Y")


print("Formatted date:", formated)