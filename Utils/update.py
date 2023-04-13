from contextlib import contextmanager
import logging
import time
import sys
import os


from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(filename='Logs/UpdateLog.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@contextmanager
def observe_file_changes(log_file_path):
    event_handler = FileModifiedHandler(log_file_path)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        yield
        while True:
            time.sleep(1)
            if event_handler.is_log_file_modified():
                logging.info(f"Detected modification in log file {log_file_path}. Ignoring...")
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# Restarting Bot on code update
class FileModifiedHandler(FileSystemEventHandler):
    def __init__(self, log_file_path):
        super().__init__()
        self.log_file_path = log_file_path
        self.log_file_modified_at = os.stat(log_file_path).st_mtime

    def on_modified(self, event):
        if event.src_path == self.log_file_path:
            # If the log file was modified, update the last modified time
            self.log_file_modified_at = os.stat(self.log_file_path).st_mtime
            logging.info(f"Detected modification in log file {event.src_path}. Ignoring...")
        else:
            logging.info(f"Detected modification in {event.src_path}. Restarting bot...")
            time.sleep(1)
            try:
                os.execv(sys.executable, ['python'] + sys.argv)
            except Exception as e:
                logging.error(f"Error occurred while restarting bot: {e}")