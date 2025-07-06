from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        # Конвертуємо дату народження з рядка у datetime об'єкт
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Визначаємо дату народження в поточному році
        birthday_this_year = birthday_date.replace(year=today.year)
        
        # Якщо день народження вже минув у цьому році, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Визначаємо різницю між днем народження та поточним днем
        days_until_birthday = (birthday_this_year - today).days
        
        # Перевіряємо, чи день народження припадає на наступні 7 днів (включаючи сьогодні)
        if 0 <= days_until_birthday <= 7:
            # Визначаємо дату привітання
            congratulation_date = birthday_this_year
            
            # Перевіряємо, чи день народження припадає на вихідний
            # weekday(): понеділок = 0, неділя = 6
            if congratulation_date.weekday() >= 5:  # субота (5) або неділя (6)
                # Переносимо на наступний понеділок
                days_until_monday = 7 - congratulation_date.weekday()
                congratulation_date = congratulation_date + timedelta(days=days_until_monday)
            
            # Додаємо до списку привітань
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })
    
    return upcoming_birthdays

