# cpu_stress.py
import multiprocessing
import time
import signal
import sys

def load():
    # busy loop — burns CPU
    while True:
        pass

def start_load(seconds=120):
    procs = []
    try:
        for _ in range(multiprocessing.cpu_count()):
            p = multiprocessing.Process(target=load)
            p.start()
            procs.append(p)
        print(f"⚡ CPU load started on {len(procs)} processes for {seconds} seconds.")
        time.sleep(seconds)
    finally:
        for p in procs:
            try:
                p.terminate()
                p.join(timeout=1)
            except Exception:
                pass
        print("✅ CPU load finished / cleaned up.")

if __name__ == "__main__":
    # On Windows, freeze_support is sometimes needed for frozen executables.
    try:
        from multiprocessing import freeze_support
        freeze_support()
    except Exception:
        pass

    # Allow user to pass runtime seconds as first arg (optional)
    secs = 120
    if len(sys.argv) > 1:
        try:
            secs = int(sys.argv[1])
        except ValueError:
            pass

    start_load(seconds=secs)
