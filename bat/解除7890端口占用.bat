net stop winnat
netsh int ipv4 add excludedportrange protocol=tcp startport=7890 numberofports=4
net start winnat