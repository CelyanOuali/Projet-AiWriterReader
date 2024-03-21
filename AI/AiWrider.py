import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random

class AIStoryStream:
    def __init__(self, root):
        self.root = root
        root.title("AI StoryStream")
        self.questions = [
            "How many heroes do you want in your story? (Max 4)",
            "What are the names of the heroes?",
            "What theme would you like for your story?",
            "What era should your story be set in?",
            "Do you want an anti-hero in your story?",
            "What is the name of the anti-hero?",
            "Can they use magic?",
            "Are they advanced in science?",
            "Do they explore the stars?",
            "Do they explore the seas?",
            "How many side characters do you want in your story? (Max 10)",
            "What is the name of the continent?",
            "What type of leader (Dirigeant) is there? (Monarchy, Democracy, Anarchy, Dictatorship, Managed Democracy)"
        ]
        self.answers = [""] * len(self.questions)
        self.create_widgets()
        self.setup_gpt2()

    def create_widgets(self):
        # GUI setup
        self.questions_frame = tk.Frame(self.root)
        self.questions_frame.pack(pady=10)

        self.story_input = scrolledtext.ScrolledText(self.root, width=60, height=10)
        self.story_input.pack(pady=5)

        ttk.Button(self.root, text="Generate User Prompt Story", command=self.generate_user_prompt).pack(pady=5)
        ttk.Button(self.root, text="Generate Random Prompt Story", command=self.generate_random_prompt).pack(pady=5)
        ttk.Button(self.root, text="Save Story", command=self.save_story).pack(pady=5)

        self.story_output = scrolledtext.ScrolledText(self.root, width=60, height=20)
        self.story_output.pack(pady=5)

        self.create_questions()

    def setup_gpt2(self):

        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def create_questions(self):

        self.question_widgets = []
        for i, question in enumerate(self.questions):
            label = ttk.Label(self.questions_frame, text=question)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            var = tk.StringVar()
            var.set("")
            if i == 0 or i == 10:
                menu = ttk.Combobox(self.questions_frame, textvariable=var, values=[""] + [str(num) for num in range(1, 5)])
                menu.grid(row=i, column=1, padx=5, pady=5)
                self.question_widgets.append(var)
            elif i == 1 or i == 5 or i == 11:
                entry = ttk.Entry(self.questions_frame, textvariable=var)
                entry.grid(row=i, column=1, padx=5, pady=5)
                self.question_widgets.append(var)
            elif i == 2:
                menu = ttk.Combobox(self.questions_frame, textvariable=var, values=["", "Fantasy", "Science Fiction", "Mystery", "Adventure"])
                menu.grid(row=i, column=1, padx=5, pady=5)
                self.question_widgets.append(var)
            elif i == 3:
                menu = ttk.Combobox(self.questions_frame, textvariable=var, values=["", "Past", "Present", "Future", "Urban", "Prehistoric", "Medieval"])
                menu.grid(row=i, column=1, padx=5, pady=5)
                self.question_widgets.append(var)
            elif i == 4:
                menu = ttk.Combobox(self.questions_frame, textvariable=var, values=["", "Yes", "No"])
                menu.grid(row=i, column=1, padx=5, pady=5)
                self.question_widgets.append(var)
            elif i == 6 or i == 7 or i == 8 or i == 9:
                menu = ttk.Combobox(self.questions_frame, textvariable=var, values=["", "Yes", "No"])
                menu.grid(row=i, column=1, padx=5, pady=5)
                self.question_widgets.append(var)
            elif i == 12:
                menu = ttk.Combobox(self.questions_frame, textvariable=var, values=["", "Monarchy", "Democracy", "Anarchy", "Dictatorship", "Managed Democracy"])
                menu.grid(row=i, column=1, padx=5, pady=5)
                self.question_widgets.append(var)


    def generate_user_prompt(self):
        for i, var in enumerate(self.question_widgets):
            self.answers[i] = var.get()

        try:
            prompt = self.construct_prompt()
            generated_story = self.generate_story_from_prompt(prompt)
            self.display_story(generated_story)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate story: {str(e)}")

    def construct_prompt(self):
        prompt = ""
        for i, question in enumerate(self.questions):
            answer = self.answers[i]
            if i == 1:
                if answer:
                    prompt += f"They were {len(answer.split(', '))} heroes, named {answer}, "
            elif i == 2:
                if answer:
                    prompt += f"with a theme of {answer.lower()}, "
            elif i == 3:
                if answer:
                    prompt += f"set in the {answer.lower()} era, "
            elif i == 4:
                if answer == "Yes":
                    prompt += f"and there was an anti-hero named {self.answers[i + 1]}, "
            elif i == 12:
                if answer:
                    prompt += f"with a {answer.lower()} type of leader, "
            else:
                if answer == "Yes":
                    prompt += f"they {question.lower()}, "

        return prompt.strip() + "\n"

    def generate_story_from_prompt(self, prompt):
        try:
            input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
            response = self.model.generate(input_ids, max_length=1000, do_sample=True)
            generated_story = self.tokenizer.decode(response[0], skip_special_tokens=True)
            return generated_story

        except Exception as e:
            raise RuntimeError(f"Failed to generate story: {str(e)}")

    def generate_random_prompt(self):
        prompt = random.choice([
            "Once upon a time, in a land far, far away...",
            "In a galaxy not so far away, there was...",
            "Legend has it that in a distant kingdom...",
            "Once upon a midnight dreary, while I pondered, weak and weary..."
        ])
        generated_story = self.generate_story_from_prompt(prompt)
        self.display_story(generated_story)

    def display_story(self, story):
        self.story_output.delete(1.0, tk.END)
        self.story_output.insert(tk.END, story)

    def save_story(self):
        story = self.story_output.get(1.0, tk.END)
        try:
            filename = "Stories.txt"
            with open(filename, "a") as file:
                file.write(story + "\n\n")
            messagebox.showinfo("Save Successful", "Story has been saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save story: {str(e)}")


if __name__ == '__main__':
    root = tk.Tk()
    app = AIStoryStream(root)
    root.mainloop()
