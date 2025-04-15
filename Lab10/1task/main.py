import psycopg2
import csv

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(database="phonebook_db", 
                        user="postgres", 
                        host='localhost',
                        password="loki",
                        port=5432)
cur = conn.cursor()

# Создание таблицы phonebook, если она ещё не существует
cur.execute('''
    CREATE TABLE IF NOT EXISTS phonebook(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        telephone VARCHAR(40) NOT NULL)
''')
conn.commit()

# Функция для загрузки данных из CSV файла
def upload_csv(filename):
    command = """INSERT INTO phonebook(id, name, telephone) VALUES (%s, %s, %s)"""
    filename = "Lab10/contacts.csv"  # Путь к CSV-файлу
    try:
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)  # Пропускаем заголовок таблицы
            for row in csvreader:
                id, name, telephone = row  # Извлекаем данные из строки
                cur.execute(command, (id, name, telephone))  # Вставляем данные в таблицу
                conn.commit()  # Сохраняем изменения
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)  # Выводим ошибку, если она возникла

# Функция для добавления нового контакта через консоль
def enter_yourself():
    id = int(input("New contact's ID: "))  # Ввод ID
    name = input("Enter contact's name: ")  # Ввод имени
    telephone = input("Enter contact's telephone number: ")  # Ввод номера телефона
    cur.execute("INSERT INTO phonebook (id, name, telephone) VALUES (%s, %s, %s)", (id, name, telephone))
    conn.commit()

# Функция для обновления данных контакта
def update_table():
    id = int(input("Enter id of a contact you want to change: "))  # Ввод ID контакта
    print("What do you want to change?")
    print("1. Contact's name")
    print("2. Contact's telephone number")
    choice = int(input("Your choice: "))

    # Обновление имени
    if choice == 1:
        new_name = input("Write new name: ")
        cur.execute("""UPDATE phonebook
                        SET name = %s
                        WHERE id = %s""", (new_name, id))
        conn.commit()
    # Обновление номера телефона
    elif choice == 2:
        new_num = input("Write necessary phone number: ")
        cur.execute("""UPDATE phonebook
                        SET telephone = %s
                        WHERE id = %s""", (new_num, id))
        conn.commit()

# Функция для фильтрации данных по имени или номеру телефона
def query_data():
    print("How do you want to filter your data?")
    print("1. By contact's name")
    print("2. By contact's phone number")
    choice = int(input("Your choice: "))

    # Поиск по имени
    if choice == 1:
        name = input("Enter needed name: ")
        cur.execute("""SELECT * FROM phonebook WHERE name = %s;""", (name,))
    # Поиск по номеру
    elif choice == 2:
        num = input("Enter needed phone number: ")
        cur.execute("""SELECT * FROM phonebook WHERE telephone = %s;""", (num,))

    rows = cur.fetchall()  # Получаем все подходящие записи
    for row in rows:
        print(row)

# Функция для удаления контакта по имени
def delete_data():
    name = input("Enter name of a contact you want to delete: ")
    cur.execute("""DELETE FROM phonebook WHERE name = %s""", (name,))
    conn.commit()

# Функция для вывода всей таблицы phonebook в консоль
def print_phonebook_table():
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()  # Получаем все записи
    headers = ["ID", "Name", "Telephone"]  # Заголовки таблицы
    
    # Определение ширины колонок для красивого вывода
    col_widths = [len(header) for header in headers]
    for row in rows:
        col_widths[0] = max(col_widths[0], len(str(row[0])))
        col_widths[1] = max(col_widths[1], len(str(row[1])))
        col_widths[2] = max(col_widths[2], len(str(row[2])))

    # Формируем рамки и заголовок таблицы
    divider = '+' + '+'.join(['-' * (w + 2) for w in col_widths]) + '+'
    header_row = '| ' + ' | '.join(f'{headers[i]:<{col_widths[i]}}' for i in range(len(headers))) + ' |'
    
    print(divider)
    print(header_row)
    print(divider)
    
    # Вывод всех строк таблицы
    for row in rows:
        row_str = '| ' + ' | '.join(f'{str(row[i]):<{col_widths[i]}}' for i in range(len(row))) + ' |'
        print(row_str)
    print(divider)

# Основной блок программы
print("Choose what you want to do with the table:")
print("1. Insert some data")  # Добавить данные
print("2. Change contact")    # Изменить контакт
print("3. Filter data by name or phone number")  # Фильтр
print("4. Delete contact")    # Удалить контакт
command = int(input("Your choice: "))

# Обработка выбора пользователя
if command == 1:
    print("Choose the method you want to insert data with:")
    print("1. By the CSV-file")  # Загрузка из CSV
    print("2. By the console")   # Ввод вручную
    choice = int(input("Your choice: "))

    if choice == 1:
        filename = input("Enter CSV-file name: ")
        upload_csv(filename)
    elif choice == 2:
        enter_yourself()

elif command == 2:
    update_table()
elif command == 3:
    query_data()
elif command == 4:
    delete_data()

# Выводим таблицу после выполнения операции
print_phonebook_table()

# Закрываем соединение с базой данных
conn.close()
