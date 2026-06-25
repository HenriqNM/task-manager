class TaskManager:
    def __init__(self) -> None:
        self.storage: dict = {}
        self.task_id_counter: int = 1

    def create_list_task(self, list_name: str) -> None:
        if list_name not in self.storage:
            self.storage[list_name] = {}

    def add_task(self, list_name: str, title_task: str, note_task: str) -> bool:
        if list_name not in self.storage:
            return False
        new_task = {
            "id": self.task_id_counter,
            "title": title_task,
            "notes": note_task,
            "completed": False
        }
        self.storage[list_name][self.task_id_counter] = new_task
        self.task_id_counter += 1
        return True

    def get_tasks(self, list_name: str) -> list | None:
        if list_name in self.storage:
            return list(self.storage[list_name].values())
        return None

    def complete_task(self, list_name: str, task_id: int) -> bool:
        if list_name not in self.storage:
            return False

        if task_id not in self.storage[list_name]:
            return False

        self.storage[list_name][task_id]["completed"] = True
        return True

    def delete_task(self, list_name: str, task_id: str) -> bool:
        if list_name not in self.storage:
            return False
        if task_id not in self.storage[list_name]:
            return False

        del self.storage[list_name][task_id]
        return True

    def delete_list(self, list_name: str) -> bool:
        if list_name not in self.storage:
            return False
        del self.storage[list_name]
        return True