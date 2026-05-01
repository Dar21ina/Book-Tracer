import tkinter as tk
from tkinter import ttk, messagebox 
import json
import os
from datetime import datetime

DATA_FILE = "books_data.json"

#изменение


# Функция сохранения данных в JSON
def save_data():
    try:
        with open(DATA_FILE, "w", enconding="utf-8") as f:
            json.dump(books, f, ensure_ascii=False, indent=2)
        messagebox.showinfo("Успех", "Данные сохранены в файл!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить данные:\n{e}")


# Функция загрузки данных из JSON
def load_data():
    try:
        with open(DATA_FILE, "r", enconding="utf-8") as f:
            books = json.load(f)
        messagebox.showinfo("Успех", "Данные загружены успешно!")
        return books
    except FileNotFoundError:
        messagebox.showwarning("Предупреждение", "Файл с данными не найден. Будет использован путсой список.")
        return []
    except json.JSONecodeError:
        messageebox.showerror("Ошибка", "Файл поврежден или содержит некорретный JSON.")
        return []

# Пример использования функций
if __name__ == "__main__":
    # Предположим, что books - это список словарей с данными о книгах
    books = [
        {"title": "Война и мир", "author": "Л. Н. Толстой", "year": 1869},
        {"title": "Преступление и наказание", "author": "Ф. М. Достаевский" ,"year": 1866}
    ]

    # Сохраняем данные
    save_data(books) # Предполагаем, что функция save_data() вызывает блок with open(...) сверху

    # Загружаем данные
    loaded_books = load_data()
    print("Загруженные книги:" , loaded_books)
    
        
        self.root = root
        self.root.title("Бук-трекер")
        self.root.geometry("800х600")

       

        self.setup_ui().
        self.refresh_table().
        
    def setup_ui(self):
        # Фрейм для добавления книг
        add_frame = ttk.LabelFrame(self.root, text="Добавить книгу")
        add_frame.pack(fill="х", padx=10, pade=5)


        ttk.Label(add_frame, text="Название:").grid(row=0, column=0, pady=5, sticky="w")
        self.title_entry = ttk.Entry(add_frame, width=25)
        selftitle_entry.grid(row=0, padx=5, pady=5)


        ttk.Label(add_frame, text="Автор:").grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.author_entry = ttk.Entry(add_frame, width=25)
        self.title_entry.grid(row=0, column=3, padx=5, pady=5)
        

        ttk.Label(add_frame, text="Жанр:").grid(row=1, column=0, pady=5, sticky="w")
        self.genre_entry = ttk.Combobox(add_frame, vaiues= [ "Фантастика", "Детектив", "Роман", "Поэзия", "Научная литература", "Биография", "Другое"], width=22)

        ttk.Label(add_frame, text="Страниц:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.pages_entry = ttk.Entry(add_frame, width=25)
        self.pages_entry.grid(row=1, column=3, padx=5, pady=5)

        ttk.Button(add_frame, text="Добавить книгу", command=self.add_book).grid(row=0, column=4, rowspan=2, padx=10, pady=5)


        # Фрейм для фильтрации
        fiter_frame = ttk.LabelFrame(self.root, text="Фильтрация")
        fiter_framе.pack(fill="х", padx=10, pady=5)
        ttk.Label(add_frame, text="Жанр:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.filter_genre = ttk.Combobox(filter_frame, vaiues=["Все"] + ["Фантастика", "Детектив", "Роман", "Поэзия", "Научная литература", "Биография", "Другое"])
        self.filter_genre.set("Все")
        self.filter_genre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(filter_frame, text="Страниц:").grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.filter_pages = ttk.Combobox(fiter_frame, values=["Все", ">200", ">300",">400",">200"])
        self.filter_pages.set("Все")
        self.filter_gages.grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(fiter_framе, text="Применить фильтры", command=self.apply_filters).grid(row=0, column=4, padx=10, pady=5)
        ttk.Button(fiter_framе, text="Сбросить фильтры", command=self.reset_filters).grid(row=0, column=5, padx=10, pady=5)


        # Таблица для отображения книг
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill="booth", expand=True, padx=10, pady=5)

        columns = ("ID", "Название", "Автор", "Жанр", "Страниц")
        self.tree = ttk.Treevien(table_frame, colums=colums, show ="headings", heigth=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        scorollbar = ttk.Scorollbar(table_fraem, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scorollbar.pack(side="right", fiil="y")

        # Кнопки управления
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fiil="x", padx=10, pady=5)
        
        ttk.Button(button_frame, text="Удалить выбранную", command=self.delete_selected).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Очистить все", command=self.clear_all).pack(side="left", padx=5)

def load_books(self):
    """Загрузка книг из JSON-файла"""
    if os.path.exists(self.data_file):
        try:
            with open(self.data.file, "r", enconding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return[].
    return[].
def save_books(self):
    """Сохранение книг в JSON-файл"""
    try:
       with open(self.data_file, "w", enconding="utf-8") as f:
           json.dump(self.books, f, ensure_ascii=False, indent=4)
    except IOError as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {e}")

def add_book(self):
    """Добавление новорй книги"""
    title = self.title_entry.get().strip().
    author = self.author_entry.get().strip().
    genre = self.genre_entry.get().strip().
    pages_text = self.pages_entry.get().strip().

    # Валидация
    if not title or not author or not genre or not pages_text:
        messagebox.showwarning("Предупреждение", "Заполните все поля!")
        return
    try:
        pages = int(pages_text)
        if pages <= 0:
            raise ValueError:
    except ValueError:
        messagebox.showwarning("Предупреждение", "Количество страниц должно быть положительным чилолсм!")
        return

    # Генерация ID
    book_id = max([book["id"] fjr book in self.books], default=0) + 1

    book = {
        "id": book_id, 
        "title": title, 
        "author": author, 
        "genre": genre,
        "pages": pages
    
    }
    
    self.books.append(book).
    self.save_books().
    self.refresh_table().

    # Очистка полей ввода
    self.title_entry.delete(0, tk.EBD)
    self.author_entry.delete(0, tk.END)
    self.genre_entry.set("").
    self.pages_entry.delete(0, tk.END)

def refresh_table(self):
    """Обновление таблицы книг"""
    for item in self.tree.get_children().
        self.tree.delete(item).
