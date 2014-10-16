import subprocess, os

def run_cmd(commands, user_input = ''):
	p = subprocess.Popen(commands, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	print p.communicate(user_input)[0]	


#apt-get update
#commands = ['sudo', 'apt-get', 'update']
#run_cmd(commands)

#apt-get upgrade
#commands[2] = 'upgrade'
#user_input = 'y'
#run_cmd(commands, user_input)

#cp cemc.remmina ../cemc.remmina
commands = ['cp', 'cemc.remmina', '../cemc.remmina']
run_cmd(commands)

#cat ../cemc.remmina
commands = ['cat', '../cemc.remmina']
run_cmd(commands)

#cp cemc-rdp.conf ../.config/upstart/cemc-rdp.conf
commands = ['cp', 'cemc-rdp.conf', '../.config/upstart/cemc-rdp.conf']
run_cmd(commands)

#cp cemc-rdp.sh ../cemc-rdp.sh
commands = ['cp', 'cemc-rdp.sh', '../cemc-rdp.sh']
run_cmd(commands)

#cp icon.png ../icon.png
commands = ['cp', 'icon.png', '../icon.png']
run_cmd(commands)

#chmod +x ../cemc-rdp.sh
commands = ['sudo', 'chmod', '+x', '../cemc-rdp.sh']
run_cmd(commands)

#create absolute path for desktop shortcut
shortcut_path = 'Exec=/home/' + os.environ['USER'] + '/cemc-rdp.sh\n'
icon_path = 'Icon=/home/' + os.environ['USER'] + '/icon.png\n'

#generate icon
os.remove('cemc.desktop')
desktop_file = open('cemc.desktop', 'a')
desktop_file.write('[Desktop Entry]\n')
desktop_file.write('Type=Application\n')
desktop_file.write('Name=Remote Desktop\n')
desktop_file.write('Comment=who comments on a desktop shortcut\n')
desktop_file.write('Terminal=false\n')
desktop_file.write(shortcut_path)
desktop_file.write(icon_path)
desktop_file.close()

#cp cemc.desktop ../Desktop/cemc.desktop
commands = ['cp', 'cemc.desktop', '../Desktop/cemc.desktop']
run_cmd(commands)

#chmod +x ../Desktop/cemc.desktop
commands = ['chmod', '+x', '../Desktop/cemc.desktop']
run_cmd(commands)

#sudo reboot
#commands = ['sudo', 'reboot']
#run_cmd(commands)
