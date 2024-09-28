class Task():
    def __init__(self, info, dead_line, status):
        self.info = info
        self.dead_line = dead_line
        self.status = status


    def add_task (self, task):
        task_list.append(task)
        self.info = task
        print(f"Добавлена задача - {task}")

    def add_time (self, time):
        self.dead_line = time
        print(f"срок выполнения - {time}")

        if self.dead_line > today_date:
            self.status = "в процессе"
        else:
            self.status = "просрочено"
        print(f"Выполнение задачи: {self.status}")

    def out_list (self):




today_date = 20
today_month = "сентябрь"

task_list = []

task = Task ("Информация", "Срок", "Статус")

task.add_task("Лечь спать вовремя")
task.add_time(25)
