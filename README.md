# turtle-imt-ales

## Drive du cours

<https://docs.google.com/presentation/d/1KK2pByMb-ojbXt3BGP8r6uaXgIfrKsmY/edit?usp=sharing&ouid=115338138531092523446&rtpof=true&sd=true>


## Réseau IMT
--> se connecter en ethernet pour avoir internet pour les mises à jour si necessaire

--> sur la turtlebot, créer un hotspot wifi SSID Turtlebot<n°> et mtp Turtlebot<n°> adresse de la turtle bot normalement 10.42.0.1

<https://www.how2shout.com/how-to/2-ways-to-create-wifi-hotspot-in-ubuntu-20-04-lts-focal-fossa.html>

--> sur le pc de pilotage, se connecter au hotspot de la turtle bot et parametrer le .bashrc avec son adresse ip


## Package ROS TP IMT Ales

	$ sudo apt-get install git
	$ cd ~/catkin_ws/src
	$ git clone https://github.com/Rastafouille/imt_turtle.git
	$ cd ~/catkin_ws
	$ catkin_make


## Clé wifi TL-WN823N single band
 
on Ubuntu 20.04 

	sudo apt-get install dkms
 	git clone https://github.com/clnhub/rtl8192eu-linux
	cd rtl8192eu-linux
	./install_wifi.sh
	
## Clé wifi T600 et T2U double band

on Ubuntu 20.04 
	
	sudo apt-get install dkms
 	git clone https://github.com/aircrack-ng/rtl8812au.git
	cd rtl8812au
	sudo make dkms_install
	
	

