import sys
import os

def extract_logs(log_file_path, target_date, output_dir="output"):
    """
    Extracts log entries for a specific date from a log file.

    Args:
        log_file_path (str): Path to the log file.
        target_date (str): Date to extract logs for (YYYY-MM-DD).
        output_dir (str, optional): Directory to save the output. Defaults to "output".
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
            for line in log_file:
                if line.startswith(target_date):
                    output_file.write(line)

    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if _name_ == "_main_":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    target_date = sys.argv[1]

    logs_folder = "logs_2024"  # Folder name
    log_file_name = "logs_2024.txt"  # File name
    log_file_path = os.path.join(logs_folder, log_file_name) # full path to file.

    if not os.path.exists(logs_folder):
        print(f"Error: Folder '{logs_folder}' not found.")
        sys.exit(1)

    if not os.path.exists(log_file_path):
        print(f"Error: Log file not found at {log_file_path}")
        sys.exit(1)

    extract_logs(log_file_path, target_date)

    print(f"Logs for {target_date} extracted to output/output_{target_date}.txt")