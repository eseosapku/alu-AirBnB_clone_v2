#!/usr/bin/env bash
#setting up nginx server
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html
sudo service nginx restart

