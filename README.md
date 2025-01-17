# TaskOptimizer

TaskOptimizer is a Python program designed to analyze and optimize currently running tasks on a Windows system to improve system efficiency. The program identifies tasks that consume high CPU and memory resources and attempts to optimize them by reducing their priority.

## Features

- Fetches currently running tasks and their resource usage.
- Identifies tasks exceeding specified CPU and memory usage thresholds.
- Reduces the priority of high usage tasks to improve overall system performance.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the `psutil` library if not already installed:

   ```bash
   pip install psutil
   ```

## Usage

Run the program using Python:

```bash
python TaskOptimizer.py
```

The program will automatically fetch the list of running tasks, identify high usage tasks, and attempt to optimize them by reducing their priority.

## Limitations

- The program currently only works on Windows operating systems.
- Reducing task priority might not always lead to a significant performance improvement, depending on the nature of the tasks and system workload.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Developed by [Your Name]