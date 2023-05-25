# How to start up backend services

## MySQL Server

Fresh Install

SQL Server

* Create Ubuntu server. If using VM's look at this https://unix.stackexchange.com/questions/419321/why-are-my-cloned-linux-vms-fighting-for-the-same-ip/419322#419322
* Install net-tools so you can run ifconfig, the command is `sudo apt install net-tools`
* Run `sudo apt install mysql-server` to download MySQL server on machine
* Run `sudo service mysql status` to check if MySQL is now running
* Edit configuration file to allow outside connections to server. Navigate to `/etc/mysql/mysql.conf.d/` and run `sudo nano mysqld.cnf`
* Change line to `bind-address = 0.0.0.0`
* Clone backend into folder of choosing, suggested in the users /home/ directory. Clone with `git clone https://www.github.com/kylerupp/WeatherBackend`
* Add database from backend repository using `sudo mysql -u root -p </path/to/db.sql`
* Enter MySQL shell with `sudo mysql`
* Add user with `CREATE USER 'name'@'host_name' IDENTIFIED WITH chaching_sha2_password BY 'password';`. Note host_name is the name of the computer that will be connecting to the server.
* Grant privilegest to the new user by running command `GRANT INSERT, UPDATE, DELETE, SELECT ON database_name.table_name TO 'name'@'host_name';`
* Flush privileges `FLUSH PRIVILEGES;`

Backend Server

* Create Ubuntu Server
* Install net-tools so you can run ifconfig, the command is `sudo apt install net-tools`
* `sudo apt install python3-pip`
* `pip install flask`
* `pip install mysql-connector`
* Run `sudo nano /etc/environment`
* Add `SQL_USER`, `SQL_PASS`, `SQL_HOST`, `SQL_DB` using `export VAR_NAME="VAR_VALUE"`
* To start server run command `python3 -m flask run --host=0.0.0.0`
