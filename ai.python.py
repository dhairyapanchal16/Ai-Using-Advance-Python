import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

root=tk.Tk()
root.title("Python Ai")

root.configure(bg='black')
def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_google():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


Label(root, text="Enter your Command ").pack(pady=20)
entry=Entry(root, width=50)
entry.pack(pady=10)
Button(root, text="Search on Youtube", command=search_youtube).pack(pady=10)
Button(root, text="Search on Google", command=search_google).pack(pady=10)
root.mainloop()


#                                      Python Ai Made By Dhairya Panchal
#                                                Thank You
