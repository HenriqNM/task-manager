import unittest
from engine import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = TaskManager()

    def test_create_task(self) -> None:
        # Test creating a list of tasks
        self.manager.create_list_task("Work")
        self.assertIn("Work", self.manager.storage)

    def test_add_task(self) -> None:
        # Test adding task
        self.manager.create_list_task("Work")
        result = self.manager.add_task("Work", "Fix Bug", "High priority")

        self.assertTrue(result)
        tasks = self.manager.get_tasks("Work")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Fix Bug")

if __name__ == "__main__":
    unittest.main()