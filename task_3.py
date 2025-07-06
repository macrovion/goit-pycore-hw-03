import re

def normalize_phone(phone_number):
    
    # Видаляємо всі символи, крім цифр та '+'
    cleaned = re.sub(r'[^\d+]', '', phone_number)
    
    # Якщо номер починається з '+380', залишаємо як є
    if cleaned.startswith('+380'):
        return cleaned
    
    # Якщо номер починається з '+38', але не з '+380', додаємо '0'
    if cleaned.startswith('+38'):
        return '+380' + cleaned[3:]
    
    # Якщо номер починається з '380', додаємо '+'
    if cleaned.startswith('380'):
        return '+' + cleaned
    
    # Якщо номер починається з '38', додаємо '+' та '0'
    if cleaned.startswith('38'):
        return '+380' + cleaned[2:]
    
    # Якщо номер починається з '0', замінюємо на '+380'
    if cleaned.startswith('0'):
        return '+38' + cleaned
    
    # Якщо номер не має префікса, додаємо '+380'
    return '+380' + cleaned

