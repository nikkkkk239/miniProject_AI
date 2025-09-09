import tkinter as tk
from tkinter import messagebox

atm_notes = {2000: 10, 500: 20, 200: 30, 100: 50}

def dispense_cash(amount, denominations):
    result = {}
    for note in sorted(denominations.keys(), reverse=True):
        if amount >= note and denominations[note] > 0:
            count = min(amount // note, denominations[note])
            result[note] = count
            amount -= note * count
            denominations[note] -= count  

    if amount == 0:
        return result
    else:
        return None


def withdraw():
    try:
        amount = int(entry.get())
        if amount <= 0:
            messagebox.showerror("Invalid Input", "Enter a positive amount.")
            return
        if amount % 100 != 0:
            messagebox.showerror("Invalid Input", "Amount must be multiple of 100.")
            return

        result = dispense_cash(amount, atm_notes.copy())  
        if result:
            output_text = "Dispensed:\n"
            for note, count in result.items():
                output_text += f"₹{note} x {count}\n"
            messagebox.showinfo("Transaction Successful", output_text)
        else:
            messagebox.showerror("Error", "Cannot dispense this amount with available notes.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


root = tk.Tk()
root.title("ATM Cash Dispenser")
root.geometry("400x300")

label = tk.Label(root, text="Enter Withdrawal Amount (₹):", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

withdraw_btn = tk.Button(root, text="Withdraw", font=("Arial", 12, "bold"), command=withdraw)
withdraw_btn.pack(pady=10)

root.mainloop()
