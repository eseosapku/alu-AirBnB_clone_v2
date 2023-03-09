#!/usr/bin/env bash
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
sudo service nginx start
