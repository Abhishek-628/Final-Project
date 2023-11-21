import tkinter as tk
import csv

class AutoComplete:
    def run(self):
        self.words = self.load_words("C:\\Users\\Abhishek Madhav\\Desktop\\Atria\\Python\\FInal-Project\\4000-most-common-english-words-csv.csv")

        self.root = tk.Tk()
        self.root.title("Auto-Complete Tool")

        self.entry = tk.Entry(self.root, font=("Arial", 16))
        self.entry.pack(padx=10, pady=10)

        self.listbox = tk.Listbox(self.root, font=("Arial", 16))
        self.listbox.pack(padx=10, pady=10)

        self.listbox.bind("<Double-Button-1>", self.select_word)
        self.entry.bind("<KeyRelease>", self.autocomplete)

        self.root.mainloop()

    def autocomplete(self, event):
        prefix = self.entry.get()
        options = self.lookup(prefix)

        self.listbox.delete(0, tk.END)
        for option in options:
            self.listbox.insert(tk.END, option)

    def lookup(self, prefix):
        matches = []
        for word in self.words:
            if word.startswith(prefix):
                matches.append(word)
        return matches

    def select_word(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            word = self.listbox.get(index)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, word)

    def load_words(self, file_path):
        words = []
        with open(file_path) as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    words.append(row[0])
        return words

if __name__ == "__main__":
    app = AutoComplete()
    app.run()
