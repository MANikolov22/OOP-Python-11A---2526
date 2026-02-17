
import random
import math
import time

def generate_task():
    task_types = [
        ('factorial', "Факториел на число", 1, 11),
        ('fibonacci', "Първите n числа на Фибоначи", 5, 16),
        ('prime', "Просто ли е числото?", 2, 120),
        ('gcd', "Най-голям общ делител", 1, 150)
    ]
    task_name, desc, min_val, max_val = random.choice(task_types)

    if task_name == 'factorial':
        n = random.randint(min_val, max_val)
        return {'type': task_name, 'desc': desc, 'n': n, 'correct': math.factorial(n)}

    elif task_name == 'fibonacci':
        n = random.randint(min_val, max_val)
        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return {'type': task_name, 'desc': desc, 'n': n, 'correct': fib[:n]}

    elif task_name == 'prime':
        n = random.randint(min_val, max_val)
        is_p = n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
        return {'type': task_name, 'desc': desc, 'n': n, 'correct': is_p}

    else:
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        correct = math.gcd(a, b)
        return {'type': task_name, 'desc': desc, 'a': a, 'b': b, 'correct': correct}


def assign_tasks(participants):
    from ui import print_header, Colors
    print_header("ГЕНЕРИРАНЕ НА ЗАДАЧИ")
    for p in participants:
        p['task'] = generate_task()
        print(f"→ Задача за {p['name']}: {p['task']['desc']}")
    print(f"\n{Colors.OKGREEN}Готови са {len(participants)} задачи!{Colors.ENDC}\n")
    time.sleep(1.8)