Installation Instructions

###################################
###################################
First get Ubuntu Server up and running (in Virtualbox).

I set the system up in Virtualbox with these settings.

OS:
    ubuntu-12.04.3-server-amd64.iso

RAM:
    1024MB

Networking:
    bridged

HD:
    8GB

Install SSH server:
    yes

use swap:
    No

###################################
###################################
Setup the VM's network

Run:

	sudo nano /etc/network/interfaces

Now change the file's contents to setup a static IP address:
 
	auto eth0
	iface eth0 inet static
	address 192.168.1.78
	netmask 255.255.255.0
	gateway 192.168.1.254
	dns-nameservers 192.168.1.254

Run:
	
	sudo apt-get remove dhcp-client isc-dhcp-client dhcp3-client

Run

	sudo /etc/init.d/networking restart

###################################
###################################	
Now, in the VM, run "setup_system.sh" like so:

    yes 'yes' | sudo bash setup_system.sh	

Now setup your ssh-key to access the repo and clone the repo to:

    /home/user/tic_tac_toe_verhulst

Next, run the "local_setup.sh" file with:

     bash local_setup.sh.

Before you can run the server you will need to activate virtual environment with:
       
     . ENV/bin/activate

Now you should be able to run the server with:

    uwsgi --socket tic_tac_toe.sock --wsgi-file app/wsgi.py --chmod-socket=666        
    	
###################################
###################################
Misc commands

To restart ngnix:

    sudo /etc/init.d/nginx restart

To reload ngnix's config file:

    sudo /etc/init.d/nginx reload

To run the Django app via it's builtin testing server:
   
    python manage.py runserver 0.0.0.0:8000

To sync static files, run:

    python manage.py collectstatic
    
To create SSH keys, run:

	ssh-keygen
	
To display the public key, run:

	cat ~/.ssh/id_rsa.pub
