import tkinter as tk
from tkinter import messagebox
from pyshorteners import Shortener

class URLShortenerApp:
    def __init__(self, master):
        self.master = master
        master.title("Advanced URL Shortener with Analytics")
        master.geometry("700x300")
        master.configure(bg="pink")

        self.label = tk.Label(master, text="Enter URL:",font= ("Georgia 25 bold"), bg="white", fg="blue")
        self.label.pack()

        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack()
       

        self.shorten_button = tk.Button(master, text="Shorten URL",font= ("Georgia 15 bold"), command=self.shorten_url, bg="green", fg="white")
        self.shorten_button.pack()

        self.analytics_button = tk.Button(master, text="View Analytics",font= ("Georgia 10 bold"), command=self.view_analytics, bg="blue", fg="white")

    def shorten_url(self):
        url = self.url_entry.get()
        shortener = Shortener()
        short_url = shortener.tinyurl.short(url)
        messagebox.showinfo("Shortened URL", f"Shortened URL: {short_url}")

    def view_analytics(self):
        urls = ['URL 1', 'URL 2', 'URL 3', 'URL 4']
        clicks = [50, 100, 150, 200]

        plt.bar(urls, clicks)
        plt.xlabel('URLs')
        plt.ylabel('Clicks')
        plt.title('URL Click Analytics')
        plt.show()

def main():
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
