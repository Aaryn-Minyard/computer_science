import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import init, Fore, Style

# Initialize colorama for colorful console output
init(autoreset=True)

# Set up logging to a file
logging.basicConfig(
    level=logging.INFO,
    filename="tv_shows.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_tv_shows(filename):
    """
    Reads the input file, builds a dictionary of TV shows by season count,
    sorts by keys and by show names, and writes the results to output files.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        logging.error(f"Error reading file {filename}: {e}")
        print(Fore.RED + f"Error reading file {filename}: {e}")
        return

    tv_shows = {}
    try:
        for i in range(0, len(lines), 2):
            seasons = int(lines[i].strip())
            show = lines[i + 1].strip()
            tv_shows.setdefault(seasons, []).append(show)
    except Exception as e:
        logging.error(f"Error processing file {filename}: {e}")
        print(Fore.RED + f"Error processing file {filename}: {e}")
        return

    # Write sorted dictionary by key (greatest to least) to output_keys.txt
    try:
        with open("output_keys.txt", 'w') as file:
            for seasons in sorted(tv_shows.keys(), reverse=True):
                file.write(f"{seasons}: {'; '.join(tv_shows[seasons])}\n")
    except Exception as e:
        logging.error(f"Error writing output_keys.txt: {e}")
        print(Fore.RED + f"Error writing output_keys.txt: {e}")

    # Write sorted TV shows (reverse alphabetical order) to output_titles.txt
    try:
        all_shows = [show for shows in tv_shows.values() for show in shows]
        sorted_shows = sorted(all_shows, reverse=True)
        with open("output_titles.txt", 'w') as file:
            for show in sorted_shows:
                file.write(f"{show}\n")
    except Exception as e:
        logging.error(f"Error writing output_titles.txt: {e}")
        print(Fore.RED + f"Error writing output_titles.txt: {e}")

    print(Fore.GREEN + f"Successfully processed '{filename}' and updated output files.")
    logging.info(f"Successfully processed '{filename}'.")

class FileChangeHandler(FileSystemEventHandler):
    """
    Watches for modifications in the specified file and reprocesses it.
    """
    def __init__(self, filename):
        self.filename = os.path.abspath(filename)
        super().__init__()

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == self.filename:
            print(Fore.YELLOW + f"Detected changes in '{self.filename}'. Reprocessing...")
            process_tv_shows(self.filename)

def monitor_file(filename):
    """
    Monitors the given file for changes and reprocesses it upon modification.
    """
    event_handler = FileChangeHandler(filename)
    observer = Observer()
    # Monitor the directory containing the file
    path = os.path.dirname(os.path.abspath(filename)) or "."
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    print(Fore.CYAN + f"Monitoring '{filename}' for changes. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print(Fore.CYAN + "Stopped monitoring.")
    observer.join()

if __name__ == "__main__":
    input_file = input("Enter the name of the input file: ").strip()
    process_tv_shows(input_file)
    # Start real-time monitoring of the input file
    monitor_file(input_file)
