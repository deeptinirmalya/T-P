class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class ExamSystem:
    def __init__(self):
        self.quizzes = []
        self.scores = {}

    def add_quiz(self, question, answer):
        q = Quiz(question, answer)
        self.quizzes.append(q)

    def take_exam(self, student):
        score = 0
        for q in self.quizzes:
            ans = input(q.question + " ")
            if ans.lower() == q.answer.lower():
                score += 1
        self.scores[student] = score
        print("Score:", score)

    def show_results(self):
        for student in self.scores:
            print(student, self.scores[student])


e = ExamSystem()

e.add_quiz("Capital of India?", "Delhi")
e.add_quiz("5 + 3 ?", "8")
e.add_quiz("Python is a language? yes/no", "yes")

name = input("Enter student name: ")

e.take_exam(name)

print("Result Report")
e.show_results()