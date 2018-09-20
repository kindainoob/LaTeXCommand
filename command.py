#coding:utf-8
import subprocess
import sys
args = sys.argv
# 引数を変数に取得
file = args[1]
# 拡張子を切り捨て
cut_file = file.split('.')
# 各，拡張子をつける
platex = 'platex ' + cut_file[0] + '.tex'
dvipdfmx = 'dvipdfmx ' + cut_file[0] + '.dvi'
# ログファイルの削除
clean = 'rm '+ cut_file[0] +'.dvi '+ cut_file[0] +'.log '+ cut_file[0] +'.aux'
# 実行
subprocess.call(platex.split())
subprocess.call(platex.split())
subprocess.call(dvipdfmx.split())
subprocess.call(clean.split())
