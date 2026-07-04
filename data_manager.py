import json
import os

USERS_FILE = 'users.json'

def load_users():
    """Завантажує дані користувачів з файлу."""
    if not os.path.exists(USERS_FILE):
        return {}  # Якщо файлу ще немає, повертаємо порожній словник
    
    with open(USERS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_users(users_data):
    """Зберігає дані користувачів у файл."""
    with open(USERS_FILE, 'w', encoding='utf-8') as file:
        json.dump(users_data, file, ensure_ascii=False, indent=4)