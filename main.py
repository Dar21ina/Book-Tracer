
import json
import random
import tkinter as tk
from tkinter import messagebox


QUOTES_FILE = "quotes.json"
HISTORY_FILE = "history.json"


default_quotes = [
    {
        "text": "Ученье — свет, а неученье — тьма.",
        "author": "Народная мудрость",
        "theme": "Образование"
    },
    {
        "text": "Знание — сила.",
        "author": "Фрэнсис Бэкон",
        "theme": "Знания"
    },
    {
        "text": "Дорогу осилит идущий.",
        "author": "Народная мудрость",
        "theme": "Мотивация"
    },
    {
        "text": "Великие дела начинаются с маленьких шагов.",
        "author": "Неизвестный автор",
        "theme": "Мотивация"
    },
    {
        "text": "Время — самый ценный ресурс.",
        "author": "Бенджамин Франклин",
        "theme": "Время"
    }
]


quotes = []
history = []


def load_data():
    """Загружает цитаты и историю из JSON-файлов."""
    global quotes, history

    try:
        with open(QUOTES_FILE, "r", encoding="utf-8") as file:
            quotes = json.load(file)
    except FileNotFoundError:
        quotes = default_quotes.copy()
        save_quotes()
    except json.JSONDecodeError:
        quotes = default_quotes.copy()
        save_quotes()

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []
        save_history()
    except json.JSONDecodeError:
        history = []
        save_history()


def save_quotes():
    """Сохраняет список цитат в файл quotes.json."""
    with open(QUOTES_FILE, "w", encoding="utf-8") as file:
        json.dump(quotes, file, ensure_ascii=False, indent=4)


def save_history():
    """Сохраняет историю цитат в файл history.json."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)


def generate_quote():
    """Выбирает случайную цитату и добавляет её в историю."""

    if not quotes:
        messagebox.showwarning("Ошибка", "Список цитат пуст.")
        return

    quote = random.choice(quotes)

    quote_text = quote["text"]
    quote_author = quote["author"]
    quote_theme = quote["theme"]

    result_label.config(
        text=f"«{quote_text}»\nАвтор: {quote_author}\nТема: {quote_theme}"
    )

    history.append(quote)
    save_history()
    update_history_listbox(history)


def update_history_listbox(items):
    """Обновляет список истории цитат."""

    history_listbox.delete(0, tk.END)

    for quote in items:
        history_listbox.insert(
            tk.END,
            f"{quote['author']} | {quote['theme']} | {quote['text']}"
        )


def add_quote():
    """Добавляет новую цитату с проверкой пустых строк."""

    text = quote_entry.get().strip()
    author = author_entry.get().strip()
    theme = theme_entry.get().strip()

    if text == "" or author == "" or theme == "":
        messagebox.showwarning(
            "Ошибка",
            "Заполните текст цитаты, автора и тему."
        )
        return

    new_quote = {
        "text": text,
        "author": author,
        "theme": theme
    }

    quotes.append(new_quote)
    save_quotes()

    quote_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    theme_entry.delete(0, tk.END)

    update_filter_menus()

    messagebox.showinfo("Успешно", "Новая цитата добавлена.")


def filter_history():
    """Фильтрует историю по автору и теме."""

    selected_author = author_filter.get()
    selected_theme = theme_filter.get()

    filtered_history = []

    for quote in history:
        author_matches = (
            selected_author == "Все авторы"
            or quote["author"] == selected_author
        )

        theme_matches = (
            selected_theme == "Все темы"
            or quote["theme"] == selected_theme
        )

        if author_matches and theme_matches:
            filtered_history.append(quote)

    update_history_listbox(filtered_history)


def reset_filter():
    """ Сбрасывает фильтры истории."""

    author_filter.set("Все авторы")
    theme_filter.set("Все темы")
    update_history_listbox(history)


def update_filter_menus():
    """Обновляет выпадающие списки авторов и тем."""

    authors = sorted(set(quote["author"] for quote in quotes))
    themes = sorted(set(quote["theme"] for quote in quotes))

    author_menu["menu"].delete(0, tk.END)
    theme_menu["menu"].delete(0, tk.END)

    author_menu["menu"].add_command(
        label="Все авторы",
        command=lambda: author_filter.set("Все авторы")
    )

    for author in authors:
        author_menu["menu"].add_command(
            label=author,
            command=lambda value=author: author_filter.set(value)
        )

    theme_menu["menu"].add_command(
        label="Все темы",
        command=lambda: theme_filter.set("Все темы")
    )

    for theme in themes:
        theme_menu["menu"].add_command(
            label=theme,
            command=lambda value=theme: theme_filter.set(value)
        )


window = tk.Tk()

window.title("Генератор цитат")
window.geometry("700x600")
window.resizable(False, False)


title_label = tk.Label(
    window,
    text="Генератор цитат",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)


result_label = tk.Label(
    window,
    text="Нажмите кнопку, чтобы сгенерировать цитату",
    font=("Arial", 12),
    wraplength=600,
    justify="center"
)
result_label.pack(pady=10)


generate_button = tk.Button(
    window,
    text="Сгенерировать цитату",
    font=("Arial", 11),
    command=generate_quote
)
generate_button.pack(pady=5)


add_frame = tk.Frame(window)
add_frame.pack(pady=10)

tk.Label(add_frame, text="Текст цитаты:").grid(row=0, column=0, padx=5, pady=3)
quote_entry = tk.Entry(add_frame, width=50)
quote_entry.grid(row=0, column=1, padx=5, pady=3)

tk.Label(add_frame, text="Автор:").grid(row=1, column=0, padx=5, pady=3)
author_entry = tk.Entry(add_frame, width=50)
author_entry.grid(row=1, column=1, padx=5, pady=3)

tk.Label(add_frame, text="Тема:").grid(row=2, column=0, padx=5, pady=3)
theme_entry = tk.Entry(add_frame, width=50)
theme_entry.grid(row=2, column=1, padx=5, pady=3)

add_button = tk.Button(
    add_frame,
    text="Добавить цитату",
    command=add_quote
)
add_button.grid(row=3, column=1, pady=5)


filter_frame = tk.Frame(window)
filter_frame.pack(pady=10)

tk.Label(filter_frame, text="Фильтр по автору:").grid(
    row=0,
    column=0,
    padx=5
)

author_filter = tk.StringVar(value="Все авторы")
author_menu = tk.OptionMenu(filter_frame, author_filter, "Все авторы")
author_menu.grid(row=0, column=1, padx=5)

tk.Label(filter_frame, text="Фильтр по теме:").grid(
    row=0,
    column=2,
    padx=5
)

theme_filter = tk.StringVar(value="Все темы")
theme_menu = tk.OptionMenu(filter_frame, theme_filter, "Все темы")
theme_menu.grid(row=0, column=3, padx=5)

filter_button = tk.Button(
    filter_frame,
    text="Применить фильтр",
    command=filter_history
)
filter_button.grid(row=1, column=1, pady=5)

reset_button = tk.Button(
    filter_frame,
    text="Сбросить фильтр",
    command=reset_filter
)
reset_button.grid(row=1, column=2, pady=5)


history_label = tk.Label(
    window,
    text="История сгенерированных цитат:",
    font=("Arial", 12, "bold")
)
history_label.pack(pady=5)


history_listbox = tk.Listbox(window, width=90, height=10)
history_listbox.pack(pady=5)


load_data()
update_filter_menus()
update_history_listbox(history)

window.mainloop()
