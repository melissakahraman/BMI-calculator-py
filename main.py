from tkinter import *

#creat window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=250)

#creat labels
my_label = Label(text="Enter Your Weight (kg)",font=("Arial",11,"normal"))
my_label.config(padx=40,pady=40)
my_label.pack()

my_label_2 = Label(text="Enter Your Height (cm)",font=("Arial",11,"normal"))
my_label_2.pack()

#creat entries
my_entry = Entry(width=15)
my_entry.place(x=75,y=70)

my_entry_2 = Entry(width=15)
my_entry_2.place(x=75,y=135)

#creat button


def click_button():
    weight = my_entry.get()
    height = my_entry_2.get()
    if weight == "" or height == "":
        calculate_label =Label(text= "Enter both weight and height!")
        calculate_label.place(x=30, y=200)
    else:
        try:
            height = float(float(height) / 100.0)
            bmi = float(float (weight) / float (height * height))
        except:
            calculate_label = Label(text="Enter a valid number!")
            calculate_label.place(x=30, y=200)
    if (bmi <= 18.5):
        calculate_label =Label(text= f"Your BMI is {bmi:.1f} You are under weight.")
        calculate_label.place(x=25, y=200)
    elif (bmi<= 24.9):
        calculate_label=Label(text=f"Your BMI is {bmi:.1f} You are normal.")
        calculate_label.place(x=25, y=200)
    elif (bmi<= 29.9):
        calculate_label=Label(text=f"Your BMI is {bmi:.1f} You are over weight.")
        calculate_label.place(x=25, y=200)
    elif (bmi<= 34.9):
        window.update()
        calculate_label=Label(text=f"Your BMI is {bmi:.1f} You are obesity (class I).")
        calculate_label.place(x=25, y=200)
    elif (bmi<= 39.9):
        window.update()
        calculate_label=Label(text=f"Your BMI is {bmi:.1f} You are obesity (class II).")
        calculate_label.place(x=25, y=200)
    else:
        calculate_label=Label(text=f"Your BMI is {bmi:.1f} You are extreme Obesity.")
        calculate_label.place(x=25, y=200)

button = Button(text="Calculate", command= click_button)
button.place(x=95,y=165)

window.mainloop()