import tkinter as tk
import csv

def autocomplete(event):
    prefix = entry.get()
    options = lookup(prefix)

    listbox.delete(0, tk.END)
    for option in options:
        listbox.insert(tk.END, option)

def lookup(prefix):
    matches = []
    for word in words:
        if word.startswith(prefix):
            matches.append(word)
    return matches

def select_word(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        word = listbox.get(index)
        entry.delete(0, tk.END)
        entry.insert(0, word)

def load_words(file_path):
    words = []
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            words.append(row[0])
    return words

if __name__ == "__main__":
    words = load_words("C:\\Users\\Abhishek Madhav\\Desktop\\Atria\\Python\\FInal-Project\\4000-most-common-english-words-csv.csv")

    root = tk.Tk()
    root.title("Auto Complete")

    entry = tk.Entry(root, font=("Arial", 16))
    entry.pack(padx=10, pady=10)

    listbox = tk.Listbox(root, font=("Arial", 16))
    listbox.pack(padx=10, pady=10)

    listbox.bind("<Double-Button-1>", select_word)
    entry.bind("<KeyRelease>", autocomplete)

    root.mainloop()