# backutil
Python Backup Utility

## Description:
`backutil` is a wrapper for the python `tarfile` library. As `tarfile` is a standard Python library, using `backutil` will provide a cross-platform and simple backup utility.


## Installation:

Install using `pip`:

`sudo pip3 install backutil`


## Usage:

```
❯ ./backutil --help
usage: backutil [-h] --path PATH [PATH ...] --dest DEST [-z] [-q]

Python backup utility

optional arguments:
  -h, --help            show this help message and exit
  --path PATH [PATH ...]
                        path(s) to backup
  --dest DEST           destination of backup
  -z, --zip             use gzip to compress the backup file
  -q, --quiet           suppress output
```

### Example commands:

Backup two files to a .tar archive:
`❯ backutil --path tmp.txt tmp2.txt --dest ~/Documents/file.tar`

Backup and compress to .tar.gz archive:
`❯ backutil --path tmp.txt tmp2.txt --dest ~/Documents/file.tar.gz -z`
