import tkinter as tk
from tkinter import ttk, messagebox
from search import main as search_main
from distributor import main as distributor_main
# from digitalizer import main as digitalizer_main


def show_notification(message):
    """Показывает окно уведомления"""
    messagebox.showinfo("Работа с договорами (ПДФ)", message)


def search_button_clicked():
    """Обработчик события для кнопки Search"""
    search_main()
    show_notification("Поиск по ключам завершено.\nРезультаты в файле search.html")


def distributor_button_clicked():
    """Обработчик события для кнопки Distributor"""
    distributor_main()
    show_notification("Распределение завершено.")

# def digitalizer_button_clicked():
#     """Обработчик события для кнопки Digitalizer"""
#     digitalizer_main()
#     show_notification("Цифровизация завершена.")


def main():
    root = tk.Tk()
    root.title("Работа с договорами (ПДФ)")

    # Кнопка для вызова функции search_main
    search_button = ttk.Button(root, text="Поиск по ключевым словам", command=search_button_clicked)
    search_button.pack(pady=10)

    # Кнопка для вызова функции distributor_main
    distributor_button = ttk.Button(root, text="Распределение сканов и цифровых пдф", command=distributor_button_clicked)
    distributor_button.pack(pady=10)

    # # Кнопка для вызова функции digitalizer_main
    # digitalizer_button = ttk.Button(root, text="Цифровизация сканов", command=digitalizer_button_clicked)
    # digitalizer_button.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
