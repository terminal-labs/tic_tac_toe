#!/bin/bash
sudo ln -s ~/tic_tac_toe_verhulst/nginx.conf /etc/nginx/sites-enabled/;
sudo /etc/init.d/nginx start;
