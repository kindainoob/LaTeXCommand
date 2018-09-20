#coding:utf-8
import subprocess
import sys
args = sys.argv

file = args[1]

cut_file = file.split('.')
platex = 'platex ' + cut_file[0] + '.tex'
dvipdfmx = 'dvipdfmx ' + cut_file[0] + '.dvi'
clean = 'rm '+ cut_file[0] +'.dvi '+ cut_file[0] +'.log '+ cut_file[0] +'.aux'

subprocess.call(platex.split())
subprocess.call(platex.split())
subprocess.call(dvipdfmx.split())
subprocess.call(clean.split())
