import os
import subprocess
import traceback
import time

if __name__ == '__main__':
    filename = 'window.ui'
    lastmodified = os.stat(filename).st_mtime
    while True:
        newmodified = os.stat(filename).st_mtime
        if newmodified != lastmodified:
            print('Change detected, regenerating ui')
            lastmodified = newmodified
            try:
                subprocess.call('generate_py.bat')
            except OSError:
                traceback.print_exc()
                break
        time.sleep(3)
