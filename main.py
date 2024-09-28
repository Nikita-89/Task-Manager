class Task():
    def __init__(self, info, dead_line, status = " "):
        self.info = info
        self.dead_line = dead_line
        self.status = status

    def check_status(self, today_date):
        if self.dead_line > today_date:
            self.status = "просрочено"
        else:
            self.status = "в процессе"

    def __repr__(self):
        return f"{self.info} (Срок: {self.dead_line}, Статус: {self.status})"

class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, info, dead_line):
        task = Task(info, dead_line)
        self.task_list.append(task)
        print(f"Добавлена задача - {info}, {dead_line}")

    def task_statuses(self, today_date):
        for task in self.task_list:
            task.check_status(today_date)

    def get_current_list(self):
        print("Текущие задачи:")
        for index, task in enumerate(self.task_list):
            print(f"{index + 1}. {task}")

today_date = 20
today_month = "сентябрь"
manager = TaskManager()
manager.add_task("Лечь спать вовремя", 19)
manager.add_task("Помыть машину", 22)
manager.add_task("Купить продукты", 30)
manager.task_statuses(today_date)
manager.get_current_list()
