"""Characterize a disk image.

Attempt to use fiwalk; if that fails, attempt to use hfs2dfxml.

Usage::

    python fiwalk-fallback-hfs2dfxml.py --relative-location=/path/to/disk-image.img

"""

from __future__ import print_function
import argparse
import os
import shutil
from subprocess import check_output, Popen, PIPE
import sys
from uuid import uuid4


def fiwalk(relative_location):
    """Use fiwalk to characterize the disk image."""
    cmd = [
        'fiwalk',
        '-x',
        relative_location,
        '-c',
        '/usr/lib/archivematica/archivematicaCommon/externals/fiwalk_plugins/ficonfig.txt'
    ]
    return check_output(cmd)


def hfs2dfxml(relative_location):
    """Use hfs2dfxml to characterize the disk image."""
    output_path = os.path.expanduser('~/temp_{}.xml'.format(uuid4()))

    # We copy the disk image to a temporary location because hfs2dfxml alters
    # the file content in some way (for some unknown reason) and this will end
    # up breaking fixity checking later on during ingest. See
    # https://github.com/cul-it/hfs2dfxml/issues/12
    temp_disk_image_path = relative_location + '.tmp'
    shutil.copy2(relative_location, temp_disk_image_path)

    # This is necessary because HFSutils (which hfs2dfxml depends on) needs
    # a HOME env var defined.
    # TODO: set HOME in MCPClient/lib/archivematicaClient.py#L180-L183 (and
    # ultimately in upstart)
    os.environ['HOME'] = '/var/lib/archivematica/'
    cmd = [
        'python',
        # TODO: fix!
        '/home/vagrant/bin/hfs2dfxml/hfs2dfxml/hfs2dfxml.py',
        relative_location,
        output_path
    ]
    process = Popen(cmd, stdout=PIPE, stderr=PIPE)
    process.communicate()
    with open(output_path) as filei:
        out = filei.read()
    os.remove(output_path)
    shutil.move(temp_disk_image_path, relative_location)
    return out


def main(relative_location):
    """Attempt to use fiwalk to characterize the disk image; if that fails,
    attempt to use hfs2dfxml.
    """
    try:
        out = fiwalk(relative_location)
        if "TSK_Error 'Cannot determine file system type'" in out:
            out = hfs2dfxml(relative_location)
    except Exception as error:
        print(error)
        return 1
    print(out)
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--relative-location")
    args, unknown = parser.parse_known_args()
    sys.exit(main(args.relative_location))
