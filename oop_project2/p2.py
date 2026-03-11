class Task:
    def __init__(self, title, category, deadline, priority):
        self.title = title
        self.category = category
        self.deadline = deadline
        self.priority = priority


class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, category, deadline, priority):
        t = Task(title, category, deadline, priority)
        self.tasks.append(t)
        print("Task Added")

    def show_all(self):
        for t in self.tasks:
            print(t.title, t.category, t.deadline, t.priority)

    def filter_category(self, category):
        for t in self.tasks:
            if t.category == category:
                print(t.title, t.deadline, t.priority)

    def filter_priority(self, priority):
        for t in self.tasks:
            if t.priority == priority:
                print(t.title, t.category, t.deadline)


m = TodoManager()

m.add_task("Build API", "Project", "10 March", "High")
m.add_task("Buy Milk", "Personal", "9 March", "Low")
m.add_task("Study Python", "Learning", "12 March", "High")

print("All Tasks")
m.show_all()

print("Project Tasks")
m.filter_category("Project")

print("High Priority Tasks")
m.filter_priority("High")