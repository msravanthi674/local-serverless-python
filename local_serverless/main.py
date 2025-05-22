import os
from multiprocessing import Process
from triggers.http_trigger import start_http_server
from triggers.file_trigger import start_file_watcher

if __name__ == "__main__":
    # Create watched directory if it doesn't exist
    os.makedirs("watched_dir", exist_ok=True)

    print("[SYSTEM] Starting local serverless environment...")

    # Start HTTP and File triggers as separate processes
    http_process = Process(target=start_http_server)
    file_process = Process(target=start_file_watcher)

    http_process.start()
    file_process.start()

    http_process.join()
    file_process.join()
