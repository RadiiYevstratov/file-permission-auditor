Chybu som opravil. Dufam ze nemusim posielat cely kod len kvoli tomu ze som posunul riadok o par medzier. Tu je README.md:# File Permission Auditor

The **File Permission Auditor** is a Python command-line tool that scans a directory and analyzes Linux file permissions to identify common security misconfigurations.

It focuses on detecting:

- **World-writable files**, which can be modified by any user.

- **Insecure SSH files** inside `.ssh` directories that have permissions more permissive than recommended.

## Features

- Recursively scans all files inside a directory.

- Detects world-writable files.

- Checks SSH-related files for unsafe permissions.

- Counts the total number of scanned files.

- Reports permission errors encountered during scanning.

- Generates a summary of all findings.

## How It Works

The application recursively traverses the specified directory using `os.walk()`.

For every file it:

1. Reads the file's permission bits using `os.stat()`.

2. Converts the permissions to octal format.

3. Determines whether the file is:

   - world-writable (write permission for "others"), or

   - located inside a `.ssh` directory with permissions that allow access to the group or other users.

4. Stores every finding and prints a report after the scan finishes.

If the program encounters directories it cannot access, it counts the permission errors and continues scanning instead of terminating.

## Problem It Solves

Incorrect Linux file permissions are a common security issue.

World-writable files can allow unauthorized users to modify data, while overly permissive SSH files may expose private keys or prevent SSH from accepting the files due to insecure permissions.

This tool provides a quick way to audit a directory and identify files that may require permission changes.

## Usage

```bash

python3 auditor.py <directory_path>

```

### Arguments

| Argument | Description |

|----------|-------------|

| `directory_path` | Path to the directory that will be scanned |

## Example

```bash

python3 main.py /home/user

```

### Example Output

```text

=== WORLD-WRITABLE FILES (2) ===

/home/user/public/file.txt (666)

/var/tmp/demo.log (666)

=== UNSAFE SSH FILES (1) ===

/home/user/.ssh/id_rsa (644)

=== SUMMARY ===

Files scanned: 1524

Findings: 3

Skipped (no access): 2

```

## What I Learned

This project helped me improve my understanding of:

- Linux file permissions (`rwx` and octal notation)

- Recursive file system traversal with `os.walk()`

- File metadata using `os.stat()`

- Handling `PermissionError` exceptions

- Building command-line applications with `argparse`

- Writing simple security auditing tools in Python
