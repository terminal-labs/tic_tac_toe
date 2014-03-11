#!/bin/bash
sudo apt-get update;
sudo apt-get dist-upgrade;

sudo apt-get install build-essential;
sudo apt-get install python-dev;
sudo apt-get install python-pip;
sudo apt-get install python-virtualenv;
sudo apt-get install nginx;
sudo apt-get install emacs;
sudo apt-get install git;

virtualenv ENV;
ENV/bin/pip install django;
ENV/bin/pip install uwsgi;
