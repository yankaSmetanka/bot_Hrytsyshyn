import math, string, random, datetime

class VirtualInterlocutor:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(VirtualInterlocutor, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.groups = {
            'фізика': ['Завдання 1: Рівняння Гейзенберга неозначеності', 'Завдання 2: Закон Бойля-Маріотта'],
            'математика': ['Завдання 1: Знайти НСД і НСК', 'Завдання 2: Скалярний добуток векторів', 'Завдання 3:Площа трапеції'],
            'географія': ['Завдання 1: Який океан найбільший за площею?', 'Завдання 2: Знайти відстань між двома точками'],
            'робота з текстом': ['Завдання 1: Кількість слів', 'Завдання 2: Перевести текст у верхній регістр', 'Завдання 3: Перевести текст у нижній регістр'],
            'ква': ['Завдання 1: Зіграти камінь-ножиці-папір.', 'Завдання 2: Сказати мотиваційну цитату']
        }

    def get_group_tasks(self, group):
        if group in self.groups:
            return self.groups[group]
        else:
            return []

    def perform_task(self, group, task):
        if group == 'фізика':
            if task == '1':
                return self.physics1()
            elif task == '2':
                return self.physics2()
            else:
                return "Такого завдання з фізики немає, ква-ква."
        elif group == 'математика':
            if task == '1':
                return self.math1()
            elif task == '2':
                return self.math2()
            elif task == '3':
                return self.math3()
            else:
                return "Такого математичного завдання немає, ква-ква."
        elif group == 'географія':
            if task == '1':
                return self.geography1()
            elif task == '2':
                return self.geography2()
            else:
                return "Такого завдання з географії немає, ква-ква."
        elif group == 'робота з текстом':
            if task == '1':
                return self.textedit1()
            elif task == '2':
                return self.textedit2()
            elif task == '3':
                return self.textedit3()
            else:
                return "Таке я з текстом робити не вмію, ква-ква."
        elif group == 'ква':
            if task == '1':
                return self.other1()
            elif task == '2':
                return self.other2()
            else:
                return "Знайдіть собі кращого співрозмовника для цього, ква-ква."
        else:
            return "Такої групи не знайдено."

    def physics1(self):
        delta_x = float(input("Введіть похибку вимірювання положення (Δx): "))
        delta_p = float(input("Введіть похибку вимірювання імпульсу (Δp): "))
        h = float(input("Введіть сталу Планка (h): "))
        inequality_result = delta_x * delta_p >= h / (2 * 3.14159)
        if inequality_result:
            print("Нерівність Гейзенберга неозначеності виконується.")
        else:
            print("Нерівність Гейзенберга неозначеності не виконується.")

    def physics2(self):
        def calc(P2, V2, P1=None, V1=None):
            if P1 is None and V1 is None:
                raise ValueError("Введіть значення P1 або V1.")

            if P1 is not None and V1 is not None:
                raise ValueError("Введіть лише одне значення P1 або V1.")

            if P1 is not None:
                V1 = (P2 * V2) / P1
                return V1
            elif V1 is not None:
                P1 = (P2 * V2) / V1
                return P1

        P2 = float(input("Введіть тиск на початку (P2): "))
        V2 = float(input("Введіть об'єм на початку (V2): "))

        choice = input("Обчислити P1 або V1? (Введіть 'P1' або 'V1'): ")

        if choice == "P1":
            P1 = calc(P2, V2, P1=True)
            print("Тиск на початку (P1):", P1)
        elif choice == "V1":
            V1 = calc(P2, V2, V1=True)
            print("Об'єм на початку (V1):", V1)
        else:
            print("Невірний вибір.")

    def math1(self):
        def find_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def find_lcm(a, b):
            gcd = find_gcd(a, b)
            lcm = (a * b) // gcd
            return lcm

        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))

        gcd = find_gcd(num1, num2)
        lcm = find_lcm(num1, num2)

        print("Найбільший спільний дільник (НСД):", gcd)
        print("Найменше спільне кратне (НСК):", lcm)

    def math2(self):
        def dot_product(vector1, vector2):
            if len(vector1) != len(vector2):
                raise ValueError("Вектори повинні мати однакову довжину.")

            dot_product = 0
            magnitude1 = 0
            magnitude2 = 0

            for i in range(len(vector1)):
                dot_product += vector1[i] * vector2[i]
                magnitude1 += vector1[i] ** 2
                magnitude2 += vector2[i] ** 2

            magnitude1 = math.sqrt(magnitude1)
            magnitude2 = math.sqrt(magnitude2)

            angle = math.acos(dot_product / (magnitude1 * magnitude2))

            return dot_product, angle

        vector_A = []
        vector_B = []

        n = int(input("Введіть розмірність векторів: "))

        print("Введіть координати вектора A:")
        for i in range(n):
            coord = float(input(f"Координата {i + 1}: "))
            vector_A.append(coord)

        print("Введіть координати вектора B:")
        for i in range(n):
            coord = float(input(f"Координата {i + 1}: "))
            vector_B.append(coord)

        result, angle = dot_product(vector_A, vector_B)

        print("Скалярний добуток: ", result)
        print("Кут між векторами в градусах: ", math.degrees(angle))

    def math3(self):
        a = float(input("Введіть довжину першої паралельної сторони (a): "))
        b = float(input("Введіть довжину другої паралельної сторони (b): "))
        h = float(input("Введіть висоту трапеції (h): "))

        area = 0.5 * (a + b) * h

        print("Площа трапеції: ", area)

    def geography1(self):
        print('Найбільший за площею океан на Землі - Тихий океан. Це ж елементарно, жабенятко!  ')

    def geography2(self):
        x1 = float(input("Введіть координату x точки А: "))
        y1 = float(input("Введіть координату y точки А: "))
        x2 = float(input("Введіть координату x точки B: "))
        y2 = float(input("Введіть координату y точки B: "))

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        print("Відстань між точками А і В: ", distance)

    def textedit1(self):
        text_inp = input('Введіть ваш текст: ')
        text0 = ""
        for char in text_inp:
            if char not in string.punctuation:
                text0 += char

        print(f'Кількість слів у тексті: {len(text0)}')

    def textedit2(self):
        text_inp = input('Введіть ваш текст: ')
        text0 = ""
        for char in text_inp:
            if char not in string.punctuation:
                text0 += char

        text_norm = text0.upper().strip()
        print(f"Виправлений текст: {text_norm}")

    def textedit3(self):
        text_inp = input('Введіть ваш текст: ')
        text0 = ""
        for char in text_inp:
            if char not in string.punctuation:
                text0 += char

        text_norm = text0.lower().strip()
        print(f"Виправлений текст: {text_norm}")

    def other1(self):
        def game(player_choice):
            choices = ["камінь", "ножиці", "папір"]
            computer_choice = random.choice(choices)

            print("Ви вибрали:", player_choice)
            print("Я вибрала:", computer_choice)

            if player_choice == computer_choice:
                print("Нічия!")
            elif (
                    (player_choice == "камінь" and computer_choice == "ножиці") or
                    (player_choice == "ножиці" and computer_choice == "папір") or
                    (player_choice == "папір" and computer_choice == "камінь")
            ):
                print("Ви перемогли!")
            else:
                print("Я перемогла, ква-ква!")

        print("Нумо грати 'Камінь, ножиці, папір'")
        choice = input("Оберіть від 1 до 3, де 1 - камінь, 2 - ножиці, 3 - папір: ")
        options = ["1", "2", "3"]

        if choice in options:
            if choice == "1":
                game("камінь")
            elif choice == "2":
                game("ножиці")
            else:
                game("папір")
        else:
            print("Що складного в тому, аби обрати від 1 до 3, ква-ква..? Будь ласка, спробуте ще раз.")

    def other2(self):
        quotes = ["Якщо ви думаєте, що занадто маленькі, щоб щось змінити, спробуйте спати з комаром у кімнаті. Далай Лама",
                  "Ніколи не відкладайте на завтра те, що можна зробити післязавтра. Марк Твен.",
                  "Ніколи не слідуйте чиїмсь шляхом, якщо тільки ви не загубилися в лісі і бачите шлях - тоді обов'язково слідуйте. Еллен Дедженерес",
                  "Більшість людей впускають можливість, бо вона вдягнена в буденність і виглядає як праця. Томас Едісон",
                  "Бездарність – різновид ліні. Федін Сергій",
                  "Ледарі зроблять усе, аби нічого не робити. Еріан Шульц",
                  "День без сонячного світла - це, знаєте, як ніч. Стів Мартін",
                  "Хочеш знати хто ти? Дій! Не питай. Дія сама визначить тебе. Томас Джефферсон",
                  'Замініть слово "потім" на слово "ніколи", так ви принаймні не обманюватимете себе. Невідомий автор',
                  "Коли перестаєш переслідувати неправильні речі, даєш шанс правильним наздогнати тебе. Лоллі Даскал",
                  "Мені здається, що чим більше я стараюся, тим більше мені щастить. Томас Джефферсон",
                  "Весь прогрес відбувається поза зоною комфорту. Майкл Бобак",
                  "Прокрастинація робить легкі речі важкими, важкі – складнішими. Мейсон Кулі",
                  "Якщо ви хочете, щоб легка робота здавалася дуже важкою, просто відкладайте її виконання. Олін Міллер",
                  "Місяць - це, звичайно, дуже довго. Але за місяць звучить куди краще, ніж ніколи. Невідомий автор",
                  "Якщо ти хочеш, але не можеш, значить - не дуже хочеш. Невідомий автор"
        ]

        def random_quote():
            quote = random.choice(quotes)
            print(f"Ось, мотивуйтеся: {quote}")

        response = input("Справді хочете почути мотиваційну цитату? (так/ні): ")

        if response.lower() == 'ні':
            print('Навіщо ж тоді голову морочити? Скажу наступного разу, ква-ква...')
        else:
            random_quote()

    def other2(self):
        num = random.randint(1, 20)
        guess = None
        attempts = 4

        def get_int(prompt):
            while True:
                try:
                    guess = int(input("Спробуйте вгадати число від 1 до 20:"))
                except ValueError:
                    print("Вибачте, я не розумію, ква-ква.")
                    continue
                else:
                    break
            return guess

        while attempts > 0:
            guess = get_int("Спробуйте вгадати число від 1 до 20:")

            if guess == num:
                print("Ви вгадали!")
                break
            elif guess < num:
                attempts -= 1
                print(f'Ні! У вас залишилося {attempts} спроб')
                print("Але ось підказка! Загадане число менше ніж Ваше.)")
            elif guess > num:
                attempts -= 1
                print(f'Ні! У вас залишилося {attempts} спроб')
                print("Але ось підказка! Загадане число більше ніж Ваше.")
            else:
                print('Щось пішло не так, ква-ква. ')
                break


def main():
    virtual_interlocutor = VirtualInterlocutor()

    print("Ласкаво прошу до Жабки Помічниці!")
    print("Я - ваш особистий віртуальний співрозмовник. Можу допомогти з питаннями базової шкільної програми і просто поквакати!")
    print("Оберіть предмет: фізика, математика, географія, мова. Якщо хочете покваквати - скажіть «ква» !")

    chat = []

    while True:
        group = input("Виберіть предмет (або 'вихід' щоб завершити): ").lower().strip()
        if group == 'вихід':
            print("Дякую за співпрацю, ква-ква!")
            break

        tasks = virtual_interlocutor.get_group_tasks(group)
        if tasks:
            print("Наявні завдання:")
            for task in tasks:
                print(task)
            selected_task = input("Введіть номер завдання: ")
            result = virtual_interlocutor.perform_task(group, selected_task)
            print(result)
            chat.append(f"User: {group} -> {selected_task}")
            chat.append(f"Bot: {result}\n")
        else:
            print("Такого завдання немає, ква-ква.")

    def save_chat(chat):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"dialogue-{formatted_datetime}.txt"

        with open(file_name, "w") as file:
            file.writelines(chat)

        print("Наш діалог успішно збережено.")

    save_chat(chat)


if __name__ == '__main__':
    main()