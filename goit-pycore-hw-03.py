from datetime import datetime

def get_days_from_today(date):
    
    try:
        # Перевірка типу вхідного параметра
        if not isinstance(date, str):
            raise TypeError("Параметр 'date' повинен бути рядком")
        
        # Перетворення рядка дати у об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        # Отримання поточної дати (лише дата, без часу)
        today = datetime.today().date()
        
        # Розрахунок різниці у днях
        difference = (today - given_date).days
        
        return difference
        
    except ValueError as e:
        # Обробка помилок формату дати
        raise ValueError(f"Неправильний формат дати. Очікується 'РРРР-ММ-ДД', отримано: '{date}'")