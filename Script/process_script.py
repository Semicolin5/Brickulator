import os


SCRIPT_FILE_PATH = "C:\\Users\\Colin\\Documents\\LEGO ISLAND BACKUP\\DUNECAR.SI"
PROCCESSED_FILE_PATH = os.getcwd() + "\\output"


if __name__ == "__main__":
    print(f"Attempting to process file: {SCRIPT_FILE_PATH}")
    file_path, file_extension = os.path.splitext(SCRIPT_FILE_PATH)

    if (file_extension != ".SI"):
        print(f"File extension {file_extension} is not a Script file.")

    with open(SCRIPT_FILE_PATH, 'rb') as script:
        print("Yeah this will probably do something")
        #process_script_file(script)
