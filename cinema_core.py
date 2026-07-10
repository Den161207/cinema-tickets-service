# cinema_core.py
from data_manager import load_users, save_users
class Movie:
    """Клас для зберігання інформації про фільм."""
    def __init__(self, movie_id: int, title: str, genre: str, duration: int, description: str = ""):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.duration = duration
        self.description = description

    def get_short_info(self):
        return self.title

    def get_full_info(self):
        return f" Жанр: {self.genre}\n Тривалість: {self.duration} хв.\n Про фільм: {self.description}"


class Session:
    """Клас для зберігання інформації про сеанс та місця в залі."""
    def __init__(self, session_id: int, movie: Movie, time: str, format_type: str = "2D", rows: int = 5, seats_per_row: int = 8):
        self.session_id = session_id
        self.movie = movie
        self.time = time
        self.format_type = format_type
        self.seats = [[0 for _ in range(seats_per_row)] for _ in range(rows)]

    def show_seats(self):
        print(f"\n=== Сеанс: {self.movie.title} | Час: {self.time} | Формат: {self.format_type} ===")
        screen_width = 8 + (len(self.seats[0]) * 4) - 1
        print(f"{'ЕКРАН':^{screen_width}}")
        print("-" * screen_width)
        
        header = "        " + " ".join([f"{i+1:^3}" for i in range(len(self.seats[0]))])
        print(header)
         
        for row_idx, row in enumerate(self.seats):
            row_display = " ".join(["[X]" if seat == 1 else "[ ]" for seat in row])
            print(f"Ряд {row_idx + 1:<2}: {row_display}")
            
    def book_seat(self, row: int, seat: int) -> bool:
        if row < 1 or seat < 1 or row > len(self.seats) or seat > len(self.seats[0]):
            return False
        if self.seats[row - 1][seat - 1] == 0:
            self.seats[row - 1][seat - 1] = 1
            return True
        else:
            return False

class CinemaCatalog:
    """Головний клас для управління каталогом та інтерактивним меню."""
    def __init__(self):
        self.movies = [
            Movie(1, "Посіпаки і Монстряки", "Анімація, Комедія", 95, "Нові кумедні пригоди улюблених жовтих бешкетників."),
            Movie(2, "Ваяна", "Анімація, Пригоди", 100, "Відважна дівчина вирушає у небезпечну морську подорож, щоб врятувати свій народ."),
            Movie(3, "Астрал: За межами Потойбіччя", "Жахи", 110, "Моторошне продовження культової серії жахів, яке змусить затамувати подих."),
            Movie(4, "Диявол носить Прада 2", "Комедія, Драма", 115, "Повернення у безжальний, але неймовірно стильний світ високої моди."),
            Movie(5, "Одіссея", "Пригоди, Драма", 120, "Епічна історія виживання та боротьби людини з нещадною стихією."),
            Movie(6, "Людина-павук: Абсолютно новий день", "Екшн, Фантастика", 130, "Пітер Паркер стикається з новим могутнім ворогом, який загрожує всьому місту.")
        ]
        self.sessions = [
            Session(101, self.movies[0], "10:00", "2D"), Session(102, self.movies[0], "12:30", "3D"), Session(103, self.movies[0], "15:00", "2D"),
            Session(201, self.movies[1], "11:00", "2D"), Session(202, self.movies[1], "14:15", "3D"), Session(203, self.movies[1], "17:30", "IMAX"),
            Session(301, self.movies[2], "19:00", "2D"), Session(302, self.movies[2], "21:30", "2D"), Session(303, self.movies[2], "23:45", "2D"),
            Session(401, self.movies[3], "13:00", "2D"), Session(402, self.movies[3], "16:40", "2D"), Session(403, self.movies[3], "20:10", "VIP"),
            Session(501, self.movies[4], "10:30", "2D"), Session(502, self.movies[4], "16:00", "IMAX"), Session(503, self.movies[4], "19:15", "3D"), Session(504, self.movies[4], "22:00", "2D"),
            Session(601, self.movies[5], "12:00", "3D"), Session(602, self.movies[5], "15:30", "IMAX 3D"), Session(603, self.movies[5], "19:30", "IMAX 3D"), Session(604, self.movies[5], "22:15", "2D")
        ]
    def get_sessions_by_movie(self, movie_id: int):
        return [session for session in self.sessions if session.movie.movie_id == movie_id]
    def run_interactive_menu(self, current_user=None):
        while True:
            print("\n" + "="*40)
            print(f"{' КАТАЛОГ ФІЛЬМІВ':^38}")
            print("="*40)
            
            for movie in self.movies:
                print(f"[{movie.movie_id}] {movie.get_short_info()}")
                
            print("-" * 40)
            print("[0] Повернутися до головного меню") 
            
            movie_choice = input("\nОберіть номер фільму (або 0 для виходу): ")
            
            if movie_choice == '0':
                break 
                
            try:
                movie_id = int(movie_choice)
                selected_movie = next((m for m in self.movies if m.movie_id == movie_id), None)
                
                if not selected_movie:
                    print("\n Помилка: Фільму з таким номером не існує.")
                    continue
            except ValueError:
                print("\n Помилка: Будь ласка, введіть число.")
                continue

            print("\n" + "*"*40)
            print(f" {selected_movie.title.upper()}")
            print(selected_movie.get_full_info())
            print("*"*40)

            movie_sessions = self.get_sessions_by_movie(movie_id)
            
            print("\n ДОСТУПНІ СЕАНСИ:")
            for index, session in enumerate(movie_sessions):
                print(f"[{index + 1}] Час: {session.time} | Формат: {session.format_type}")
            print("[0] Повернутися до каталогу")

            session_choice = input("\nОберіть номер сеанса: ")
            
            if session_choice == '0':
                continue
                
            try:
                session_index = int(session_choice) - 1
                if session_index < 0 or session_index >= len(movie_sessions):
                    print("\n Помилка: Такого сеансу немає.")
                    continue
                    
                selected_session = movie_sessions[session_index]
                
            except ValueError:
                print("\n Помилка: Будь ласка, введіть число.")
                continue

            selected_session.show_seats()
            
            print("\nВведіть ряд та місце. Для кількох квитків використовуйте КОМУ.")
            print("Приклад: 3-4, 3-5 (або 3/4, 3/5)")
            seat_input = input("Ваш вибір: ")
            
            try:
                bookings = seat_input.split(',')
                success_tickets = []
                failed_tickets = []
                
                for booking in bookings:
                    clean_booking = booking.replace('-', ' ').replace('/', ' ').replace('\\', ' ').strip()
                    
                    if not clean_booking:
                        continue
                        
                    parts = clean_booking.split()
                    
                    if len(parts) != 2:
                        raise ValueError("Неправильний формат")
                        
                    row = int(parts[0])
                    seat = int(parts[1])
                    
                    if selected_session.book_seat(row, seat):
                        success_tickets.append(f"Ряд {row} Місце {seat}")
                        
                        if current_user:
                            users = load_users() 
                            ticket_dict = {
                                "movie": f"{selected_movie.title} ({selected_session.time})",
                                "row": row,
                                "seat": seat
                            }
                            users[current_user]["history"].append(ticket_dict)
                            save_users(users) 
                        # ----------------------------------------
                            
                    else:
                        failed_tickets.append(f"Ряд {row} Місце {seat}")
                
                print("\n--- РЕЗУЛЬТАТ БРОНЮВАННЯ ---")
                if success_tickets:
                    print(f" Успішно заброньовано: {', '.join(success_tickets)}")
                if failed_tickets:
                    print(f" Не вдалося забронювати (зайняті або не існують): {', '.join(failed_tickets)}")
                    
            except ValueError:
                print("\n Неправильний формат вводу. Використовуйте формат Ряд-Місце (наприклад: 2-5).")
            
            input("\nНатисніть Enter, щоб продовжити...")