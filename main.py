from tkinter import *


# -----Predict Digit-----
def predict_digit(image):
    print("DELETE ME. I'm only here to avoid an indent error.")
    # convert to grayscale and resize the image.
    # Reshape the image for model input.
    # Predicts the class.

# ------Writing To Text-----
def writing_to_text():
    # Variables
    accuracy = 0.00
    digit = 2 #----------DELETE. Only here to make sure the program runs.

    # Get the id and coordinates of the canvas.

    # Initialize image from the coordinates of the canvas.

    # Assign values to digit and accuracy

    # If digit and accuracy were assigned values, show
    # the results. Otherwise, an alert will popup.
    if (str(digit).isalnum()) and (accuracy > 0.00):
        show_results(digit, accuracy)
    else:
        invalid_prediction_popup()

# ------Show Digit-------
def show_results(digit,accuracy):

    # Update the predicted number.
    predicted_number_label.config(text=digit)

    # Verifies accuracy entry is empty & updates.
    if len(accuracy_entry.get())<1:
        accuracy_entry.insert(0,(str(accuracy)+'%'))

# -------Alert Popup------
def invalid_prediction_popup():

    # Initializes the popup window
    popup_window = Tk()
    popup_window.title("Error")
    popup_window.geometry("305x100")

    # Shows error message.
    popup_label = Label(popup_window, text = "Invalid prediction. Please clear and "
                                            "try again.")
    popup_label.pack(side="top",fill="x",pady=20)

    # User press okay and window is closed.
    okay_button = Button(popup_window,text = "Okay",command = popup_window.destroy)
    okay_button.pack()

# ------Clear------
def clear():

    # Clears all entries and writings.
    canvas_draw.delete("all")
    predicted_number_label.config(text="")
    accuracy_entry.delete(0,'end')

# ------Write Digit------
def write_digit(event):

    # Variables
    ballpoint_size=7
    x=event.x
    y=event.y

    # Allows the user to "write".
    canvas_draw.create_oval((x - ballpoint_size), (y - ballpoint_size), (x + ballpoint_size),
                            (y + ballpoint_size), fill='black')

# -----UI Setup-------
window = Tk()
window.title("Digit Recognizer")
window.configure(bg="#0099cc")
window.config(padx=20,pady=20)

# Canvas
canvas_draw = Canvas(height = 222,width = 200,bg = "white")
canvas_draw.grid(row=0,column=0,padx=5,columnspan=2,sticky=W)
canvas_draw.bind("<B1-Motion>",write_digit)
canvas_predicted_number = Canvas(height = 222,width = 200,bg = "white")
canvas_predicted_number.grid(row=0, column=3, columnspan = 5, padx=5, sticky=W)

# Labels
accuracy_label = Label(text = "       Accuracy:",
                       font=("Calibri",15),bg="#0099cc")
accuracy_label.grid(row = 1,column = 0,pady=20)
predicted_number_label = Label(font=("Calibri",110),bg="white")
predicted_number_label.grid(row=0, column=3, columnspan = 5, padx=5)

# Entries
accuracy_entry = Entry(width = 7,font=("Calibri",18))
accuracy_entry.grid(row=1,column=1,columnspan=2,padx=5)

# Buttons
translate_button = Button(text="Translate",width = 12,font=("Calibri",15),
                          command = writing_to_text)
translate_button.grid(row=2,column=0,columnspan=2,pady=15)
clear_button=Button(text="Clear", width = 12, font=("Calibri",15), command = clear)
clear_button.grid(row=2,column=3,columnspan=5,pady=15)

# Loop waits for window close.
window.mainloop()
