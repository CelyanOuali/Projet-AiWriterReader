import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random

class AIStoryStream:
    def __init__(self, root):
        self.root = root
        root.title("AI StoryStream")
        self.create_widgets()
        self.setup_gpt2()
        self.story_count = 0  # Counter to track the number of generated stories

    def create_widgets(self):
        # GUI setup
        self.story_input = scrolledtext.ScrolledText(self.root, width=60, height=10)
        self.story_input.pack(pady=5)

        self.prompt_type_var = tk.IntVar()
        ttk.Radiobutton(self.root, text="Generate from Prompt", variable=self.prompt_type_var, value=1).pack()
        ttk.Radiobutton(self.root, text="Generate Random Story", variable=self.prompt_type_var, value=2).pack()

        ttk.Button(self.root, text="Generate Story", command=self.generate_story).pack(pady=5)
        ttk.Button(self.root, text="Save Story", command=self.save_story).pack(pady=5)

        self.story_output = scrolledtext.ScrolledText(self.root, width=60, height=20)
        self.story_output.pack(pady=5)

    def setup_gpt2(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def generate_story(self):
        # Generate a story based on user input or randomly

        if self.prompt_type_var.get() == 1:  # Generate from Prompt
            user_input = self.story_input.get(1.0, tk.END).strip()
            if not user_input:
                messagebox.showwarning("Warning", "Please provide some input.")
                return

            prompt = user_input
        elif self.prompt_type_var.get() == 2:  # Generate Random Story
            prompt = random.choice(["Once upon a time, in a land far, far away...",
                                    "In a galaxy not so far away, there was...",
                                    "Legend has it that in a distant kingdom...",
                                    "Once upon a midnight dreary, while I pondered, weak and weary..."])
        else:
            messagebox.showwarning("Warning", "Please select a prompt type.")
            return

        try:
            input_ids = self.tokenizer.encode(prompt, return_tensors="pt")

            # Generate story based on the provided prompt
            response = self.model.generate(input_ids, max_length=200, do_sample=True)
            generated_story = self.tokenizer.decode(response[0], skip_special_tokens=True)

            self.story_output.delete(1.0, tk.END)
            self.story_output.insert(tk.END, generated_story)

            self.generated_story = generated_story  # Store generated story for saving
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate story: {str(e)}")

        print("Generated Story:", self.generated_story)  # Debugging statement

    def save_story(self):
        # Save the generated story to Stories.txt with each story separated by "Story X"
        if hasattr(self, 'generated_story'):
            print("Saving Story:", self.generated_story)  # Debugging statement

            filename = "Stories.txt"
            with open(filename, 'a') as f:
                self.story_count += 1
                if self.story_count >= 1:
                    f.write(f"\n\nStory {self.story_count}\n")
                else:
                    f.write(f"Story {self.story_count}\n")
                f.write(self.generated_story)
            messagebox.showinfo("Success", "Story saved successfully.")
        else:
            messagebox.showwarning("Warning", "No story generated yet.")

if __name__ == '__main__':
    root = tk.Tk()
    app = AIStoryStream(root)
    root.mainloop()