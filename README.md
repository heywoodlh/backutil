# backutil
Python Backup Utility

## Description:
`backutil` is a wrapper for the python `tarfile` library. As `tarfile` is a standard Python library, using `backutil` will provide a cross-platform and simple backup utility.


## Installation:

Install using `pip`:

`sudo pip3 install backutil`


## Usage:
```
❯ backutil --help
usage: backutil [-h] [--path PATH [PATH ...]] [-o OUTFILE] [--webdav URL]
                [--remote REMOTE PATH] [--encrypt RECIPIENT] [-z] [--rm] [-v]
                [-q] [-i] [-V]

Python backup utility

optional arguments:
  -h, --help            show this help message and exit
  --path PATH [PATH ...]
                        path(s) to backup
  -o OUTFILE, --outfile OUTFILE
                        output file of backup
  --webdav URL          WebDav URL to upload to
  --remote REMOTE PATH  Remote WebDav path to upload to
  --encrypt RECIPIENT   Use gpg to encrypt file
  -z, --zip             use gzip to compress the backup file
  --rm                  remove local backup file
  -v, --verbose         enable verbose output
  -q, --quiet           suppress output
  -i, --insecure        ignore SSL certificate warnings
  -V, --version         print version of backutil
```


### Example commands:

Backup two files to a .tar archive:
`❯ backutil --path tmp.txt tmp2.txt --outfile ~/Documents/file.tar`

Backup and compress to .tar.gz archive:
`❯ backutil --path tmp.txt tmp2.txt --outfile ~/Documents/file.tar.gz -z`

Backup to a .tar archive verbosely:
`❯ backutil --path tmp.txt tmp2.txt --outfile ~/Documents/file.tar -v`

Backup and compress to a .tar.gz archive, supressing output:
`❯ backutil --path tmp.txt tmp2.txt --outfile ~/Documents/file.tar.gz -z -q`

Backup file, zip it and upload to Nextcloud Webdav as file.tar.gz in the Nextcloud user's root directory: 
`❯ backutil --path tmp.txt tmp2.txt --outfile ~/file.tar.gz --webdav 'https://cloud.example.com:8080/' --remote file.tar.gz -z`

Backup files, zip them and upload the archive to Nextcloud Webdav as file.tar.gz in the Nextcloud user's root directory, then remove the local archive: 
`❯ backutil --path tmp.txt tmp2.txt --outfile ~/file.tar.gz --webdav 'https://cloud.example.com:8080/' --remote file.tar.gz -z --rm`


### Configuration:

Backutil supports a configuration file storing details, which enables non-interactive usage of backups (in case you'd like to run backutil as a cron job or something similar). 

Place the file in your home directory as `.backutil.conf`. Currently this is the configuration you can use:
```
[WEBDAV]
Username = username
Password = mysupersecretpassword
#Command = command_to_print_password
```

I would recommend not storing your password in plaintext and use `gpg`, `pass` or some other secure way to print your password from the command line without storing it unencrypted. That is why the 'Command' directive is supported in the configuration.  


### Additional Information:
Currently WebDav functionality has only been tested on an instance of Nextcloud.
