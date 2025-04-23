import tkinter as tk
from tkinter import messagebox
import os

# === აქ შეცვალე შენი ფაილების დირექტორია ===
files_dir = "/home/lasha/mytexts"

# === ღილაკების და ფაილების შესაბამისობა ===
buttons = {
    "N3. ფაილური სისტემები. Linux-ის კატალოგების სტრუქტურა": "/home/lasha/lessons.linux/lesson3/examen",
    "ისტორია": "history.txt",
    "ტექნიკა": "tech.txt",
    "პოეზია": "poetry.txt",
    "რომანები": "novels.txt",
    "ზღაპრები": "fairytales.txt",
    "მეცნიერება": "science.txt",
    "პროგრამირება": "coding.txt",
    "ჰაკინგი": "hacking.txt",
    "ლიტერატურა": "literature.txt",
    "ენები": "languages.txt",
    "მუსიკა": "music.txt",
    "ფილმები": "movies.txt",
    "ციტატები": "quotes.txt",
    "სათავგადასავლო": "adventure.txt",
    "ფანტასტიკა": "fantasy.txt",
    "ბიოგრაფია": "biography.txt",
    "მოთხრობები": "stories.txt",
    "ლექსიკონი": "dictionary.txt",
    "ჩანაწერები": "notes.txt"
}

def open_file(filename):
    filepath = os.path.join(files_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        show_text_window(filename, content)
    else:
        messagebox.showerror("შეცდომა", f"ფაილი ვერ მოიძებნა:\n{filepath}")

def show_text_window(title, content):
    text_win = tk.Toplevel(root)
    text_win.title(title)
    text_box = tk.Text(text_win, wrap="word")
    text_box.insert("1.0", content)
    text_box.pack(expand=True, fill="both")

root = tk.Tk()
root.title("ჩემი ტექსტ ფაილები")
root.geometry("400x600")

frame = tk.Frame(root)
frame.pack(pady=10)

for i, (label, filename) in enumerate(buttons.items()):
    btn = tk.Button(frame, text=label, width=55, command=lambda f=filename: open_file(f))
    btn.grid(row=i // 2, column=i % 2, padx=5, pady=5)

root.mainloop()


