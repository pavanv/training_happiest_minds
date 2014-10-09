import subprocess

result = subprocess.check_output(['ls', '-l'])
print 'result={}'.format(result)
print '\n\noutput has {} chars'.format(len(result))