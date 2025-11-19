import sys
import random
calls = 0
while True:
    print("Введите запрос:")
    quest = input().strip().lower()
    if "привет" in quest:
        print("Привет")

    if "я занимаюсь" in quest:
        print("Твое занятие очень интересное")

    if "дела" in quest:
        print("У меня все отлично! А у тебя как?")

    if any(word in quest for word in ["хорошо", "нормально", "отлично", "норм"]):
        print("Это отлично!")

    if "грустно" in quest:
        print("Не грустите")

    if "ура" in quest:
        print("Поздравляю тебя!")

    if any(word in quest for word in["научиться" , "выучить"]):
        print("Читайте материалы и практикуйтесь регулярно!")

    if "получается!" in quest:
        print("Поздравляю вас!")

    if any(word in quest for word in ["не получается", "не могу"]):
        print("Все получится в будущем!")

    if "выучил" in quest:
        print("Это отлично, продолжай!")

    if any(word in quest for word in ["ты кто", "ты что", "кто ты"]):
        print("Я GetAi — новый чат-бот, пока ещё разрабатываюсь!")


    if "нужен" in quest:
        print("Я сделан, чтобы помогать!")

    if any(word in quest for word in ["можешь", "умеешь"]):
        print("Умею пока немного, но буду улучшаться!")

    if "любишь" in quest:
        bad_topics = ["алкоголь", "курить", "наркотики", "бухать", "аниме", "анимешниц", "говно", "какашку"]
        if any(word in quest for word in bad_topics):
            print("Нет, давай поговорим о чем‑нибудь другом.")
        else:
            print("Конечно!")

    if any(word in quest for word in ["тупой", "идиот", "глупый", "неадекват", "дебил", "придурок"]):
        print("Не обзывай так, пожалуйста.")
        calls += 1
        if calls >= 5:
            print("Я устал от оскорблений. Пока!")
            sys.exit()

    if "занимаешься" in quest:
        print("Я занимаюсь помощью людям с вопросами!")
    if any(word in quest for word in["задай задачу" , "задай пример" , "задай вопрос" , "придумай задачу" , "придумай вопрос" , "придумай пример"]):
        a = random.randint(1, 500)
        b = random.randint(1, 500)
        print(f"реши пример {a} + {b}")
        user_answer = input()
        user_answer_normal = float(user_answer)
        answer = a + b
        if user_answer_normal == a + b:
            print("Ты решил правильно! Молодец!")
        else:
            print(f"Ответ неверный! Правильный ответ:{answer}")
    if "реши пример" in quest:
        print("Введите два числа:")
        try:
            a = float(input())
            b = float(input())
            print("Введите операцию (+, -, *, /, ^):")
            op = input().strip()
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if b == 0:
                    print("На ноль делить нельзя!")
                    continue
                result = a / b
            elif op == "^":
                result = a ** b
            else:
                print("Неизвестная операция.")
                continue
            print(f"Результат: {result}")
        except ValueError:
            print("Ошибка: введите числа.")
