# coding:utf-8
import subprocess
import sys
args = sys.argv

file = args[1]
cmd = 'pwd'
wd = (subprocess.Popen(cmd, stdout=subprocess.PIPE,
                           shell=True).communicate()[0]).decode('utf-8')
file = args[1]
platex = 'platex ' + file
dvipdfmx = 'dvipdfmx ' + file
clean = 'rm *.log *.aux *.dvi'

cmd = 'cp ' + wd + file + ' ./'
subprocess.call(platex.split())
subprocess.call(platex.split())
subprocess.call(dvipdfmx.split())
subprocess.call(clean.split())
