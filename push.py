import os
import sys
me = sys.argv[1]
if me:
    cmd = 'git add -A'
    os.system(cmd)
    cmd = 'git commit -m ' + me
    os.system(cmd)
    cmd = 'git push origin master'
    os.system(cmd)
else:
    print("请传入参数")
