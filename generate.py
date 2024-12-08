import os
import shutil
from datetime import datetime

def main():
    # Get the current year
    current_year = datetime.now().year
    folder_path = f"{current_year}/solutions"

    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder for year {current_year} does not exist.")
        return

    # Get the list of day{n}.py files
    day_files = [f for f in os.listdir(folder_path) if f.startswith("day") and f.endswith(".py")]
    day_numbers = [int(f[3:-3]) for f in day_files]

    # Determine the next day number
    next_day_number = max(day_numbers, default=0) + 1
    new_file_name = f"day{next_day_number}.py"
    new_file_path = os.path.join(folder_path, new_file_name)

    # Copy the template file to the new file
    template_path = "templates/template.py"
    if not os.path.exists(template_path):
        print("Template file does not exist.")
        return

    shutil.copy(template_path, new_file_path)
    print(f"Created new file: {new_file_path}")

if __name__ == "__main__":
    main()
