"""Siegfried Archivematica identification command. Updated to use blkid to
attempt to identify HFS disk images when Siegfried fails.

"""

from __future__ import print_function

import os.path
import json
import subprocess
import sys


class IdToolError(Exception):
    pass


class ParseError(IdToolError):
    PREFIX = 'The output produced by siegfried could not be parsed'
    def __init__(self, message=None):
        message = self.PREFIX if message is None else '{}: {}'.format(self.PREFIX, message)
        Exception.__init__(self, message)


def blkid(path):
    try:
        return subprocess.check_output(['blkid', '-o', 'full', path])
    except Exception:
        return ''


def sf_tool(path):
    return subprocess.check_output(['sf', '-json', path])


def find_puid(sf_output):
    result = json.loads(sf_output)
    try:
        matches = result['files'][0]['matches']
    except KeyError as error:
        raise ParseError('error matching key {}'.format(error))
    if len(matches) == 0:
        raise ParseError('no matches found')
    match = matches[0]
    puid = None
    if 'puid' in match:
        puid = match['puid']
    elif 'id' in match:
        puid = match['id']
    else:
        raise ParseError
    if puid == 'UNKNOWN':
        (_, extension) = os.path.splitext(sys.argv[1])
        if extension and extension in ('.img', '.001') and 'TYPE="hfs"' in blkid(sys.argv[1]):
            return 'archivematica-fmt/6'
        else:
            raise IdToolError('siegfried determined that the file format is UNKNOWN')
    return puid


def main(path):
    try:
        print(find_puid(sf_tool(path)))
    except IdToolError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
