from ClassesObjectsExercise.project_todo.task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        #happy case
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = []
        for task in self.tasks:
            if task.completed:
                completed_tasks.append(task)

        #remove all task which are compleated_tasks list from tasks list
        if len(completed_tasks) > 0:
            for task in completed_tasks:
                self.tasks.remove(task)

        return f"Cleared {len(completed_tasks)} tasks."



    def view_section(self):
        message = f"Section {self.name}:\n"

        message += "\n".join([f"{task.details()}" for task in self.tasks])
        return message



task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())