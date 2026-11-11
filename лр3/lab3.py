import tkinter as tk
from tkinter import messagebox
from string import ascii_uppercase, digits
import random
import os
import winsound

SYMBOLS = ascii_uppercase + digits
TITLE = 'KEYGEN'

BG = '#1e1e1e'
TEXT = '#e8e8e8'
BUTTON = '#3a3a3a'


def make_block(digit):
    block = []
    for i in range(5):
        block.append(random.choice(SYMBOLS))
    block[random.randint(0, 4)] = digit
    return ''.join(block)


def make_key(dec):
    block1 = make_block(dec[0])
    block2 = make_block(dec[1])
    block3 = make_block(dec[2])
    return f'{block1}-{block2}-{block3} {dec[-2:]}'


def animate(key, step):
    if step < 15:
        text = ''
        for ch in key:
            if ch == '-' or ch == ' ':
                text += ch
            else:
                text += random.choice(SYMBOLS)
        key_label.configure(text=text)
        window.after(50, animate, key, step + 1)
    else:
        key_label.configure(text=key)
        btn.configure(state='normal')


def type_title(pos):
    if pos <= len(TITLE):
        title_label.configure(text=TITLE[:pos] + '_')
        delay = random.randint(80, 350)
        if random.randint(1, 5) == 1:
            delay += 500
        window.after(delay, type_title, pos + 1)
    else:
        blink_cursor(True)


def blink_cursor(show):
    if show:
        title_label.configure(text=TITLE + '_')
    else:
        title_label.configure(text=TITLE + ' ')
    window.after(500, blink_cursor, not show)


def start_music():
    if os.path.exists('music.wav'):
        winsound.PlaySound('music.wav',
                           winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)


def on_close():
    winsound.PlaySound(None, 0)
    window.destroy()


def copy_key():
    key = key_label.cget('text')
    if key == 'XXXXX-XXXXX-XXXXX XX':
        return
    window.clipboard_clear()
    window.clipboard_append(key)
    copy_btn.configure(text='Скопировано!')
    window.after(1000, reset_copy_text)


def reset_copy_text():
    copy_btn.configure(text='Копировать')


def generate():
    hex_num = hex_entry.get().upper()

    if len(hex_num) != 5:
        messagebox.showwarning('Ошибка', 'Введите HEX-число из 5 символов')
        return
    for ch in hex_num:
        if ch not in '0123456789ABCDEF':
            messagebox.showwarning('Ошибка', 'Допустимы только символы 0-9 и A-F')
            return

    dec = str(int(hex_num, 16))
    if len(dec) < 5:
        messagebox.showwarning('Ошибка', f'{hex_num} = {dec} - меньше 5 цифр')
        return

    btn.configure(state='disabled')
    animate(make_key(dec), 0)


window = tk.Tk()
window.title('KeyGen')
window.geometry('600x350')
window.resizable(0, 0)
window.protocol('WM_DELETE_WINDOW', on_close)

bg_img = tk.PhotoImage(file='bg.png')
label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(window, text='', font=('Consolas', 20),
                       bg=BG, fg=TEXT)
title_label.place(x=12, y=12)

frame = tk.Frame(window, bg=BG)
frame.place(x=12, y=-12, rely=1.0, anchor='sw')

hex_label = tk.Label(frame, text='HEX:', font=('Segoe UI', 12),
                     bg=BG, fg=TEXT)
hex_label.grid(row=0, column=0, padx=(0, 8))

hex_entry = tk.Entry(frame, width=7, font=('Consolas', 14))
hex_entry.insert(0, '54CD1')
hex_entry.grid(row=0, column=1)

btn = tk.Button(frame, text='Сгенерировать', width=13, font=('Segoe UI', 11),
                bg=BUTTON, fg=TEXT, relief='flat', command=generate)
btn.grid(row=0, column=2, padx=(8, 0))

key_label = tk.Label(frame, text='XXXXX-XXXXX-XXXXX XX', font=('Consolas', 16),
                     bg=BG, fg=TEXT)
key_label.grid(row=1, column=0, columnspan=3, pady=(10, 0))

copy_btn = tk.Button(frame, text='Копировать', width=13, font=('Segoe UI', 11),
                     bg=BUTTON, fg=TEXT, relief='flat', command=copy_key)
copy_btn.grid(row=2, column=0, columnspan=3, pady=(8, 0))

start_music()
type_title(0)
window.mainloop()
