
import os
import time
import sys


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}══════ {text} ══════{Colors.ENDC}\n")


def show_info_page(date, host):
    clear_screen()
    print_header("МАТЕМАТИЧЕСКО СЪСТЕЗАНИЕ 2026")
    print(f"{Colors.OKBLUE}Дата:{Colors.ENDC} {date}")
    print(f"{Colors.OKBLUE}Водещ:{Colors.ENDC} {host}")
    print("\n" + "═" * 60)
    print(" Добре дошли в състезанието за любители на математиката!")
    print(" Правила:")
    print(" • Всеки участник получава уникална задача")
    print(" • Имате една възможност да отговорите правилно")
    print(" • Правилен отговор = 1 точка")
    print(" • Победителят е участникът с най-много точки")
    print("═" * 60)
    print(f"\n{Colors.WARNING}Натиснете Enter, за да започнем...{Colors.ENDC}")
    input()


def show_final_results(participants, date, host):
    clear_screen()
    print_header("КЛАСИРАНЕ – КРАЕН РЕЗУЛТАТ")
    print(f"Дата: {date}   |   Водещ: {host}\n")

    if not participants:
        print("Никой не се състезава днес...")
        return

    sorted_part = sorted(participants, key=lambda x: -x['points'])

    for i, p in enumerate(sorted_part, 1):
        mark = f"{Colors.OKGREEN}★{Colors.ENDC}" if p['points'] == 1 else " "
        print(f"  {i:2}. {mark} {p['name']:20} ({p['country']}) → {p['points']} т.")

    max_score = sorted_part[0]['points']
    winners = [p['name'] for p in sorted_part if p['points'] == max_score]

    print("\n" + "═" * 60)
    if max_score > 0:
        print(f"{Colors.HEADER}ПОБЕДИТЕЛ(И): {', '.join(winners)} ! {Colors.OKGREEN}Поздравления!{Colors.ENDC}")
    else:
        print(f"{Colors.WARNING}Няма участник с точки... може би следващия път!{Colors.ENDC}")
    print("═" * 60 + "\n")