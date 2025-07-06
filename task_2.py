import random

def get_numbers_ticket(min_val, max_val, quantity):
        
    # Перевірка валідності вхідних параметрів
    if (min_val < 1 or 
        max_val > 1000 or 
        min_val > max_val or 
        quantity < 1 or 
        quantity > (max_val - min_val + 1)):
        return []
    
    # Генерація унікальних чисел
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    
    # Повертаємо відсортований список
    return sorted(numbers)
  
