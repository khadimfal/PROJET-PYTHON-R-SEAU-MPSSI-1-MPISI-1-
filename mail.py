#!/usr/bin python3
import os
import sys
import time

time_exec = int(sys.argv[1])

my_dir = os.path.dirname(sys.argv[0])
os.system('%s %s' % (sys.executable, 
                        os.path.join(my_dir, f'Analyseur.py {time_exec} > log.txt')))

os.system('mail -s "rapport analyse de paquets" -A log.txt postmaster@redmail.com < log.txt' )



