import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x370")
root.configure(bg="blue")

player = "X"
ai = "O"
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    for i in range(3):
        # linii
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]
        # coloane
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]

    # diagonale
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    # remiza
    if all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        return "Draw"

    return None

def disable_all():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

def ai_move():
    empty = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]["text"] == ""]
    if empty:
        i, j = random.choice(empty)
        buttons[i][j].config(text=ai, state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Result", "It's a draw!")
            else:
                messagebox.showinfo("Result", f"{winner} wins!")
            disable_all()

def player_move(i, j):
    if buttons[i][j]["text"] == "":
        buttons[i][j].config(text=player, state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Result", "It's a draw!")
            else:
                messagebox.showinfo("Result", f"{winner} wins!")
            disable_all()
        else:
            root.after(500, ai_move)  # AI mută după 0.5 secunde

# creare butoane
for i in range(3):
    for j in range(3):
        b = tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2,
                      command=lambda i=i, j=j: player_move(i, j), bg="white")
        b.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = b

# buton de restart (opțional)
def restart_game():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal", bg="white")

restart_btn = tk.Button(root, text="Restart", font=("Helvetica", 12),
                        command=restart_game, bg="gray", fg="white")
restart_btn.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
