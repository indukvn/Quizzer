from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Python Programming", width=200, font=("Arial", 16, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.lab = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.lab.grid(row=0, column=1)

        true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(row=2, column=1)
        self.get_nxt_ques()

        self.window.mainloop()

    def get_nxt_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lab.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text=f"You've reached the end of quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        self.give_response(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_response(self.quiz.check_answer("False"))

    def give_response(self, is_right):
        if is_right:
            self.canvas.config(bg="#C3FF99")
        else:
            self.canvas.config(bg="#F87474")
        self.window.after(1200, self.get_nxt_ques)
