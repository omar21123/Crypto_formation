# bruteforce_pq_mt_clean.py
import math
from concurrent.futures import ThreadPoolExecutor, as_completed

n = 130033          # modulus
NUM_THREADS = 2     # number of threads
limit = int(math.isqrt(n)) + 1


def factor_range(start, end):
    """Tests a range to find a factor."""
    for p in range(start, end):
        if n % p == 0:
            return p, n // p
    return None


def try_once():
    """Runs a single brute-force attempt."""
    chunk_size = limit // NUM_THREADS
    ranges = [(i * chunk_size + 2, (i + 1) * chunk_size + 2) for i in range(NUM_THREADS)]

    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(factor_range, r[0], r[1]) for r in ranges]

        for future in as_completed(futures):
            result = future.result()
            if result:
                return result

    return None


print("[*] Starting brute-force... Press CTRL+C to stop.")

try:
    while True:
        result = try_once()
        if result:
            p, q = result
            print("\n[+] Factors found!")
            print("p =", p)
            print("q =", q)
            break

except KeyboardInterrupt:
    print("\n[!] Stopped by user.")
