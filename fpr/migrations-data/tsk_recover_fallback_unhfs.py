"""Extract a disk image.

Attempt to use tsk_recover. If that fails, attempt to use unhfs.

Usage::

    python tsk_recover_fallback_unhfs.py disk-image.img output_dir

"""

from __future__ import print_function
import json
import os
import re
from subprocess import check_output, CalledProcessError, PIPE, Popen
import sys
from uuid import uuid4


class TskRecoverException(Exception):
    pass


def main(package, outdir):
    """Attempt to use tsk_recover to extract the disk image; if that fails,
    attempt to us unhfs.
    """
    tool_override = ''
    try:
        # -a extracts only allocated files; we're not capturing unallocated
        # files
        cmd = ['tsk_recover', package, '-a', outdir]
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        match = re.match(r'Files Recovered: (\d+)', stdout.splitlines()[0])
        if match and match.groups()[0] == '0':
            raise TskRecoverException(
                'tsk_recover failed to extract any files with the message:'
                ' {}'.format(stdout))
    except TskRecoverException:
        os.mkdir(outdir)
        cmd = [
            '/usr/local/hfsexplorer/bin/unhfs.sh',
            '-v',
            '-o',
            outdir,
            package
        ]
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        # The tool_override string, if present, must match the description
        # value of an fpr_fptool row in the database.
        tool_override = 'hfsexplorer'
    print(json.dumps({'stdout': stdout, 'tool_override': tool_override}))
    return 0


if __name__ == '__main__':
    package = sys.argv[1]
    outdir = sys.argv[2]
    sys.exit(main(package, outdir))
