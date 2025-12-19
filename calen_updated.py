import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import calendar

selected_font = "arial.ttf"  # Default font type
selected_size = 40           # Default font size
selected_background = None   # Stores selected background image path
preview_image = None         # Stores preview image object for display


# LANGUAGE MAPPINGS 
months = {
    "English": ["January","February","March","April","May","June","July","August","September","October","November","December"],
    "French": ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"],
    "Spanish": ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    "German": ["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]
}

weekdays = {
    "English": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "French": ["Lun","Mar","Mer","Jeu","Ven","Sam","Dim"],
    "Spanish": ["Lun","Mar","Mié","Jue","Vie","Sáb","Dom"],
    "German": ["Mo","Di","Mi","Do","Fr","Sa","So"]
}

igbo_days = ["Eke", "Orie", "Afo", "Nkwo"]


# MAIN CALENDAR GENERATION
def generate_calendar(year, language, save_folder, save_pdf=False):
    year = int(year)  # Convert input year to integer
    cal = calendar.Calendar(firstweekday=0)   # Creates calendar starting on Monday

    pdf_pages = []  # Stores pages for PDF

    for month in range(1, 13):   # Loop through all 12 months

        # Load background image for page 
        if selected_background and os.path.exists(selected_background):  # If the user selected a background image AND the file actually exists
            bg = Image.open(selected_background).resize((1200, 900))     # Open the chosen background image and resize it to fit the calendar dimensions
            img = bg.copy()      
        else:
            img = Image.new("RGB", (1200, 900), "#9FBADB")   # If no valid background image is selected, create a solid-color background instead


        draw = ImageDraw.Draw(img)  # Create a drawing object that allows us to write text and draw shapes on the image

        # Fonts
        # Load the font styles chosen by user
        title_font = ImageFont.truetype(selected_font, selected_size + 30)
        text_font = ImageFont.truetype(selected_font, selected_size)
        small_font = ImageFont.truetype(selected_font, selected_size - 8)

        # Month name
        month_name = months[language][month - 1]  # Get month name in chosen language
        draw.text((350, 30), f"{month_name} {year}", fill="black", font=title_font)  # Draw the month title at top center

        # Weekday names
        for i, day in enumerate(weekdays[language]):   # Draw weekday names row
            draw.text((80 + i * 150, 150), day, fill="blue", font=text_font)

        # Month days matrix
        month_days = cal.monthdayscalendar(year, month)  # Get matrix of days for the month (weeks containing numbers)
        start_market_index = 0   # Track Igbo market cycle
        y_position = 250  # Starting vertical position for days

        # Loop through each week in the month
        for week in month_days:
            for i, day in enumerate(week):
                if day != 0:  # Skip empty spots (days belonging to previous/next month)
                    draw.text((80 + i * 150, y), str(day), fill="black", font=text_font)   # Draw the day number  
                    # Draw corresponding Igbo market day       
                    market_day = igbo_days[start_market_index % 4]
                    draw.text((80 + i * 150, y_position + 45), market_day, fill="green", font=small_font)
                    start_market_index += 1   # Move to next Igbo day
            y_position += 120  # Move down to next week row



        # Save PNG
        file_path = os.path.join(save_folder, f"{year}_{month_name}.png")  # Create the full file path where the PNG image for the current month will be saved
        img.save(file_path)  # Save the generated calendar image as a PNG file in the selected folder


        # Store for PDF
        pdf_pages.append(img.convert("RGB")) # Convert image to RGB mode (required for PDF output), then store the image inside the list of pages that will later be combined into a single PDF

    if save_pdf:
        pdf_output = os.path.join(save_folder, f"{year}_Calendar.pdf")     # Create a file path for the multi-page PDF calendar
        pdf_pages[0].save(pdf_output, save_all=True, append_images=pdf_pages[1:])  # Save the first image as the PDF file, and append all other months as additional pages
        messagebox.showinfo("PDF Created", f"PDF saved successfully:\n{pdf_output}")    
    else:
        messagebox.showinfo("Success", "Calendar PNG files generated successfully!")    



# PREVIEW FUNCTION 
def preview_calendar():
    global preview_image # Declare preview_image as global so it doesn't get garbage-collected, this ensures the preview displays correctly in Tkinter.

    # Get the year and language selected by the user from the GUI
    year = year_entry.get()
    language = language_var.get()  

    cal = calendar.Calendar()  


    if selected_background:
        bg = Image.open(selected_background).resize((600, 450))    # Open the selected background image and resize it for the preview size

        img = bg.copy()  # Work on a copy so the original image remains unchanged

    else:
        img = Image.new("RGB", (600, 450), "#9FBADB")  # If no background is selected, create a plain colored background for preview


    draw = ImageDraw.Draw(img)  

    title_font = ImageFont.truetype(selected_font, selected_size)   # Load the selected font style and size for the month title
    text_font = ImageFont.truetype(selected_font, selected_size - 10)  # Load a slightly smaller font for the day numbers


    month_name = months[language][0]   # Get the translated name for January based on the selected language
    draw.text((180, 10), f"{month_name} {year}", fill="black", font=title_font)  # Draw the month title at the top of the preview


    month_days = cal.monthdayscalendar(int(year), 1)   # Get a matrix of weeks and days for January (1)


    y = 80            # Starting vertical position for the calendar grid
    x_start = 40      # Starting horizontal offset

    # Loop through each row (week) in the month
    for row in month_days:
        x = x_start
        for d in row:
            if d != 0:
                draw.text((x, y), str(d), fill="black", font=text_font) # Draw day numbers only for valid days (0 means empty slot)
            x += 70
        y += 60

    # Convert to Tkinter image
    preview_image = ImageTk.PhotoImage(img)

    # Show window
    w = tk.Toplevel(root)
    w.title("Preview Calendar")
    w.geometry("620x500")

    tk.Label(w, text="Preview", font=("Arial", 16)).pack(pady=10)
    tk.Label(w, image=preview_image).pack()


#FILE HANDLING 
def choose_background():
    global selected_background
    selected_background = filedialog.askopenfilename(
        title="Choose Background Image",
        filetypes=[("Images", "*.jpg *.png *.jpeg")]
    )
    if selected_background:
        bg_label.config(text=os.path.basename(selected_background))


def validate_inputs(*args):
    if year_entry.get().isdigit() and len(year_entry.get()) == 4 and language_var.get() != "":
        png_btn["state"] = "normal"
        pdf_btn["state"] = "normal"
    else:
        png_btn["state"] = "disabled"
        pdf_btn["state"] = "disabled"


def start_generate(pdf=False):
    folder = filedialog.askdirectory(title="Select Folder")
    if folder:
        generate_calendar(year_entry.get(), language_var.get(), folder, save_pdf=pdf)
    else:
        messagebox.showwarning("Cancelled", "No folder selected")


# GUI SETUP 
root = tk.Tk()
root.title("Multilingual Calendar Generator")
root.geometry("700x650")
root.configure(bg="#7ea0c6")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Background image 
bg_image_path = "C:/Users/DELL/Desktop/docs/image-378.jpg"
if os.path.exists(bg_image_path):
    bg_image = Image.open(bg_image_path)     # Load background image
    bg_photo = ImageTk.PhotoImage(bg_image)  # Convert for tkinter
    background_label = tk.Label(root, image=bg_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill full windo

title = tk.Label(root, text="Base Bangers Calendar Generator", font=("Arial", 22, "bold"), bg="#7ea0c6")
title.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")


# Language Selection
language_var = tk.StringVar()
language_label = tk.Label(root, text="Select Language:", font=("Arial", 14), bg="#528e4f")
language_label.grid(row=1, column=0, pady=10, sticky="e")

language_menu = ttk.Combobox(root, textvariable=language_var, values=list(months.keys()), state="readonly")
language_menu.grid(row=1, column=1, pady=10, sticky="w")
language_menu.bind("<<ComboboxSelected>>", validate_inputs)

# Year Entry
year_label = tk.Label(root, text="Enter Year:", font=("Arial", 14), bg="#a1c56d")
year_label.grid(row=2, column=0, pady=10, sticky="e")
year_entry = tk.Entry(root, width=10, font=("Arial", 14))
year_entry.grid(row=2, column=1, pady=10, sticky="w")
year_entry.bind("<KeyRelease>", validate_inputs)

# Choose Background Button
bg_label = tk.Label(root, text="Background Image:", font=("Arial", 14), bg="#7ea0c6")
bg_label.grid(row=3, column=0, pady=10, sticky="e")
bg_btn = tk.Button(root, text="Choose Background", command=choose_background)
bg_btn.grid(row=3, column=1, pady=10, sticky="w")

# Font Type Dropdown
fonts_folder = "C:/Windows/Fonts"
font_files = [f for f in os.listdir(fonts_folder) if f.endswith(".ttf")]

font_var = tk.StringVar(value="arial.ttf")
font_label = tk.Label(root, text="Font Type:", bg="#c6aa7e", font=("Arial", 14))
font_label.grid(row=4, column=0, pady=10, sticky="e")

font_combo = ttk.Combobox(root, textvariable=font_var, values=font_files, state="readonly")
#font_combo.pack()
font_combo.grid(row=4, column=1, pady=10, sticky="w")

def update_font(*args):
    global selected_font
    selected_font = os.path.join(fonts_folder, font_var.get())
font_var.trace("w", update_font)


# Font size dropdown
size_var = tk.IntVar(value=40)
size_label = tk.Label(root, text="Font Size:", bg="#7ea0c6", font=("Arial", 14))
size_label.grid(row=5, column=0, pady=10, sticky="e")
size_combo = ttk.Combobox(root, textvariable=size_var, values=list(range(10, 101, 2)), state="readonly")
size_combo.grid(row=5, column=1, pady=10, sticky="w")
                    

def update_size(*args):
    global selected_size
    selected_size = size_var.get()
size_var.trace("w", update_size)


# Preview Button
preview_btn = tk.Button(root, text="Preview Calendar", font=("Arial", 14), bg="#005bbb", fg="white", command=preview_calendar)\
    .grid(row=6, column=0, pady=10, columnspan=2, sticky="ew")

# Generate PNG button
png_btn = tk.Button(root, text="Generate PNG Calendar", font=("Arial", 16),
                         bg="green", fg="white", state="disabled",
                         command=lambda: start_generate(pdf=False))
png_btn.grid(row=7, column=0, pady=10, columnspan=2, sticky="ew")

# Generate PDF button
pdf_btn = tk.Button(root, text="Generate PDF Calendar", font=("Arial", 16),
                    bg="purple", fg="white", state="disabled",
                    command=lambda: start_generate(pdf=True))
pdf_btn.grid(row=8, column=0, pady= 10, columnspan=2, sticky="ew")

root.mainloop()
