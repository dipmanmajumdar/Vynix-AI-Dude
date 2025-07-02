import tkinter as tk
from tkinter import ttk
import google.generativeai as genai
import time
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from PIL import Image, ImageTk

# Initialize the Gemini client with API key
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

# Global variable to control typing animation and store images
typing = False
images = []  # To prevent garbage collection of PhotoImage objects

# Function to convert LaTeX to image
def latex_to_image(latex_str):
    fig = plt.Figure(figsize=(4, 0.25), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.text(0.5, 0.5, f'${latex_str}$', size=12, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.9, pad=1))
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.02)
    buf.seek(0)
    img = Image.open(buf)
    photo = ImageTk.PhotoImage(img)
    images.append(photo)  # Store to prevent garbage collection
    return photo

# Function to send message and handle response
def send_message():
    global typing
    message = input_box.get().strip()
    if message:
        # Animate user message appearance on the right without extra newline
        chat_log.insert(tk.END, "You: " + message, "user")
        chat_log.see(tk.END)
        input_box.delete(0, tk.END)
        
        # Start bot response with typing animation on the left
        typing = True
        chat_log.insert(tk.END, "\nVynix: ", "bot")
        chat_log.see(tk.END)
        window.update()
        try:
            # Check if message is math-related and request multiple formatted questions
            math_keywords = ['solve', 'derivative', 'integral', 'equation', 'math', 'calculate', 'questions', 'problem']
            use_latex = any(keyword in message.lower() for keyword in math_keywords)
            prompt = message + (" Please generate 3-5 distinct math problems with solutions, each labeled as '\\textbf{Problem X}' where X is the number, and format all mathematical expressions in LaTeX using '$...$' delimiters. Provide the response in a clear, step-by-step manner similar to a textbook." if use_latex else "")
            response = model.generate_content(prompt)
            
            # Typing effect with LaTeX handling
            response_text = response.text
            if use_latex:
                import re
                # Split response into text and LaTeX parts
                parts = re.split(r'(\$[^$]+\$)', response_text)
                for part in parts:
                    if part and '$' in part:  # LaTeX portion
                        latex_str = part.strip('$')
                        img = latex_to_image(latex_str)
                        chat_log.image_create(tk.END, image=img)
                        chat_log.insert(tk.END, " ")  # Small space after image
                    elif part:  # Plain text
                        chat_log.insert(tk.END, part, "bot")  # Insert whole text chunk at once
                        chat_log.see(tk.END)
                        window.update()
                        time.sleep(0.01)  # Faster typing
            else:
                for char in response_text:
                    if not typing:
                        break
                    chat_log.insert(tk.END, char, "bot")
                    chat_log.see(tk.END)
                    window.update()
                    time.sleep(0.01)
            chat_log.insert(tk.END, "\n")  # Single newline at the end
            window.update_idletasks()  # Ensure all updates are processed
        except Exception as e:
            chat_log.insert(tk.END, f"\nError: {str(e)}\n", "error")
        chat_log.see(tk.END)
        typing = False

# Function to stop typing animation
def stop_typing():
    global typing
    typing = False
    chat_log.insert(tk.END, "\n", "bot")
    chat_log.see(tk.END)

# Bind hover effects for Send button
def send_enter(e):
    send_button.config(bg="#4CAF50", fg="white")

def send_leave(e):
    send_button.config(bg="#333333", fg="#cccccc")

# Bind hover effects for Stop button
def stop_enter(e):
    stop_button.config(bg="#e53935", fg="white")

def stop_leave(e):
    stop_button.config(bg="#333333", fg="#cccccc")

# Function to create a welcome animation
def welcome_animation():
    global typing
    typing = True
    welcome_text = "Hi Dude! How can I assist you today?\n"
    chat_log.insert(tk.END, "Vynix: ", "bot")
    for i, char in enumerate(welcome_text):
        if not typing:
            break
        chat_log.insert(tk.END, char, "bot")
        chat_log.see(tk.END)
        window.update()
        time.sleep(0.05)
    chat_log.insert(tk.END, "\n")
    typing = False

# GUI setup
window = tk.Tk()
window.title("Vynix: Your AI Dude")
window.geometry("600x700")
window.configure(bg="#121212")  # Dark black background

# Heading
heading_label = tk.Label(window, text="Vynix: Your AI Dude", font=("Times New Roman", 24, "bold"), 
                        fg="#a5d6a7", bg="#121212")
heading_label.pack(pady=10)

# Configure chat log
chat_log = tk.Text(window, height=25, width=60, bg="#252526", fg="#cccccc", 
                  font=("Times New Roman", 14), wrap=tk.WORD, borderwidth=2, relief="flat")
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Define tags for styling and alignment
chat_log.tag_configure("user", foreground="#90caf9", font=("Times New Roman", 14, "bold"), justify="right", lmargin1=200, rmargin=10)
chat_log.tag_configure("bot", foreground="#ffffff", font=("Times New Roman", 14), justify="left", lmargin1=10, rmargin=200)
chat_log.tag_configure("error", foreground="#ef5350", font=("Times New Roman", 14, "italic"), justify="center")

# Input frame
input_frame = tk.Frame(window, bg="#121212")
input_frame.pack(pady=5)

# Input box with rounded corners
style = ttk.Style()
style.configure("Rounded.TEntry", background="#333333", foreground="#cccccc", 
                fieldbackground="#333333", borderwidth=0, padding=5)
style.layout("Rounded.TEntry", [
    ("Entry.padding", {"sticky": "nswe", "children": [
        ("Entry.textarea", {"sticky": "nswe"})
    ]})
])
style.map("Rounded.TEntry", background=[("active", "#333333")])

input_box = ttk.Entry(input_frame, font=("Times New Roman", 14), width=40, style="Rounded.TEntry")
input_box.pack(side=tk.LEFT, padx=(0, 5))

# Send button
send_button = tk.Button(input_frame, text="Send", command=send_message, 
                       bg="#333333", fg="#cccccc", font=("Times New Roman", 12, "bold"),
                       borderwidth=0, relief="flat", activebackground="#4CAF50")
send_button.pack(side=tk.LEFT, padx=2)

# Stop button with stop logo
stop_button = tk.Button(input_frame, text="■", command=stop_typing, 
                       bg="#333333", fg="#cccccc", font=("Times New Roman", 12, "bold"),
                       borderwidth=0, relief="flat", activebackground="#e53935")
stop_button.pack(side=tk.LEFT, padx=2)

# Bind hover effects
send_button.bind("<Enter>", send_enter)
send_button.bind("<Leave>", send_leave)
stop_button.bind("<Enter>", stop_enter)
stop_button.bind("<Leave>", stop_leave)

# Input box key binding
input_box.bind("<Return>", lambda event: send_message())

# Footer
footer_label = tk.Label(window, text="Developed by Dee", font=("Times New Roman", 10, "italic"), 
                       fg="#666666", bg="#121212")
footer_label.pack(pady=5)

# Run welcome animation
window.after(500, welcome_animation)

# Start the main loop
window.mainloop()
