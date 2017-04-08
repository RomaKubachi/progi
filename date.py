class DayError(Exception):
    pass

class MonthError(Exception):
    pass

while True:
    try:
        date = input("Введите дату рождения в формате дд.мм.гггг: ")
        day = int(date[:2])
        month = int(date[3:5])
        year = int(date[6:])
        # print(day, month, year)

        if month == 2 and day > 28:
            raise DayError
        if month == 4 or month == 6 or month == 9 or month == 11 and day > 30:
            raise DayError    
        if day > 31 or day < 1:
            raise DayError
        if month > 12 or month < 1:
            raise MonthError

        if (day >= 22 and month == 3) or (day <= 19 and month == 4):
            print("Ты Овен")
        if (day >= 20 and month == 4) or (day <= 21 and month == 5):
            print("Ты Телец")
        if (day >= 22 and month == 5) or (day <= 21 and month == 6):
            print("Ты Близнецы")
        if (day >= 22 and month == 6) or (day <= 21 and month == 7):
            print("Ты Рак")
        if (day >= 22 and month == 7) or (day <= 21 and month == 8):
            print("Ты Лев")
        if (day >= 22 and month == 8) or (day <= 21 and month == 9):
            print("Ты Дева")
        if (day >= 22 and month == 9) or (day <= 21 and month == 10):
            print("Ты Весы")
        if (day >= 22 and month == 10) or (day <= 20 and month == 11):
            print("Ты Скорпион")
        if (day >= 21 and month == 11) or (day <= 21 and month == 12):
            print("Ты Стрелец")
        if (day >= 22 and month == 12) or (day <= 19 and month == 1):
            print("Ты Козерог")
        if (day >= 20 and month == 1) or (day <= 19 and month == 2):
            print("Ты Водолей")
        if (day >= 20 and month == 2) or (day <= 21 and month == 3):
            print("Ты Близнецы")
	
        break
    except ValueError:
        print("Введите дату в правильном формате")
    except DayError:
        print("Введите правильный день")
    except MonthError:
        print("Введите правильный месяц")