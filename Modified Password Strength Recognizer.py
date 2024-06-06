import tkinter as tk
from tkinter import ttk

# Import the font module
from tkinter import font

def password_strength_recognizer(password):
    """Recognizes the strength of a password."""
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isalpha() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char in "!@#$%^&*()-+" for char in password):
        score += 1
    return min(score, 5)  # Ensure the score does not exceed 5

def check_password(event=None):  # Added event parameter to handle key press event
    password = entry_field.get()
    score = password_strength_recognizer(password)
    
    strength_label.config(text=f"Strength: {get_strength_message(score)}", fg=get_strength_color(score))
    
    # Change background color based on password strength
    root.config(bg=get_background_color(score))
    
    # Provide suggestions for stronger passwords
    suggestion_label.config(text=get_password_suggestions(password))
    
    # Update star rating
    update_star_rating(score)

def get_strength_message(score):
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    else:
        return "Strong"

def get_strength_color(score):
    if score <= 2:
        return "red"
    elif score == 3:
        return "orange"
    else:
        return "green"

def get_background_color(score):
    if score <= 2:
        return "#FFCCCC"  # Light red
    elif score == 3:
        return "#FFD699"  # Light orange
    else:
        return "#CCFFCC"  # Light green

def get_password_suggestions(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include numbers (e.g., 123)")
    if not any(char.isalpha() for char in password):
        suggestions.append("Include letters (e.g., abc)")
    if not any(char.isupper() for char in password):
        suggestions.append("Include uppercase letters (e.g., ABC)")
    if not any(char.islower() for char in password):
        suggestions.append("Include lowercase letters (e.g., abc)")
    if not any(char in "!@#$%^&*()-+" for char in password):
        suggestions.append("Include special characters (e.g., !@#)")
    return "\n".join(suggestions)

def update_star_rating(score):
    # Create a string of stars
    stars = '★' * score + '☆' * (5 - score)
    
    # Update the star label
    star_label['text'] = stars

# Create the main window
root = tk.Tk()
root.title("Password Strength Recognizer")
root.geometry("400x350")  # Set window size
root.configure(bg="white")  # Set initial background color to white

# Create a frame to hold the widgets (optional for layout)
main_frame = tk.Frame(root, bg="white")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Entry field for password
entry_field = tk.Entry(main_frame, width=30)
entry_field.grid(row=0, column=0, pady=10, columnspan=2)

# Bind the Enter key to the check_password function
entry_field.bind('<Return>', check_password)

# Label for password input
password_label = tk.Label(main_frame, text="Enter Password:")
password_label.grid(row=0, column=1, sticky="e")

# Button to check password
check_button = tk.Button(main_frame, text="Check Strength", command=check_password)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

# Label to display strength message
strength_label = tk.Label(main_frame, text="Strength: ")
strength_label.grid(row=2, column=0, sticky="e")

# Label to display password suggestions
suggestion_label = tk.Label(main_frame, text="", wraplength=300)
suggestion_label.grid(row=3, column=0, columnspan=2, pady=10)

# Star rating to show password strength
star_label = tk.Label(main_frame, text='☆☆☆☆☆', font=("Helvetica", 24))
star_label.grid(row=4, column=0, columnspan=2)

# Run the main loop
root.mainloop()
