# evaluation.py
import time
from ui import Colors, clear_screen, print_header
from tasks import generate_task  # ако искаме да тестваме единично


def evaluate_participant(p):
    task = p['task']
    t = task['type']

    print(f"\n{Colors.HEADER}→ {p['name'].upper()} – твоя ред!{Colors.ENDC}")
    print(f"Задача: {task['desc']}")

    if t == 'factorial':
        print(f"   Колко е {task['n']}! ?")
        try:
            ans = int(input("Твой отговор: "))
            if ans == task['correct']:
                p['points'] = 1
                print(f"{Colors.OKGREEN}✓ Точно!{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}Грешка. Правилен отговор: {task['correct']}{Colors.ENDC}")
        except:
            print(f"{Colors.FAIL}Невалиден отговор → 0 точки{Colors.ENDC}")

    elif t == 'fibonacci':
        print(f"   Първите {task['n']} числа на Фибоначи (разделени със запетая)")
        try:
            ans_str = input("Твой отговор: ").replace(" ", "")
            ans = [int(x) for x in ans_str.split(',')]
            if ans == task['correct']:
                p['points'] = 1
                print(f"{Colors.OKGREEN}✓ Перфектно!{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}Грешка. Правилно: {', '.join(map(str, task['correct']))}{Colors.ENDC}")
        except:
            print(f"{Colors.FAIL}Невалиден формат → 0 точки{Colors.ENDC}")

    elif t == 'prime':
        print(f"   Числото {task['n']} просто ли е? (да/не)")
        ans = input("Твой отговор: ").lower().strip()
        correct_str = "да" if task['correct'] else "не"
        if ans in [correct_str, 'yes' if correct_str == 'да' else 'no', 'y', 'n']:
            p['points'] = 1
            print(f"{Colors.OKGREEN}✓ Правилно!{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}Грешка. Правилен отговор: {correct_str}{Colors.ENDC}")

    elif t == 'gcd':
        print(f"   НОД({task['a']}, {task['b']}) = ?")
        try:
            ans = int(input("Твой отговор: "))
            if ans == task['correct']:
                p['points'] = 1
                print(f"{Colors.OKGREEN}✓ Точно!{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}Грешка. Правилно: {task['correct']}{Colors.ENDC}")
        except:
            print(f"{Colors.FAIL}Невалиден отговор → 0 точки{Colors.ENDC}")

    p['answered'] = True
    time.sleep(1.2)


def run_evaluation(participants):
    from ui import print_header, Colors
    print_header("СЪСТЕЗАНИЕТО ЗАПОЧВА!")
    print(f"Участници: {len(participants)}\n")
    time.sleep(1.5)

    for p in participants:
        evaluate_participant(p)
        clear_screen()
        remaining = sum(1 for x in participants if not x['answered'])
        print(f"Оставащи участници: {remaining}\n")