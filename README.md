# easydns-ddns-updater
A tiny Docker container to update easyDNS A records

To build this it is first necessary to run a version of alpine:python, then install request and dnspython.
docker run --name python --privileged -it python:alpine sh
pip install request
pip install dnspython
exit
docker commit <container ID> python:ddns


