#!/usr/bin/env bash
# Sets up ngingx and sets the host
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/released/test/
echo "Holberton School" > /data/web_static/release/text/index/html
sudo ln -s /data/web_static/release/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
sudo service ngingx restart
