#!/bin/bash

INSTALL_DIR="/usr/local/bin"

json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
url_all=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
url=$(echo "$url_all"| cut -d$'\n' -f 1)
echo "$url"
curl -L "$url" | tar -xz
chmod +x geckodriver
sudo mv geckodriver "$INSTALL_DIR"
echo "installed geckodriver binary in $INSTALL_DIR"

