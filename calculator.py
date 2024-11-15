import tkinter as tk

# Using tkinter we create the main window for the calculator app
window = tk.Tk()
window.title("My Python Calculator")
window.geometry("500x500")
window.configure(bg = "gray")

# Initialize important variables
equation = ""
currentOperator = ""
currNum = ""

# Configure the grid to center content
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Display the solution label
solutionLabel = tk.Label(window, text="0", font=("Arial", 50), bg="lightblue", fg="black")
solutionLabel.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

# Button variables
buttonWidth = 5
buttonHeight = 2
buttonFont = ("Arial", 20)

# Functions for operation buttons
def addFunc():
    global equation, currentOperator, currNum
    if equation:
        currentOperator = "+"
        equation += currentOperator
        currNum = ""
        solutionLabel.config(text = currentOperator)

def subFunc():
    global equation, currentOperator, currNum
    if equation:
        currentOperator = "-"
        equation += currentOperator
        currNum = ""
        solutionLabel.config(text = currentOperator)

def multFunc():
    global equation, currentOperator, currNum
    if equation:
        currentOperator = "*"
        equation += currentOperator
        currNum = ""
        solutionLabel.config(text = currentOperator)

def divFunc():
    global equation, currentOperator, currNum
    if equation:
        currentOperator = "/"
        equation += currentOperator
        currNum = ""
        solutionLabel.config(text = currentOperator)

def solveFunc():
    global equation, currNum
    try:
        result = eval(equation)  
        equation = str(result)  
        currNum = ""
        solutionLabel.config(text = equation)  
    except Exception as e:
        solutionLabel.config(text="Error")
        equation = ""

def numberFunc(num):
    global equation, currNum
    equation += str(num) 
    currNum += str(num)
    solutionLabel.config(text = currNum)

def clearFunc():
    global equation, currNum
    equation = ""
    currNum = ""
    solutionLabel.config(text = equation)

# Create buttons and arrange in a grid
button_texts = [
    ("7", lambda: numberFunc(7)), ("8", lambda: numberFunc(8)), ("9", lambda: numberFunc(9)), ("*", multFunc, "lightyellow"),
    ("4", lambda: numberFunc(4)), ("5", lambda: numberFunc(5)), ("6", lambda: numberFunc(6)), ("/", divFunc, "lightyellow"),
    ("1", lambda: numberFunc(1)), ("2", lambda: numberFunc(2)), ("3", lambda: numberFunc(3)), ("-", subFunc, "lightyellow"),
    ("C", clearFunc, "lightcoral"),
    ("0", lambda: numberFunc(0)), ("=", solveFunc, "lightgreen"), ("+", addFunc, "lightyellow"),
]

# Arrange buttons in rows
row, col = 1, 0
for button_info in button_texts:
    if button_info[0] is not None:  
        text, command = button_info[:2]
        bg_color = button_info[2] if len(button_info) > 2 else "white"  
        tk.Button(
            window,
            text=text,
            width=buttonWidth,
            height=buttonHeight,
            command=command,
            font=buttonFont,
            bg=bg_color,
            fg="black",
        ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3: 
        col = 0
        row += 1

# Start the main loop
window.mainloop()
