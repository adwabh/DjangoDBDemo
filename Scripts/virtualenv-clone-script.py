#!c:\users\nex7ngg\documents\python\pythonrest\django04\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'virtualenv-clone==0.2.6','console_scripts','virtualenv-clone'
__requires__ = 'virtualenv-clone==0.2.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('virtualenv-clone==0.2.6', 'console_scripts', 'virtualenv-clone')()
    )
