# Timer Context Manager with @contextmanager
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield  # Pause here while the block runs
    end = time.time()
    print(f"⏱️ Time taken: {end - start:.2f} seconds")

# Usage
with timer():
    # Simulate some task
    time.sleep(2)