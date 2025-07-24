# Class-based Context Manager
class CustomLogger:
    def __enter__(self):
        print("Start Logging...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End Logging.")

# Usage
with CustomLogger():
    print("Inside the logging block")