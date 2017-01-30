# Catalog of Vitamain and Minerals in Food Sources

## Configuring the environment## 
1. Clone this directory. You will need git installed.

2. To install git.  If you dont have git already here is the link to install it:

[link to git] https://git-scm.com/downloads

create a git respository; suggested name: vitamins


2. Install Virtual Box. Virtual Box provides the virtual machine.

[link to virtual box] https://www.virtualbox.org/wiki/Downloads

2. Install vagrant. Vagrant has configurations which will configure the Virtual Box.

[link to vagrant] https://www.vagrantup.com/downloads.html


3. clone the github Virtual Machine configuration

git clone https://github.com/lguadagna/fullstack-nanodegree-vm

4. Vagrant up.
Cd to the /vagrant directory of cloned repository above. Type

`vagrant up`

This will run the configuration file pg_config.sh

5. login to the virtual machine.
type:
`vagrant ssh`
After vagrant up completes, you will be in the /home/vagrant directory.

6. Change to the shared directory: /vagrant. inside the virtual machine window type:

`cd /vagrant`


7. Create the database structure.
within the vm run:
` python database_setup.py`

8. Add the initial entries to the database.
`python some_vitamins.py`

9. startup the web server.
`python finalproject.py`

10. Access the project at:
`http://localhost:5000`


`--------------------------------------------------------------------`

##This project is demonstrating##
1. creation of sql data structures 
2. use of sql alchemy to manipulate the database
3. use of jinja templates
4. use of flask
5. using an external authorization (oAuth) system like google or facebook to secure login
6. use of a bootstrap template




