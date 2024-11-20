# DCS comp.
from random import choice
import customtkinter as ct
from tkinter import messagebox, filedialog


# Функция генерации пароля
def pass_gen():
    # Берем переменную числа
    long_pass = len_pass_num.get()

    # Проверка включена ли кнопка доп символов и если включена то объединяем буквы и доп символы
    if dop_symbol.get():
        num_all = numbers_main + numbers_dop
    else:
        num_all = numbers_main

    # Генерация пароля
    password = "".join(choice(num_all) for _ in range(int(long_pass)))

    # Удаление всего что находится в поле от начального(0) и до конечного символа(end)
    pass_stroka.delete(0, "end")
    # Вставка сгенерированного пароля в поле
    pass_stroka.insert(0, password)


def copy_func():
    # Получаем текущий пароль из поля ввода
    password_copy = pass_stroka.get()

    if password_copy:

        window.clipboard_clear()  # Очистка буфера обмена
        window.clipboard_append(password_copy)  # Добавление текста в буфер обмена
        window.update()  # Обновление буфера обмена

        # Показываем сообщение об успешном копировании
        messagebox.showinfo("Информация", "Пароль успешно скопирован!")
    else:
        # Сообщение, если поле пустое
        messagebox.showinfo("Информация", "Поле для пароля пустое!")


# Функция сохранения пароля
def save_pass():
    pass_save = pass_stroka.get()
    if pass_save:
        # Расширение файла в котором будет сохраняться пароль
        f_way = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")],
                                             title="Сохранить пароль")

        if f_way:
            # Создаем файл и записываем в него сгенерированный пароль
            with open(f_way, "w") as file:
                file.write(pass_save)

                # Окно с информацией, что все успешно
                messagebox.showinfo("Информация", "Пароль успешно сохранен!")


# Параметры окна
ct.set_appearance_mode("dark")  # Темная тема
window = ct.CTk()  # Инициализация
window.title("Passgener")  # Название
window.geometry('350x350+800+300')  # Размеры + сдвиг чтобы окно было в центре
window.resizable(False, False)  # запрет на изменение размеров окна
window.iconbitmap("icon/icon.ico")

# Наборы символов
numbers_main = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
numbers_dop = "@!?{}[]().,/''`_-+=*:;%№#$<>"

# Фраза "Длина пароля"
nad_len = ct.CTkLabel(window, text="Длина пароля:", font=("Roboto", 26))
nad_len.place(relx=0.19, rely=0.07)  # Расположение надписи

# Ползунок для выбора длины пароля
polzunok_len = ct.CTkSlider(window, from_=8, to=32, number_of_steps=24, width=270, command=lambda value: up_len(
    value))  # При изменении значения ползунка вызывается функция up_len передавая ей текущее значение.
polzunok_len.set(20)  # Начальная длина
polzunok_len.place(relx=0.12, rely=0.23)  # Расположение


# Обновление отображаемого числа длины пароля
def up_len(value):
    # Округление значения до целого числа
    len_pass_num.set(str((int(value))))


# Метки для 8
num_min = ct.CTkLabel(window, text="8", font=("Roboto", 12))
num_min.place(relx=0.14, rely=0.32)  # Расположение

# Метки для 32
num_max = ct.CTkLabel(window, text="32", font=("Roboto", 12))
num_max.place(relx=0.85, rely=0.32)  # Расположение

# Метка для отображения текущей длины пароля
len_pass_num = ct.StringVar()
num_disp = ct.CTkLabel(window, textvariable=len_pass_num, font=("Roboto", 26))
len_pass_num.set("20")  # Изначальная длина
num_disp.place(relx=0.73, rely=0.07)  # Расположение

# Переключатель доп символов
dop_symbol = ct.BooleanVar()
use_dop = ct.CTkSwitch(window, text="Использовать доп. символы", font=("Roboto", 14), variable=dop_symbol)
use_dop.place(relx=0.172, rely=0.42)  # Расположение

# Поле для вывода пароля
pass_stroka = ct.CTkEntry(window, width=230, height=45, font=("Roboto", 18), justify="center")
pass_stroka.place(relx=0.12, rely=0.55)  # Расположение

# Кнопка копирования
button_copy = ct.CTkButton(window, text="📝", width=45, height=45, command=copy_func)
button_copy.place(relx=0.8, rely=0.55)  # Расположение

# Кнопка сохранения пароля
save_btn = ct.CTkButton(window, text="📂", width=45, height=45, command=save_pass)
save_btn.place(relx=0.8, rely=0.73)  # Расположение

# Кнопка генерации пароля
button_generate = ct.CTkButton(window, text="Сгенерировать", width=230, height=45, command=pass_gen)
button_generate.place(relx=0.12, rely=0.73)  # Расположение

window.mainloop()
