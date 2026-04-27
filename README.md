# Minecraft
Voxel Engine (like Minecraft) in Python and OpenGL 

Control: WASDQE + mouse

![minecraft](/screenshot/0.jpg)

=================== How to use ===================


##### Depending on your python version, you may have to change python3 to python ####

=================== Instructions on how to use this ===================

In your terminal, run this: git clone https://github.com/Coder5330/Minecraft

It should say something like: 

Cloning into 'Minecraft'...

remote: Enumerating objects: 121, done.

remote: Counting objects: 100% (121/121), done.

remote: Compressing objects: 100% (119/119), done.

remote: Total 121 (delta 13), reused 0 (delta 0), pack-reused 0 (from 0)

Receiving objects: 100% (121/121), 872.27 KiB | 5.35 MiB/s, done.

Resolving deltas: 100% (13/13), done.

Then run: cd Minecraft

=================== Single Player ===================

For single player, run: python3 main.py

It should open a Minecraft like world

=================== Multiplayer ===================

You need multiple laptops for multiplayer, all on the same WiFi network.

--- On the HOST laptop ---
Step 1: Find your IP address:
  Mac/Linux:  ifconfig | grep "inet "
  Windows:    ipconfig
  Look for something like 192.168.x.x (NOT 127.0.0.1)

Step 2: Start the server:
  python3 server.py

Step 3: Join the game (host plays too):
  python3 main.py --host 127.0.0.1 --name yourNameHere

--- On EVERY OTHER laptop ---
Step 4: Join using the HOST's IP from Step 1:
  python3 main.py --host 192.168.x.x --name yourNameHere
  (replace 192.168.x.x with the host's actual IP)

Example:
  Host's IP is 192.168.50.240
  Host runs:    python3 main.py --host 127.0.0.1 --name Alice
  Friend runs:  python3 main.py --host 192.168.50.240 --name Bob

Note: Everyone must be on the same WiFi network.
