import tkinter as tk
from tkinter import messagebox
import pygame

# Initialize Pygame mixer for sound playback
pygame.mixer.init()

# Define a dictionary of guitar notes and their sound files
NOTES = {
    "E": "sounds/E.wav",
    "A": "sounds/A.wav",
    "D": "sounds/D.wav",
    "G": "sounds/G.wav",
    "B": "sounds/B.wav",
    "e": "sounds/high_E.wav",
}

# Function to play a note
def play_sound(note):
    try:
        sound = pygame.mixer.Sound(NOTES[note])
        sound.play()
    except Exception as e:
        messagebox.showerror("Error", f"Could not play note: {note}\n{e}")

# GUI setup
def create_guitar_app():
    root = tk.Tk()
    root.title("Guitar App")

    tk.Label(root, text="Guitar Simulator", font=("Arial", 16)).pack(pady=10)

    # Create buttons for each note
    for note in NOTES.keys():
        button = tk.Button(
            root, 
            text=note, 
            font=("Arial", 14), 
            width=10, 
            command=lambda n=note: play_sound(n)
        )
        button.pack(pady=5)

    root.mainloop()

# Run the app
if __name__ == "__main__":
    create_guitar_app()
