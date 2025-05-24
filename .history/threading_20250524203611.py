import threading
import time

def partial_sum(start, end, result):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    result.append(sum)

def parallel_sum(num_threads, total_sum_range):
    start_time = time.time()
    results = []
    threads = []
    segment_size = total_sum_range // num_threads

    for i in range(num_threads):
        start = i * segment_size + 1
        end = (i + 1) * segment_size if i < num_threads - 1 else total_sum_range
        thread = threading.Thread(target=partial_sum, args=(start, end, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(results)
    end_time = time.time()
    duration = end_time - start_time

    return total_sum, duration

if __name__ == "__main__":
    num_threads = 
    total_sum_range = 1000000000

    total_sum, duration = parallel_sum(num_threads, total_sum_range)
    print(f"Total sum: {total_sum}")
    print(f"Time taken with {num_threads} threads: {duration:.4f} seconds")

    start_time = time.time()
    sequential_sum = sum(range(1, total_sum_range + 1))
    end_time = time.time()
    sequential_duration = end_time - start_time

    print(f"Sequential sum: {sequential_sum}")
    print(f"Time taken without threads: {sequential_duration:.4f} seconds")