import os
import argparse

def main():
    starting_path = get_args()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Enter a folder where you would like to check to check premissions")
    args = parser.parse_args()
    return args

main()