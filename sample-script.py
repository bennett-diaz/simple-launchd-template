import os

#creates a .txt file on the Desktop
def create_text_filefile():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "my_new_test_file.txt")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("This is a test file.")
            f.close()

def main():
    create_text_filefile()
    print("This is the main function")


if __name__ == "__main__":
    main()
