#!/bin/bash
/usr/bin/socat -T1 -u UDP-RECVFROM:8125,reuseaddr,fork UDP:127.0.0.1:9125
