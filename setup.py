import subprocess

def run_cmd(commands, user_input = ''):
	p = subprocess.Popen(commands, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	print p.communicate(user_input)[0]	


#apt-get update
commands = ['sudo', 'apt-get', 'update']

run_cmd(commands)


#apt-get upgrade
commands[2] = 'upgrade'
user_input = 'y'

run_cmd(commands, user_input)

#cp cemc.remmina ~/cemc.remmina
commands = ['cp', 'cemc.remmina', '../cemc.remmina']
run_cmd(commands)

commands = ['cat', '../cemc.remmina']
run_cmd(commands)
