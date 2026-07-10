import account_manager

def show_main_menu(is_logged_in):
    print("\n=== Сервіс купівлі квитків в кіно ===")
    if not is_logged_in:
        print("1. Зареєструватися")
        print("2. Увійти в акаунт")
        print("3. Вихід")
    else:
        print("1. Переглянути афішу (список фільмів)")
        print("2. Купити квиток")
        print("3. Особистий кабінет (інформація та історія)")
        print("4. Вийти з акаунту")
        print("5. Вихід з програми")
    print("=======================================")

def main():
    is_running = True
    current_user = None # Змінна, що зберігає логін авторизованого користувача
    
    while is_running:
        show_main_menu(current_user is not None)
        choice = input("Оберіть дію: ").strip()
        
        # Логіка для НЕавторизованого користувача
        if current_user is None:
            if choice == '1':
                account_manager.register()
            elif choice == '2':
                current_user = account_manager.login()
            elif choice == '3':
                print("\nДякуємо за використання сервісу! До побачення.")
                is_running = False
            else:
                print("\nНевірна команда. Спробуйте ще раз.")
                
        # Логіка для АВТОРИЗОВАНОГО користувача
        else:
            if choice == '1':
                print("\n[У розробці Студентом 2] Тут буде список фільмів...")
            elif choice == '2':
                print("\n[У розробці Студентом 2] Тут буде процес купівлі квитка...")
                # Примітка: Студент 2 має написати функцію, яка після купівлі квитка
                # буде додавати його в список 'history' поточного користувача.
            elif choice == '3':
                account_manager.show_profile(current_user)
            elif choice == '4':
                print(f"\nКористувач {current_user} вийшов з системи.")
                current_user = None
            elif choice == '5':
                print("\nДякуємо за використання сервісу! До побачення.")
                is_running = False
            else:
                print("\nНевірна команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()