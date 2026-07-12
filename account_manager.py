from data_manager import load_users, save_users

def register():
    users = load_users()
    
    print("\n--- Реєстрація ---")
    username = input("Введіть логін: ").strip()
    
    if username in users:
        print("Помилка: Користувач з таким логіном вже існує!")
        return None
        
    password = input("Введіть пароль: ").strip()
    name = input("Введіть ваше ПІБ: ").strip()
    
    users[username] = {
        "password": password,
        "name": name,
        "preferences": [],
        "history": [],
        "snacks_history": [] 
    }
    
    save_users(users)
    print("Реєстрація успішна! Тепер ви можете увійти.")
    return username

def login():
    users = load_users()
    
    print("\n--- Вхід ---")
    username = input("Введіть логін: ").strip()
    password = input("Введіть пароль: ").strip()
    
    if username in users and users[username]["password"] == password:
        print(f"Вітаємо, {users[username]['name']}!")
        return username
    else:
        print("Помилка: Невірний логін або пароль.")
        return None

def show_profile(username):
    users = load_users()
    user_data = users[username]
    
    print(f"\n--- Особистий кабінет: {user_data['name']} ---")
    print(f"Логін: {username}")
    
    print("\nІсторія бронювання квитків:")
    if not user_data.get("history"):
        print(" У вас ще немає замовлень квитків.")
    else:
        for index, ticket in enumerate(user_data["history"], 1):
            print(f" {index}. Фільм: '{ticket['movie']}', Ряд: {ticket['row']}, Місце: {ticket['seat']}")
            
    print("\nІсторія покупок у барі:")
    snacks = user_data.get("snacks_history", [])
    if not snacks:
        print(" Ви ще нічого не купували в барі.")
    else:
        for index, order in enumerate(snacks, 1):
            items_str = ", ".join(order["items"])
            print(f" {index}. Замовлення: {items_str} | Сума: {order['total']} грн.")
            
    print("-----------------------------------")