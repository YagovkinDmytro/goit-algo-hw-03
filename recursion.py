import sys
import shutil
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def list_of_folder(path, indent="  "):
    for el in path.iterdir():
        if el.is_dir():
            print(f"{indent}{Fore.BLUE}📁 {el.name}")
            list_of_folder(el, indent + "  ")
        else:
            print(f"{indent}{Fore.GREEN}📄 {el.name}")     

def copy_of_files(path, new_directory_path):
    if not new_directory_path.exists():
        new_directory_path.mkdir(parents=True, exist_ok=True)
    for el in path.iterdir():
        if el.is_dir():
                copy_of_files(el, new_directory_path)
        else:
                directory_name = el.suffix
                new_folder = Path(new_directory_path/directory_name)
                if not new_folder.exists():
                    new_folder.mkdir(parents=True, exist_ok=True)
                source = Path(path/el.name)
                destination = (Path(new_folder/el.name))
                try:
                    shutil.copy2(source, destination)
                except Exception as e:
                    print(f"{Fore.RED}! Unexpected error while copying {el.name}: {e}")
                    continue

def main():
    if len(sys.argv) > 1:
        path_to_directory = Path(sys.argv[1])
        new_directory_path = Path(sys.argv[2]).joinpath("dist") if len(sys.argv) > 2 else Path("dist").absolute()
        if path_to_directory.exists() and path_to_directory.is_dir():
            directory = Path(path_to_directory)
            copy_of_files(directory, new_directory_path)
            list_of_folder(new_directory_path)
            print(f"{Fore.YELLOW}📁 '{path_to_directory.name}' has been copied into 📁 '{new_directory_path.name}'")
        else:
            print(f"{Fore.RED}The directory path is invalid or does not exist: {path_to_directory}")
    else:
         print(f"{Fore.YELLOW}Arguments are not provided")

if __name__ == "__main__":
    main()