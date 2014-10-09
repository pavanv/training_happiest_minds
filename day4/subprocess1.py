import subprocess

result = subprocess.call(['ls', '-l'])
print '\n\nresult={}'.format(result)