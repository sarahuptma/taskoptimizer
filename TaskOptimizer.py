import psutil
import subprocess
import os

class TaskOptimizer:
    def __init__(self):
        self.processes = []

    def fetch_current_tasks(self):
        """Fetches the currently running processes."""
        self.processes = [proc for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]
        print("Fetched current running tasks.")

    def identify_high_usage_tasks(self, cpu_threshold=10.0, memory_threshold=10.0):
        """
        Identifies tasks that exceed the given CPU and memory usage thresholds.
        """
        high_usage_tasks = [proc.info for proc in self.processes
                            if proc.info['cpu_percent'] > cpu_threshold or proc.info['memory_percent'] > memory_threshold]
        print(f"Identified high usage tasks: {high_usage_tasks}")
        return high_usage_tasks

    def optimize_task(self, task_info):
        """
        Attempts to optimize a task by reducing its priority.
        """
        try:
            process = psutil.Process(task_info['pid'])
            process.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
            print(f"Optimized task: {task_info}")
            return True
        except Exception as e:
            print(f"Failed to optimize task {task_info}: {e}")
            return False

    def optimize_system(self):
        """Optimizes the system by reducing priority of high usage tasks."""
        self.fetch_current_tasks()
        high_usage_tasks = self.identify_high_usage_tasks()

        for task_info in high_usage_tasks:
            self.optimize_task(task_info)

if __name__ == "__main__":
    optimizer = TaskOptimizer()
    optimizer.optimize_system()