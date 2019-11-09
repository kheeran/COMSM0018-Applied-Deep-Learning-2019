#!/bin/bash

Port="57986"
Hostname="gpu01"

ssh -N -L 6006:$Hostname:$Port kn16063@bc4login.acrc.bris.ac.uk
