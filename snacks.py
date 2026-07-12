from data_manager import load_users, save_users

def run_snack_bar(current_user):
    other_snacks = {
        "2": {"name": "Кока-Кола (0.5л)", "price": 50},
        "3": {"name": "Фанта (0.5л)", "price": 50},
        "4": {"name": "Начос із сирним соусом", "price": 140},
        "5": {"name": "Вода негазована (0.5л)", "price": 30}
    }
    
    popcorn_flavors = {
        "1": "Сирний",
        "2": "Карамельний",
        "3": "Солоний",
        "4": "Сирний з беконом"
    }
    
    popcorn_sizes = {
        "1": {"name": "Великий", "price": 150},
        "2": {"name": "Середній", "price": 120},
        "3": {"name": "Малий", "price": 90}
    }
    
    cart = []
    total_price = 0
    
    while True:
        print("\n" + "="*40)
        print(f"{' БАР КІНОТЕАТРУ ':^38}")
        print("="*40)
        
        print("[1] 🍿 Попкорн (Обрати смак та розмір)")
        for key, item in other_snacks.items():
            print(f"[{key}] {item['name']} - {item['price']} грн")
            
        print("-" * 40)
        print("[0] Завершити покупки та повернутися")
        
        choice = input("\nОберіть номер товару: ").strip()
        
        if choice == "0":
            break
            
        elif choice == "1":
            print("\n--- Вибір смаку попкорну ---")
            for f_key, f_val in popcorn_flavors.items():
                print(f"[{f_key}] {f_val}")
            
            flavor_choice = input("Оберіть номер смаку: ").strip()
            
            if flavor_choice not in popcorn_flavors:
                print("❌ Помилка: Такого смаку немає. Спробуйте ще раз.")
                continue
                
            print("\n--- Вибір розміру попкорну ---")
            for s_key, s_val in popcorn_sizes.items():
                print(f"[{s_key}] {s_val['name']} - {s_val['price']} грн")
                
            size_choice = input("Оберіть номер розміру: ").strip()
            
            if size_choice not in popcorn_sizes:
                print("❌ Помилка: Такого розміру немає. Спробуйте ще раз.")
                continue
                
            selected_flavor = popcorn_flavors[flavor_choice]
            selected_size = popcorn_sizes[size_choice]
            
            final_name = f"Попкорн ({selected_flavor}, {selected_size['name']})"
            cart.append(final_name)
            total_price += selected_size['price']
            
            print(f"\n✅ Додано в кошик: {final_name}. Поточна сума: {total_price} грн.")
            
        elif choice in other_snacks:
            selected_item = other_snacks[choice]
            cart.append(selected_item['name'])
            total_price += selected_item['price']
            print(f"\n✅ Додано в кошик: {selected_item['name']}. Поточна сума: {total_price} грн.")
            
        else:
            print("\n❌ Помилка: Будь ласка, введіть коректне число.")
            
    if cart:
        print("\n" + "*"*40)
        print(f" 🛒 ВАШ ЧЕК У БАРІ: {total_price} грн.")
        print(f" Придбані товари: {', '.join(cart)}")
        print("*"*40)
        
        # --- ЗБЕРЕЖЕННЯ В ОСОБИСТИЙ КАБІНЕТ ---
        users = load_users()
        
        # Створюємо список покупок їжі, якщо його ще немає (для старих акаунтів)
        if "snacks_history" not in users[current_user]:
            users[current_user]["snacks_history"] = []
            
        # Формуємо замовлення
        order = {
            "items": cart,
            "total": total_price
        }
        
        # Додаємо замовлення до користувача і зберігаємо
        users[current_user]["snacks_history"].append(order)
        save_users(users)
        print("✅ Ваше замовлення успішно збережено в Особистому кабінеті!")
        
    else:
        print("\nВи нічого не замовили у барі.")