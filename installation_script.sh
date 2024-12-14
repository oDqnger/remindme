sudo mkdir /usr/share/remindme
sudo mkdir /usr/share/remindme/music
mkdir ~/.config/remindme/
sudo curl -v -L -H "Accept: application/octet-stream" -o ~/.config/remindme/config.toml https://github.com/oDqnger/remindme/releases/download/beta_version/config.toml
sudo curl -v -L -H "Accept: application/octet-stream" -o /usr/share/remindme/music/testing.mp3 https://github.com/oDqnger/remindme/releases/download/beta_version/testing.mp3
sudo curl -v -L -H "Accept: application/octet-stream" -o /usr/share/remindme/remindme_python https://github.com/oDqnger/remindme/releases/download/beta_version/remindme
sudo chmod +x /usr/share/remindme/remindme_python
sudo curl -v -L -H "Accept: application/octet-stream" -o /usr/local/bin/remindme https://github.com/oDqnger/remindme/releases/download/beta_version/remindme_script
sudo chmod +x /usr/local/bin/remindme

echo "Installation completed"
