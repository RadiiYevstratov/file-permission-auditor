# File Permission Auditor

The **File Permission Auditor** scans directories and analyzes Linux file permissions to help identify files and directories with potentially insecure permission settings.

It is designed as a simple security auditing tool that highlights world-writable files and directories while also reporting permission-related errors encountered during the scan.

## Features

- Recursively scans directories and subdirectories.
- Detects world-writable files.
- Detects world-writable directories.
- Counts the total number of scanned files.
- Reports permission errors encountered during scanning.
- Generates a clear audit summary.

## How It Works

The application recursively walks through the specified directory using Python's built-in file system functions.

For every file and directory, it reads the permission bits and checks whether they are writable by everyone (world-writable). During the scan, it also handles inaccessible files or directories and counts any permission-related errors instead of stopping the program.

After the scan is complete, the tool prints a summary containing:
- Total scanned files
- Number of world-writable files
- Number of world-writable directories
- Number of permission errors

## Problem It Solves

Incorrect file permissions are one of the most common Linux security misconfigurations. Files or directories that are writable by every user can allow unauthorized modification, accidental deletion, or privilege escalation.

This tool helps administrators, students, and cybersecurity learners quickly identify potentially insecure permissions and gain better visibility into the security of a Linux file system.

## Usage

```bash
python3 main.py <directory_path>
```

### Arguments

| Argument | Description |
|----------|-------------|
| `directory_path` | Path to the directory that should be scanned |

## Example

```bash
python3 main.py /home/user
```

### Example Output

```
========== File Permission Audit ==========
Directory: /home/user

Files scanned: 1824
World-writable files: 4
World-writable directories: 2
Permission errors: 3

World-writable files:
- /home/user/shared/test.txt
- /home/user/public/data.log
- /var/tmp/example.txt
- /tmp/demo.txt

World-writable directories:
- /home/user/shared
- /tmp/demo
```