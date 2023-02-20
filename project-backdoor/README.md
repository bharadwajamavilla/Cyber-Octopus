# INSTRUCTIONS :

1. Copy the backdoor.py file to Desktop of target windows machine</br>

2. Navigate to the desktop in terminal and run </br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;pip install pyinstaller </br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;and </br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;pyinstaller backdoor.py --onefile --noconsole </br>

3. Now we got 3 folders and 1 file on Desktop. They are </br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1. dist&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;(Folder)</br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2. build&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;(Folder) </br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;3. __pycache__ &emsp;&emsp;&emsp;&emsp;&ensp;(Folder) </br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;4. backdoor.spec&emsp;&emsp;&ensp;(File) </br>

4. We can delete all those EXCEPT "dist" Folder

5. In the dist Folder we have "backdoor.exe" file

6. Run server.py in kali linux (before opening backdoor.exe)

7. Now open the backdoor.exe on windows

8. The backdoor.exe file can be scanned with Microsoft defender, and no threats will be found !!

9. We can see the Listener got a connection from the target, and opens terminal. 💥
