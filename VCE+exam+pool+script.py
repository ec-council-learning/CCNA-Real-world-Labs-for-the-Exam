import tkinter as tk
import random

# Function to generate and display random numbers
def generate_numbers():
    # Generate a random number from 1 to 2 for VCE
    num_vce = random.randint(1, 2)
    label_vce.config(text=f"The {num_vce} > for VCE")

    # Generate a random number from 1 to 6 for Udemy exams
    num_udemy = random.randint(1, 6)
    label_udemy.config(text=f"The {num_udemy} > for Udemy exams")

    # Generate four random numbers from 1 to 23 for PKT labs
    num_pkt = random.sample(range(1, 24), 4)
    label_pkt.config(text=f"The {num_pkt} > for PKT labs")

    # Generate a random number from 1 to 7 for CCNA dumps PDFs
    num_ccna = random.randint(1, 7)
    label_ccna.config(text=f"The {num_ccna} > for CCNA dumps PDFs")

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")

# Create labels to display the results
label_vce = tk.Label(root, text="The # > for VCE")
label_vce.pack(pady=5)

label_udemy = tk.Label(root, text="The # > for Udemy exams")
label_udemy.pack(pady=5)

label_pkt = tk.Label(root, text="The # > for PKT labs")
label_pkt.pack(pady=5)

label_ccna = tk.Label(root, text="The # > for CCNA dumps PDFs")
label_ccna.pack(pady=5)

# Create a button to generate the numbers
button_generate = tk.Button(root, text="Generate Numbers", command=generate_numbers)
button_generate.pack(pady=20)

# Start the main loop of the graphical interface
root.mainloop()
