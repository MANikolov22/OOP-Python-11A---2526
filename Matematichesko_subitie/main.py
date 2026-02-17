from storage import save_participants, load_participants
from ui import show_info_page, show_final_results
from registration import register_participants
from tasks import assign_tasks
from evaluation import run_evaluation
import time


def main():
    date = "17 февруари 2026"
    host = "Михаил Николов"

    participants = load_participants()
    show_info_page(date, host)

    new_participants = register_participants()
    participants.extend(new_participants)

    if not participants:
        print("Състезанието се отменя поради липса на участници.")
        return

    assign_tasks(participants)
    run_evaluation(participants)

    show_final_results(participants, date, host)
    save_participants(participants)
    input(f"\nНатиснете Enter за изход...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nСъстезанието беше прекъснато.")