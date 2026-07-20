import os
import argparse
import sys

WW_TARGETS = [2, 3, 6, 7]


def main():
    starting_path = get_args()
    ww_report, ssh_report = walk_through(starting_path)
    for key, values in ww_report.items():
        print(key, values)
    for key, values in ssh_report.items():
        print(key, values, 'ssh')

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Enter a folder where you would like to check to check premissions")
    args = parser.parse_args()
    return args.path

def walk_through(path):
    ww_report={}
    ssh_report = {}
    files_scanned = 0
    try:
        for (root, dirs, files) in os.walk(path, topdown=True):
            for i in files:
                full_path = os.path.join(root, i)
                oct_num = octal_num(full_path)
                files_scanned += 1
                if ".ssh" in full_path:
                    ssh_permission(oct_num, full_path, ssh_report)
                else:
                   check_permission(oct_num,full_path, ww_report)

        
        return ww_report, ssh_report
    except FileNotFoundError:
        print(f"Folder {full_path} doesn't exist or you dont have")
        sys.exit(1)
    except PermissionError:
        print("PermissionError")
    


def octal_num(path):
    status = os.stat(path=path)
    return oct(status.st_mode)[-3:]

def check_permission(oct_num, path, ww_report ):
    other_perm = oct_num[-1]
    if int(other_perm) in WW_TARGETS:
        ww_report[path] = oct_num

    return ww_report

def ssh_permission(oct_num, path, ssh_report):
    owner_perm = int(oct_num[0])
    group_perm = int(oct_num[1])
    other_perm = int(oct_num[-1])

    if owner_perm > 6 or group_perm != 0 or other_perm != 0:
        ssh_report[path] = oct_num

    return ssh_report
main()
