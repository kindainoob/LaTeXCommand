#coding:utf-8
import subprocess

filename = input ("作成するレポート名を入力してください：")
lesson_name = input("授業名を入力してください：")
lesson_number = input("授業の回数を入力してください：")
title = input("レポートのタイトルを入力してください：")
number = input("学籍番号を入力してください：")
name = input("名前を入力してください：")
filename += '.tex'


template = """
\\documentclass{jsarticle}

\\begin{document}
\\title{%(title)s}
\\author{学籍番号：%(number)s\\\\氏名：%(name)s}
\\date{提出日：\\today}
\\maketitle

\\end{document}

"""%locals()


f = open(filename,'w')
f.write(template)
