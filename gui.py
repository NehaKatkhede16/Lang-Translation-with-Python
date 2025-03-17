import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LanguageTranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("600x300")
        self.root.configure(bg="#f0f8ff")

        # Title label
        self.title_label = tk.Label(
            self.root,
            text="Language Translator",
            font=("Helvetica", 18, "bold"),
            bg="#4682b4",
            fg="white",
            pady=10,
        )
        self.title_label.pack(fill=tk.X)

        # Input frame
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(pady=20)

        self.input_label = tk.Label(
            self.input_frame, text="Enter text:", font=("Arial", 12), bg="#f0f8ff"
        )
        self.input_label.grid(row=0, column=0, padx=10, pady=5)

        self.input_entry = ttk.Entry(self.input_frame, width=50, font=("Arial", 12))
        self.input_entry.grid(row=0, column=1, padx=10, pady=5)

        # Language selection
        self.language_label = tk.Label(
            self.input_frame, text="Language:", font=("Arial", 12), bg="#f0f8ff"
        )
        self.language_label.grid(row=1, column=0, padx=10, pady=5)

        self.language_combobox = ttk.Combobox(
            self.input_frame, 
            values=["French", "Spanish", "German", "Hindi", "Chinese"],
            state="readonly",
            font=("Arial", 12),
        )
        self.language_combobox.grid(row=1, column=1, padx=10, pady=5)
        self.language_combobox.set("Select Language")

        # Translate button
        self.translate_button = tk.Button(
            self.root,
            text="Translate",
            font=("Arial", 14),
            bg="#32cd32",
            fg="white",
            activebackground="#228b22",
            activeforeground="white",
            command=self.translate_text,
        )
        self.translate_button.pack(pady=10)

        # Output frame
        self.output_frame = ttk.Frame(self.root)
        self.output_frame.pack(pady=20)

        self.output_label = tk.Label(
            self.output_frame, text="Translated text:", font=("Arial", 12), bg="#f0f8ff"
        )
        self.output_label.grid(row=0, column=0, padx=10, pady=5)

        self.output_text = tk.Text(
            self.output_frame, width=50, height=5, font=("Arial", 12), wrap=tk.WORD
        )
        self.output_text.grid(row=0, column=1, padx=10, pady=5)

    def translate_text(self):
        # Get input text and selected language
        input_text = self.input_entry.get()
        selected_language = self.language_combobox.get()

        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to translate!")
            return

        if selected_language == "Select Language":
            messagebox.showwarning("Warning", "Please select a language!")
            return

        # Simulated translation (replace this with your translation logic)
        translated_text = f"[Translated to {selected_language}]: {input_text}"

        # Display translated text
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, translated_text)

# Main function
def main():
    root = tk.Tk()
    gui = LanguageTranslatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
