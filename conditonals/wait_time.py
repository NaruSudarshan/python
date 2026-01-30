import time

max_retries = 5
wait_time = 1
attempts = 0

while attempts < max_retries:
    success = False  # Simulate a condition check
    if success:
        print("Operation succeeded")
        break
    else:
        print(f"Attempt {attempts + 1} failed. Retrying in {wait_time} seconds...")
        time.sleep(wait_time)
        wait_time *= 2  # Exponential backoff
        attempts += 1