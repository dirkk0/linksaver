import subprocess

#cmd  = "convert -o %s_%i -F " % (thisProject, i)
cmd = ""

import os


# os.chdir(".")
for files in os.listdir("."):
    if files.endswith(".jpg"):
        print files


if cmd:
    process = subprocess.Popen(cmd, shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output,stderr = process.communicate()
    status = process.poll()
    print output
