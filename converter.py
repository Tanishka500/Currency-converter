import tkinter as tk
from tkinter import ttk

exchange_rates = {
    "US Dollar (USD)": 1.0,
    "Euro (EUR)": 0.85,
    "British Pound (GBP)": 0.75,
    "Indian Rupee (INR)": 75.0,
    "Japanese Yen (JPY)": 110.0,
    "Canadian Dollar (CAD)": 1.25,
    "Australian Dollar (AUD)": 1.35,
    "Swiss Franc (CHF)": 0.92,
    "Chinese Yuan (CNY)": 6.5,
    "Russian Ruble (RUB)": 74.0
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()
        
        if from_currency and to_currency:
            converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
            result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            result_label.config(text="Please select both currencies.")
    except ValueError:
        result_label.config(text="Invalid amount.")

root = tk.Tk()
root.title("Currency Converter")
root.configure(bg="#354A21") 

label_font = ("Times Roman", 12, "bold")
entry_font = ("Times Roman", 12, "bold")
result_font = ("Times Roman", 14, "bold")

tk.Label(root, text="Amount:", font=label_font, bg="#354A21", fg="black").grid(column=0, row=0, padx=10, pady=10)
amount_entry = tk.Entry(root, font=entry_font)
amount_entry.grid(column=1, row=0, padx=10, pady=10)

tk.Label(root, text="From:", font=label_font, bg="#354A21", fg="black").grid(column=0, row=1, padx=10, pady=10)
from_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()), font=entry_font)
from_currency_combobox.grid(column=1, row=1, padx=10, pady=10)

tk.Label(root, text="To:", font=label_font, bg="#354A21", fg="black").grid(column=0, row=2, padx=10, pady=10)
to_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()), font=entry_font)
to_currency_combobox.grid(column=1, row=2, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_currency, font=label_font, bg="black", fg="white")
convert_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=result_font, bg="#354A21", fg="black")
result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

root.mainloop()