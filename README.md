# File Permission Auditor

File Permission Auditor is a Python command-line tool that scans a Linux directory tree and audits file permissions for common security issues.

The application detects:
- World-writable files that can be modified by any user on the system.
- Insecure SSH files inside `.ssh` directories where group or other users have any permissions set.

It also reports the total number of scanned files and counts directories that could not be accessed because of insufficient permissions.

---

## Features

- Recursively scans directories and subdirectories.
- Detects world-writable files.
- Audits SSH files for insecure permissions.
- Reports inaccessible directories without interrupting the scan.
- Displays a summary of all findings.

---

## Security Context

Incorrect file permissions are a common Linux security misconfiguration.

World-writable files may allow unauthorized users to modify application data, replace configuration files, or tamper with system resources. Likewise, SSH private keys with group or world permissions may expose sensitive authentication material and are rejected by OpenSSH for security reasons.

---

## How It Works

The application recursively traverses the specified directory using Python's `os.walk()`.

For every file it:

1. Reads the file mode using `os.stat()`.
2. Converts the mode to octal notation (for example `644` or `755`).
3. Flags a file as **world-writable** when the write bit for **others** is set (`mode & 0o002`).
4. If the file is located inside a `.ssh` directory, it is reported when **any group or other permission bit is set** (`mode & 0o077`).
5. Continues scanning even if some directories cannot be accessed, while counting permission-related errors.

After the scan, the tool prints:

- World-writable files
- Unsafe SSH files
- Number of scanned files
- Total findings
- Number of skipped directories

---

## Requirements

- Python 3.10 or newer
- Linux operating system
- No third-party dependencies (Python Standard Library only)

---

## Usage

```bash
python3 auditor.py <directory_path>
```

### Arguments

| Argument | Description |
|----------|-------------|
| `directory_path` | Path to the directory that should be scanned |

---

## Example

```bash
python3 auditor.py /home/user
```

### Example Output

```text
=== WORLD-WRITABLE FILES (2) ===

/tmp/test.txt (666)
/var/tmp/demo.log (777)

=== UNSAFE SSH FILES (1) ===

/home/user/.ssh/id_rsa (644)

=== SUMMARY ===

Files scanned: 1524
Findings: 3
Skipped (no access): 2
```

---

## Exit Codes

| Exit Code | Meaning |
|----------:|---------|
| `0` | Scan completed successfully |
| `1` | Invalid directory path or unrecoverable startup error |

---

## Limitations

- Only regular files are audited.
- The tool does not evaluate symbolic links separately.
- It does not check SUID, SGID, or sticky bits.
- It does not distinguish between SSH private and public keys. Any file inside a `.ssh` directory with group or other permissions is reported.
- ACLs (Access Control Lists) and extended file attributes are not analyzed.

---

## What I Learned

This project helped me improve my understanding of:

- Linux file permission model (`rwx` and octal notation)
- Secure SSH file permission requirements
- Recursive filesystem traversal using `os.walk()`
- Reading file metadata with `os.stat()`
- Building robust command-line tools with `argparse`
- Exception handling for filesystem operations
- Designing a simple security auditing utility
