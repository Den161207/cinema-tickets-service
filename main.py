import account_manager
from cinema_core import CinemaCatalog  

def show_main_menu(is_logged_in):
    print("\n=== Сервіс купівлі квитків в кіно ===")
    if not is_logged_in:
        print("1. Зареєструватися")
        print("2. Увійти в акаунт")
        print("3. Вихід")
    else:
       
        print("1. Каталог фільмів та бронювання квитків")
        print("2. Особистий кабінет (інформація та історія)")
        print("3. Вийти з акаунту")
        print("4. Вихід з програми")
    print("=======================================")

def main():
    is_running = True
    current_user = None
    cinema = CinemaCatalog() 
    
    while is_running:
        show_main_menu(current_user is not None)
        choice = input("Оберіть дію: ").strip()
        
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
                
        else:
            if choice == '1':
                
                cinema.run_interactive_menu(current_user)
                
            elif choice == '2':
                account_manager.show_profile(current_user)
                
            elif choice == '3':
                print(f"\nКористувач {current_user} вийшов з системи.")
                current_user = None
                
            elif choice == '4':
                print("\nДякуємо за використання сервісу! До побачення.")
                is_running = False
                
            else:
                print("\nНевірна команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()