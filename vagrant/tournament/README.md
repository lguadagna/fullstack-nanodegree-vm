#Tournament with Swiss Pairings

##Configuring the Environment##

1. Install git.  If you don't have git already here is the link to install it: 

[link to git] https://git-scm.com/downloads

create a git respository; suggested name: tournament

2. Install Virtual Box. Virtual Box provides the virtual machine.

[link to virtual box] https://www.virtualbox.org/wiki/Downloads

2. Install vagrant. Vagrant has configurations which will configure the Virtual Box.

[link to vagrant] https://www.vagrantup.com/downloads.html


3. clone the github Virtual Machine configuration 
 
`git clone  https://github.com/lguadagna/fullstack-nanodegree-vm  `

4. Vagrant up.
Cd to the /vagrant directory of cloned repository above. Type

`vagrant up`


5. login to the virtual machine.
type:
`vagrant ssh`
After vagrant up completes, you will be in the /home/vagrant directory.   

6. Change to the shared directory: /vagrant. inside the virtual machine window type:

`cd /vagrant`

4. run the configuration file pg_config.sh 

7. Create the database: 

`psql -f tournament.sql`

8. Run the program.  Test. Test all the procedures and methods in the swiss pairings tournament by testing.
type:
`python tournament_test.py`


`--------------------------------------------------------------------`

##This project is demonstrating##
1. creation of sql data structures with tournament.sql and
2. use of the database to store player and match information
3. the tournament.py code can be used to create and delete players and matches.
it can also be used to pair players of equal ability.

The exercise was to set up a vagrant virtual linux machine and sql server and then use that server.
this virtual machine is operating system independant as it runs linux in a stand alone process
