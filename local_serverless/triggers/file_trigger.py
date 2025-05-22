from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dispatcher import dispatch_event

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".txt"):
            dispatch_event("file_logger", {"file": event.src_path})

def start_file_watcher(path="watched_dir/"):
    observer = Observer()
    observer.schedule(Watcher(), path=path, recursive=False)
    observer.start()
