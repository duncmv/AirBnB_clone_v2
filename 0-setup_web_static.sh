#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/  /data/web_static/shared/
sample="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"

echo "$sample" | sudo tee /data/web_static/releases/test/index.html

link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"

if [ -L "$link_path" ]; then
	    sudo rm "$link_path"
fi

sudo ln -s "$target_path" "$link_path"

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '59i\	location /hbnb_static {\n		alias /data/web_static/current/;\n	}' /etc/nginx/sites-available/default
sudo service nginx restart
