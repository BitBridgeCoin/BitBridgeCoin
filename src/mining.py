import subprocess
import time
print('start mining...')
while(1):
    result = ""
    while(len(result) < 20):
        result = subprocess.check_output(['./bitbridgecoin-cli', 'generate', '1'])
    print("Found New Block:  " + result.split('"')[1].split('"')[0])
    print("Mining For Next Block...")
    time.sleep(10)
