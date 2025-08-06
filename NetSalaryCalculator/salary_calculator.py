import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_net_salary(gross_salary):
    CAS = 0.25
    CASS = 0.10
    tax_rate = 0.10

    social_security = gross_salary * CAS
    health_insurance = gross_salary * CASS
    taxable_income = gross_salary - social_security - health_insurance
    income_tax = taxable_income * tax_rate
    net_salary = gross_salary - social_security - health_insurance - income_tax

    save_to_file(gross_salary, social_security, health_insurance, income_tax, net_salary)

    return social_security, health_insurance, income_tax, net_salary

def save_to_file(gross_salary, social_security, health_insurance, income_tax, net_salary):
    with open("salary_report.txt", "a", encoding="utf-8") as file:
        file.write(f"\n--- Salary Breakdown ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
        file.write(f"Gross Salary: {gross_salary:.2f} RON\n")
        file.write(f"CAS (25%): {social_security:.2f} RON\n")
        file.write(f"CASS (10%): {health_insurance:.2f} RON\n")
        file.write(f"Income Tax (10%): {income_tax:.2f} RON\n")
        file.write(f"Net Salary: {net_salary:.2f} RON\n")
        file.write("--------------------------------------------------------\n")

def on_calculate():
    try:
        gross_salary = float(entry_salary.get())
        if gross_salary <= 0:
            messagebox.showwarning("Eroare", "Introdu un salariu brut mai mare decât zero.")
            return
        cas, cass, tax, net = calculate_net_salary(gross_salary)
        exchange_rate = 5.07
        net_eur = net / exchange_rate
        result_text.set(
            f"CAS (25%): {cas:.2f} RON\n"
            f"CASS (10%): {cass:.2f} RON\n"
            f"Tax (10%): {tax:.2f} RON\n"
            f"Net Salary: {net:.2f} RON\n"
            f"Net Salary: {net_eur:.2f} EUR"
        )
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

root = tk.Tk()
root.title("Net Salary Calculator")
root.geometry("400x300")
root.configure(bg="blue")

tk.Label(root, bg="yellow", fg="purple", text="Gross salary (RON):").pack(pady=10)
entry_salary = tk.Entry(root)
entry_salary.pack()

tk.Button(root, bg="green", fg="white", text="CALCULATED!", command=on_calculate).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left",bg="blue", fg="white").pack(pady=10)

done_button = tk.Button(root, bg="red", fg="white", text="FINISH!", command=root.destroy)
done_button.pack(pady=10)

root.mainloop()
