
#Exercise 1: Threaded Prime Number Checker
import threading

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, primes):
    """Check primes in a range and append them to the shared list primes."""
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)

def main():
    start_range = 1
    end_range = 100
    num_threads = 4

    threads = []
    primes = []

    # Calculate the size of each chunk
    chunk_size = (end_range - start_range) // num_threads

    for i in range(num_threads):
        # Define the start and end for each thread's chunk
        chunk_start = start_range + i * chunk_size
        # Last chunk goes to the end_range
        chunk_end = start_range + (i + 1) * chunk_size if i != num_threads - 1 else end_range

        # Create and start thread
        thread = threading.Thread(target=check_primes, args=(chunk_start, chunk_end, primes))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    primes.sort()
    print("Prime numbers found:", primes)

if __name__ == "__main__":
    main()


#Exercise 2: Threaded File Processing

import threading
from collections import Counter

def count_words(lines, word_counts):
    """Count words in the list of lines and update the shared Counter."""
    local_count = Counter()
    for line in lines:
        words = line.strip().split()
        local_count.update(words)
    # Update the shared dictionary (thread-safe using a lock)
    with lock:
        word_counts.update(local_count)

def main():
    filename = "large_text.txt"
    num_threads = 4

    with open(filename, 'r') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    word_counts = Counter()

    for i in range(num_threads):
        chunk_start = i * chunk_size
        chunk_end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread_lines = lines[chunk_start:chunk_end]
        thread = threading.Thread(target=count_words, args=(thread_lines, word_counts))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Word counts across all threads:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    lock = threading.Lock()  # lock for thread-safe update
    main()

