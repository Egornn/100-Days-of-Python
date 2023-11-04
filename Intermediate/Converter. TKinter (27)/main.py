import tkinter as tk

MILE_TO_KM = 1.60934
FONT = font = ('Courier', 15)


def convert():
    print(entry_input.get())
    km = "%.2f" % (float(entry_input.get()) * MILE_TO_KM)
    km_converted.config(text=km)


window = tk.Tk()
window.minsize(200, 100)
window.config(padx=30, pady=20)
window.title("Mile to Kilometres Converter")

entry_input = tk.Entry(width=5, font=FONT, )
entry_input.insert(0, string='0')
entry_input.grid(row=0, column=1)

miles_label = tk.Label(text='miles', font=FONT)
miles_label.grid(row=0, column=2)

km_labels = tk.Label(text='km', font=FONT)
km_labels.grid(row=1, column=2)

equal_label = tk.Label(text='is equal to', font=FONT)
equal_label.grid(row=1, column=0)

km_converted = tk.Label(text='0.00', font=FONT)
km_converted.grid(row=1, column=1)

convert_button = tk.Button(text='Convert!', command=convert, font=FONT, padx=5)
convert_button.grid(row=2, column=1)

window.mainloop()
