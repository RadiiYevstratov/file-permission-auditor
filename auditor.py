import os
import argparse
import sys



def main():
    starting_path = get_args()
    ww_report, ssh_report, files_scanned, permission_error = walk_through(starting_path)
    print_result(ww_report=ww_report, ssh_report=ssh_report, files_scanned=files_scanned,permission_error=permission_error)



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Enter a folder where you would like to check to check permissions")
    args = parser.parse_args()
    return args.path




def walk_through(path):
    ww_report={}
    ssh_report = {}
    files_scanned = 0
    permission_error = 0

    def walk_error(error):
        nonlocal permission_error

        if isinstance(error, PermissionError):
            permission_error +=1

    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a directory or does not exist.", file=sys.stderr)
        sys.exit(1)
    for (root, dirs, files) in os.walk(path, topdown=True, onerror=walk_error):
        for i in files:
            full_path = os.path.join(root, i)
            oct_num = octal_num(full_path)
            files_scanned += 1
            if ".ssh" in root.split(os.sep):
                ssh_permission(oct_num, full_path, ssh_report)
            else:
                check_permission(oct_num,full_path, ww_report)

    
    return ww_report, ssh_report, files_scanned, permission_error


def octal_num(path):
    status = os.stat(path=path)
    return oct(status.st_mode)[-3:]

def check_permission(oct_num, path, ww_report ):
    other_perm = oct_num[-1]
    if int(other_perm) & 2:
        ww_report[path] = oct_num

    return ww_report

def ssh_permission(oct_num, path, ssh_report):
    group_perm = int(oct_num[1])
    other_perm = int(oct_num[-1])

    if group_perm != 0 or other_perm != 0:
        ssh_report[path] = oct_num

    return ssh_report

def print_result(ssh_report, ww_report, files_scanned, permission_error):
    print(f"=== WORLD-WRITABLE FILES ({len(ww_report)}) === \n")
    for key, value in ww_report.items():
        print(f"{key} ({value})")
    
    print("\n")

    print(f"=== UNSAFE SSH FILES ({len(ssh_report)}) === \n")
    for key,value in ssh_report.items():
        print(f"{key} ({value})")

    print("\n")

    print("=== SUMMARY === \n")
    print(f"Files scanned: {files_scanned}")
    print(f"Findings: {len(ssh_report) + len(ww_report)}")
    print(f"Skipped (no access): {permission_error}")


if __name__ == "__main__":
    main()


