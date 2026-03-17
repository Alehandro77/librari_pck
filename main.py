import pickle
import os
from abc import ABC, abstractmethod

class People(ABC):

    def __init__(self, name):
        self._name = name
    
    @abstractmethod
    def get_menu(self):
        pass

class Employee(People):
    def __init__(self, name):
        super().__init__(name)

class ReturnName():
    def get_name(self):
        return self._name

class Book:

    def __init__(self, name, aftor, status):
        self.__name = name
        self.__aftor = aftor
        self.__status = status

    def get_name(self):
        return self.__name

    def get_aftor(self):
        return self.__aftor

    def get_status(self):
        if self.__status:
            return "книга свободна"
        else:
            return "книга занята"

    def set_status(self):
        self.__status =  not self.__status

class User(People, ReturnName):

    def __init__(self, name, books_taken):
        super().__init__(name)
        self.__books_taken = books_taken

    def get_books_taken(self):
        return self.__books_taken

    def get_book_name(self):
        books_name = ""
        for book in self.__books_taken:
            books_name += book.get_name() + ", "
        books_name = books_name[:-2]
        return books_name
    
    def return_book(self):
        print("Какую книгу вернуть?")
        print("Ваши взятые книги: " + self.get_book_name())
        name_book = input().lower()

        for book in self.__books_taken:
            if name_book == book.get_name().lower():
                self.__books_taken.remove(book)
                book.set_status()
                return "Книга возвращена"
            
        return "У вас нет такой книги"

    def take_book(self, buks):
        print("Какую книгу хотите взять?")
        print(get_free_book(buks))
        name_book = input().lower()

        for book in buks:
            if name_book == book.get_name().lower() and book.get_status() == "книга свободна":
                for book_user in self.__books_taken:
                    if name_book == book_user.get_name().lower():
                        return "Вы уже взяли эту книгу"

                self.__books_taken.append(book)
                book.set_status()
                return "Вы взяли книгу"

        return "Такой книги нет или она занята"
    
    def get_menu(self):
        menu = "\nВыбери действие: \n" \
                "1. Посмотреть список взятых книг\n" \
                "2. Посмотреть доступные книги\n" \
                "3. Взять книгу\n" \
                "4. Вернуть книгу\n" \
                "0. Выйти"
        
        return menu

class Bibliotekar(Employee, ReturnName):

    def __init__(self, name):
        super().__init__(name)

    def get_book(self, buks):
        for book in buks:
            print(f"Название книги: {book.get_name()}. Автор: {book.get_aftor()}. Статус: {book.get_status()}.")

    def add_book(self, buks):
        name = input("Введи название книги: ")
        aftor = input("Введи автора книги: ")

        buks.append(Book(name, aftor, True))

    def remov_book(self, buks):
        index = int(input("Введи номер книги: ")) - 1
        if buks[index].get_status() == "книга свободна":
            buks.pop(index)
        else: 
            print("Книга взята!")

    def get_users(self, users):
        for user in users:
            print(f"Пользоваель: {user.get_name()}. Взятые книги: {user.get_book_name()}")

    def add_user(self, users):
        name = input("Введите имя нового пользователя: ")
        books = []
        users.append(User(name, books))

    def get_menu(self):
        menu = "\nВыбери действие: \n" \
                "1. Вывести все книги\n" \
                "2. Добавить книгу\n" \
                "3. Удалить книгу\n" \
                "4. Вывести список пользователей\n" \
                "5. Зарегестрировать нового пользователя\n" \
                "0. Выход"
        
        return menu

def get_free_book(buks):
    free_books = "Свободные книги: "

    for book in buks:
        if book.get_status() == "книга свободна":
            free_books += book.get_name() + ", "

    free_books = free_books[:-2]
    return free_books
    
def entrance(list):
    global curent_user
    name = input("Введите своё имя: ").lower()

    for user in list:
        if name == user.get_name().lower():
            os.system("cls")
            curent_user = list.index(user)
            print("Здравствуйте " + name)
            return True
    
    os.system("cls")
    print("Такого пользователя нет!")
    return False

#----------------------------------------------------------------------
# def import_bibl():
#     bibls = []
#     with open("bibls.pkl", "rb") as file:
#         for i, line in enumerate(file):
#             bibls.append(Bibliotekar(pickle.load(file)))
#     return bibls

def import_bibl():
    bibls = []

    with open("bibls.pkl", "rb") as file:
        while True:
            try:
                bibls.append(pickle.load(file))
            except EOFError:
                break
    return bibls

# def import_bibl():
#     bibls = []
#     with open('bibls.txt', 'r', encoding='utf-8') as f:
#         for i, line in enumerate(f):
#             line = line.rstrip('\n')
#             bibls.append(Bibliotekar(line))
#     return bibls

def import_book():
    books = []

    with open("book.pkl", "rb") as file:
        while True:
            try:
                books.append(pickle.load(file))
            except EOFError:
                break
    return books

# def import_book():
#     books = []
#     with open('book.txt', 'r', encoding='utf-8') as f:
#         for i, line in enumerate(f):
#             line = line.rstrip('\n')
#             line = line.split(";")
#             name = line[0]
#             aftor = line[1]
#             status = line[2]

#             if status == "книга свободна":
#                 status = True
#             else:
#                 status = False

#             books.append(Book(name, aftor, status))

#     return books

def import_user():
    users = []

    with open("users.pkl", "rb") as file:
        while True:
            try:
                users.append(pickle.load(file))
            except EOFError:
                break
    return users

# def import_user(books):
#     users = []
#     books_name = {book.get_name(): book for book in books}

#     with open('user.txt', 'r', encoding='utf-8') as f:
#         for i, line in enumerate(f):
#             line = line.rstrip('\n')
#             line = line.split(";")
#             name = line[0]
#             books_taken = line[1].split(", ")

#             user_books = []
#             for title in books_taken:
#                 if title in books_name:
#                     user_books.append(books_name[title])
#                 else:
#                     print(f"Книга {title} отсутствует в библиотеке!!!")

#             users.append(User(name, user_books))

#     return users

#--------------------------------------------------------
def export_users(users):

    with open("users.pkl", "wb") as file:
        for user in users:
            pickle.dump(user, file)

# def export_users(users):
#     text = ""

#     for user in users:
#         name = user.get_name()
#         books = user.get_book_name();
#         text += name + ";" + books + "\n"

#     with open('user.txt', 'w', encoding='utf-8') as f:
#         f.write(text)

def export_bibls(bibls):

    with open("bibls.pkl", "wb") as file:
        for bibl in bibls:
            pickle.dump(bibl, file)


# def export_bibls(bibls):
#     text = ""

#     for bibl in bibls:
#         name = bibl.get_name()
#         text += name + "\n"
    
#     with open('bibls.txt', 'w', encoding='utf-8') as f:
#         f.write(text)

def export_books(books):

    with open("book.pkl", "wb") as file:
        for book in books:
            pickle.dump(book, file)


# def export_books(books):
#     text = ""

#     for book in books:
#         name = book.get_name()
#         afrot = book.get_aftor()
#         status = book.get_status()
#         text += name + ";" + afrot+ ";" + status + "\n"
    
#     with open('book.txt', 'w', encoding='utf-8') as f:
#         f.write(text)

#--------------------------------------------------------

def export_file(bibls, users, books):
    export_bibls(bibls)
    export_books(books)
    export_users(users)

def main():
    
    buks = import_book()
    bibls = import_bibl()
    users = import_user()

    os.system("cls")

    while True:

        print("Введите роль:\n" \
            "Б - библиотекорь\n" \
            "П - пользователь")

        rol = input().lower()

        if rol == "б":
            if entrance(bibls):
                break
            
        elif rol == "п":
            if entrance(users):
                break
        else:
            os.system("cls")
            print("Введи корректную роль")

    if rol == "б":
        while True:

            try:
                print(bibls[curent_user].get_menu())
                
                choice = int(input())

                os.system("cls")

                if choice == 1:
                    print("\n -----Список книг----- \n")
                    bibls[curent_user].get_book(buks)

                elif choice == 2:
                    print("\n -----Добавление книги----- \n")
                    bibls[curent_user].add_book(buks)

                elif choice == 3:
                    print("\n -----Удаление книги----- \n")
                    bibls[curent_user].remov_book(buks)

                elif choice == 4:
                    print("\n -----Списко пользователей----- \n")
                    bibls[curent_user].get_users(users)

                elif choice == 5:
                    print("\n -----Добавление пользователя----- \n")
                    bibls[curent_user].add_user(users)

                elif choice == 0:
                    print("До свидания")
                    break
                else:
                    os.system("cls")
                    print("Введите корректное значение!")
            except:
                os.system("cls")
                print("Введите корректное значение!")

    elif rol == "п":
        while True:
            
            try:
                print(users[curent_user].get_menu())
                
                choice = int(input())

                os.system("cls")

                if choice == 1:
                    print("Взятые книги: ", end="")
                    print(users[curent_user].get_book_name())

                elif choice == 2:
                    print(get_free_book(buks))

                elif choice == 3:
                    print(users[curent_user].take_book(buks))

                elif choice == 4:
                    print(users[curent_user].return_book())

                elif choice == 0:
                    print("До свидания")
                    break
                else:
                    os.system("cls")
                    print("Введите корректное значение!")
            except:
                os.system("cls")
                print("Введите корректное значение!")

    export_file(bibls, users, buks)

if __name__ == "__main__":
    main()
