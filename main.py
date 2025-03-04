import tkinter as tk
from tkinter import scrolledtext
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def send_message():
    user_text = entry.get()
    if user_text.strip():
        chat_box.insert(tk.END, "\nYou: " + user_text + "\n", "user")
        response = get_response(user_text)
        chat_box.insert(tk.END, "Bot: " + response + "\n", "bot")
        chat_box.yview(tk.END)  # Auto-scroll to latest message
        entry.delete(0, tk.END)
        root.after(500, lambda: speak(response))  # Speak after a short delay

def get_response(text):
    responses = {
        "hello": "Hello! Welcome to the AI College Predictor. How can I assist you today?",
        "admission": "You can check your admission chances by providing your academic scores, entrance exam results, and preferred colleges.",
        "scholarship": "We offer a Scholarship Finder tool to help you discover scholarships based on your academic performance, financial need, and other criteria.",
        "placement": "Our platform provides detailed insights into college placement records, top recruiters, and average salary packages.",
        "compare": "You can compare colleges side-by-side based on factors like fees, placements, infrastructure, and faculty.",
        "cutoff": "You can check the previous year's cutoff scores for various colleges and courses.",
        "eligibility": "Eligibility criteria vary by college and course. Please specify the name of the college and course you're interested in.",
        "courses": "We provide information on various courses offered by colleges.",
        "fees": "You can get detailed fee structures for different colleges and courses.",
        "rank": "You can check the ranking of colleges based on various parameters like academics, placements, and infrastructure.",
        "application": "The application process varies by college. Please specify the college you're interested in.",
        "deadline": "Application deadlines vary by college and course.",
        "thanks": "You're welcome! If you have more questions, feel free to ask.",
        "bye": "Goodbye! Have a great day, and good luck with your college search!"
    }
    return responses.get(text.lower(), "Sorry, I don't understand that.")

# Create GUI window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("420x550")
root.configure(bg="#001f3f")

# Chat Header
header = tk.Label(root, text="AI Chatbot", font=("Poppins", 18, "bold"), fg="white", bg="#004080", pady=10)
header.pack(fill=tk.X)

# Chat Display Area
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, bg="#000032", fg="#cce7ff", font=("Poppins", 12), borderwidth=0, highlightthickness=0)
chat_box.pack(pady=10, padx=10)
chat_box.tag_configure("user", foreground="#00aaff", font=("Poppins", 12, "bold"), justify="right")
chat_box.tag_configure("bot", foreground="#cce7ff", font=("Poppins", 12), justify="left")
chat_box.insert(tk.END, "Bot: Hello! How can I assist you?\n", "bot")

# Input Frame
input_frame = tk.Frame(root, bg="#000032")
input_frame.pack(fill=tk.X, padx=10, pady=5)

# Input Field
entry = tk.Entry(input_frame, width=35, font=("Poppins", 12), bg="#334466", fg="#cce7ff", insertbackground="white", relief="flat", justify="center")
entry.pack(side=tk.LEFT, padx=10, ipady=5, expand=True, fill=tk.X)

# Send Button
send_button = tk.Button(input_frame, text="Send", font=("Poppins", 12, "bold"), bg="#007bff", fg="white", relief="flat", padx=15, pady=5, command=send_message)
send_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
