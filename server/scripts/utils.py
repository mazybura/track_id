import os
import pandas as pd


def read_tsv(file_path):
    try:
        df = pd.read_csv(file_path, delimiter="\t", encoding="utf-8")
        if df.empty:
            print(f"File {file_path} is empty or incorrectly formatted.")
            return None
        print(df.columns)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def write_to_df(data, column_names):
    try:
        df = pd.DataFrame(data, columns=column_names)
        return df
    except Exception as e:
        print("An error occurred while writing data to the DataFrame:", e)
        return None


def count_files_in_folder(folder_path):
    try:
        files_and_folders = os.listdir(folder_path)
        files = [
            file
            for file in files_and_folders
            if os.path.isfile(os.path.join(folder_path, file))
        ]
        return len(files)
    except Exception as e:
        print(f"Error accured: {e}")
        return None


# df = read_tsv(r"C:\Users\micha\code\TuneFetch\server\data\tracks.tsv")
# print(df.columns)


import os

# Tu wpisz foldery i pliki, które chcesz pomijać
IGNORED_DIRS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    "venv",
    "data",
    "out",
}
IGNORED_FILES = {"Thumbs.db", ".DS_Store"}


def print_directory_structure(root_path, indent=""):
    try:
        items = os.listdir(root_path)
    except PermissionError:
        print(f"{indent}[Permission Denied]: {root_path}")
        return
    except FileNotFoundError:
        print(f"{indent}[Not Found]: {root_path}")
        return

    for item in sorted(items):
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            if item in IGNORED_DIRS:
                continue
            print(f"{indent}📁 {item}/")
            print_directory_structure(item_path, indent + "    ")
        else:
            if item in IGNORED_FILES:
                continue
            print(f"{indent}📄 {item}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Użycie: python skrypt.py <ścieżka_root>")
    else:
        root = sys.argv[1]
        print(f"Struktura katalogów dla: {root}")
        print_directory_structure(root)
