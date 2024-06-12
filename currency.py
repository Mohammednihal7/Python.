import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import os

# Function to get exchange rates
def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']

# Function to perform conversion
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()
        
        if from_currency != "USD":
            amount = amount / rates[from_currency]
        
        converted_amount = amount * rates[to_currency]
        result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# Initialize the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x250")
root.configure(bg="pink")  # Set background color to pink

# Fetch exchange rates
rates = get_exchange_rates()

# Configure ttk theme
style = ttk.Style()
style.theme_use('clam')

# GUI Components
amount_label = ttk.Label(root, text="Amount:", background="pink")  # Set background color to pink
amount_label.pack(pady=5)

amount_entry = ttk.Entry(root)
amount_entry.pack(pady=5)

from_currency_label = ttk.Label(root, text="From Currency:", background="pink")  # Set background color to pink
from_currency_label.pack(pady=5)

from_currency_combo = ttk.Combobox(root, values=list(rates.keys()))
from_currency_combo.set("USD")
from_currency_combo.pack(pady=5)

to_currency_label = ttk.Label(root, text="To Currency:", background="pink")  # Set background color to pink
to_currency_label.pack(pady=5)

to_currency_combo = ttk.Combobox(root, values=list(rates.keys()))
to_currency_combo.set("EUR")
to_currency_combo.pack(pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=5)

result_label = ttk.Label(root, text="Converted Amount:", background="pink")  # Set background color to pink
result_label.pack(pady=5)

# Add country flags
image_dir = os.path.join(os.getcwd(), "images")
flag_photo_images = {}
for currency in rates.keys():
    image_path = os.path.join(image_dir, f"{currency.lower()}_flag.png")
    if os.path.exists(image_path):
        flag_photo_images[currency] = ImageTk.PhotoImage(Image.open(image_path).resize((30, 20), Image.ANTIALIAS))

# Run the main loop
root.mainloop()