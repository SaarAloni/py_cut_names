import os
import sys

def main():
    directory = os.getcwd()
    user_input = input("Please enter the substring you want to cut: ")
    this_file = os.path.basename(sys.argv[0])
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            if user_input in filename:
                if filename == this_file:
                    continue
                new_name = filename.replace(user_input, "")
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

if __name__ == "__main__":
    main()