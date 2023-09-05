import tkinter as tk
import random

lunch_menu = [
    'Pasta', 'Pizza', 'Hamburger', 'Salad', 'Sushi', 'Sandwich', 'Burrito', 'Taco', 'Chicken Curry', 'Soup', 'Stir-Fry', 'Rice Bowl', 'Fish and Chips', 'Lasagna', 'Hot Dog', 'Quesadilla', 'Caesar Salad', 'Chicken Wrap', 'Grilled Cheese', 'BLT Sandwich', 'Pho', 'Samosa', 'Falafel', 'Beef Stew', 'Miso Soup', 'Gyro', 'Pad Thai'
]

def recommend_menu():
    num_menus = int(num_menus_entry.get())
    random_menus = random.sample(lunch_menu, num_menus)
    menu_label.config(text=", ".join(random_menus))

window = tk.Tk()
window.title("Lunch Menu Recommender")

menu_label = tk.Label(window, text="Please enter the number of menu recommendations you'd like to receive.", font=("Arial", 12))
menu_label.pack(pady=20)

num_menus_entry = tk.Entry(window, width=10, font=("Arial", 14))
num_menus_entry.pack(pady=10)

recommend_button = tk.Button(window, text="Recommend", command=recommend_menu, font=("Arial", 14))
recommend_button.pack(pady=10)

window.mainloop()