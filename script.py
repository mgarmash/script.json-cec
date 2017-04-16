import xbmc
import urlparse
import sys
import os

try:
        params = urlparse.parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command',None)
except:
        command = None

if command and command[0] == 'activate':
        os.system("echo -ne '\x40\x04' > /dev/cec")

elif command and command[0] == 'standby':
        os.system("echo -ne '\xff\x36' > /dev/cec")
