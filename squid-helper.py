#!/usr/bin/python3

from pymongo import MongoClient
import sys
import socket
import logging

logging.basicConfig(filename='/var/log/squid/auth.log', level=logging.DEBUG)

db = MongoClient("mongodb://localhost:27017/")
users = db.server.users

"""USAGE:The function returns True if the user and passwd match False otherwise"""
def matchpasswd(login,passwd):
    # Write your own function definition.
    # Use mysql, files, /etc/passwd or some service or whatever you want
    results = users.find_one({"username": login})
    if results:
        if password == results['password']:
            logging.debug('Password correct for %s' % login)
            return True
        else:
            logging.debug('Password incorrect for %s' % login)
            return False
    else:
        return False

while True:
    logging.debug('Squid Helper Started, waiting for input from STDIN...')
    # read a line from stdin
    line = sys.stdin.readline()
    logging.debug('Received STDIN: %s' % line)
    line = line.split()
    # extract username and password from line
    username = line[0]
    password = line[1]

    if matchpasswd(username, password):
        sys.stdout.write('OK\n')
        logging.debug('Sent STDOUT: OK')
    else:
        sys.stdout.write('ERR\n')
        logging.debug('Sent STDOUT: ERR')
    # Flush the output to stdout.
    sys.stdout.flush()
