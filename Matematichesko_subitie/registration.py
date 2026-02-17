
from ui import Colors, print_header, clear_screen
import time


def register_participants():
    participants = []
    print_header("РЕГИСТРАЦИЯ НА УЧАСТНИЦИ")

    while True:
        name = input(f"{Colors.OKGREEN}Име на участник (или 'край' за край): {Colors.ENDC}").strip()
        if name.lower() in ['край', 'done', 'exit', '']:
            if not participants:
                print(f"{Colors.WARNING}Няма регистрирани участници!{Colors.ENDC}")
                time.sleep(1.5)
            break

        try:
            age = int(input(f"{Colors.OKGREEN}Години: {Colors.ENDC}"))
            if age < 5 or age > 120:
                print(f"{Colors.FAIL}Невалидна възраст!{Colors.ENDC}")
                continue
        except ValueError:
            print(f"{Colors.FAIL}Моля, въведете число за години!{Colors.ENDC}")
            continue

        country = input(f"{Colors.OKGREEN}Държава: {Colors.ENDC}").strip()

        participants.append({
            'name': name,
            'age': age,
            'country': country,
            'task': None,
            'points': 0,
            'answered': False
        })
        print(f"{Colors.OKGREEN}→ {name} беше успешно регистриран!{Colors.ENDC}\n")
        time.sleep(0.6)

    return participants