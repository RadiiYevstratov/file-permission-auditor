import os
import argparse
import sys

WW_TARGETS = [2, 3, 6]
def main():
    starting_path = get_args()
    walk_through(starting_path)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Enter a folder where you would like to check to check premissions")
    args = parser.parse_args()
    return args.path

def walk_through(path):
    try:
        for (root, dirs, files) in os.walk(path, topdown=True):
            for i in files:
                full_path = os.path.join(root, i)
                oct_num = octal_num(full_path)
    except(FileNotFoundError):
        print(f"Folder {full_path} doesn't exist")
        sys.exit(1)


def octal_num(path):
    status = os.stat(path=path)
    return oct(status.st_mode)[-3:]

main()