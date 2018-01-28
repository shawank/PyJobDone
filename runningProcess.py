import subprocess
import re


def check(str)
	result = subprocess.run(['ps', '-A', '|', 'grep', str], stdout = subprocess.PIPE)
	temp = re.findall(r'grep', result.stdout.decode('UTF-8'))
	return len(temp) == 0


