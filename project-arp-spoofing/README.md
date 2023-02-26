# INSTRUCTIONS :

1. Open kali Terminal and install Bettercap used for ARP spoofing

2. To install Bettercap run (If already installed, Go to step 3)<br>
&emsp;&emsp;&emsp;$ sudo su <br>
&emsp;&emsp;&emsp;$ apt-get install bettercap

3. Run Bettercap <br>
&emsp;&emsp;&emsp;$ bettercap

4. Now open the sniff.cap file, and replace "0.0.0.0" with target ip address

5. To know all the ip of systems in our network, <br>
&emsp;&emsp;&emsp;Open another terminal <br>
&emsp;&emsp;&emsp;$ bettercap <br>
&emsp;&emsp;&emsp;$ net.probe on <br>
&emsp;&emsp;&emsp;We can see all the ip address in our network

6. Now run the command <br>
&emsp;&emsp;&emsp;$ bettercap -iface eth0 -caplet sniff.cap

7. To exit spoofing run, <br>
&emsp;&emsp;&emsp;$ exit

8. After exiting it automatically set all the fields to defaults (ie, previous values)

9. To check whether there is ARP poisioning going on in our network <br>
&emsp;&emsp;&emsp; Open terminal ( In Windows ) <br>
&emsp;&emsp;&emsp; $ arp -a

10. If any two ip address have same MAC address , then ARP poisioning is performed in our network
