#!/usr/bin/env bash
<<<<<<< HEAD
#setting up nginx server

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
=======
#deploy web static

#Install nginx 
sudo apt-get -y update
sudo apt-get -y install nginx

#create folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#fake html file
echo "<html>
      <head>
      </head>
      <body>
        Holberton School
      </body>
    </html>" | sudo tee /data/web_static/releases/test/index.html

#create symbolic link 
#if it already exists, delete and recreate
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#give ownership of data folder to ubuntu user
chown -R ubuntu:ubuntu /data/

#update the ngix config
sudo sed -ri "55i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-available/default

#restart nginx
>>>>>>> a8c4b288fb66d0ef1047421a7606ff8ed4c0fe17
sudo service nginx start
