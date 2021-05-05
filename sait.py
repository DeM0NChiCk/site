from flask import Flask, render_template, url_for, request, redirect
import os

def katalog():
    return render_template('katalog.html')
    

name = ''
price = ''
opisanie = ''

def str1():
    name = ''
    price = ''
    opisanie = ''
    if request.url.endswith('id1'):
        name = 'dress1'
        price='30000'
        opisanie = 'Da da'
    return render_template('str1.html', name = name, price = price, opisanie= opisanie)
def str2():
    name = ''
    price = ''
    opisanie = ''
    if request.url.endswith('id2'):
        name = 'dress2'
        price='40000'
        opisanie = 'Da da'
    return render_template('str2.html', name = name, price = price, opisanie= opisanie)
def str3():
    name = ''
    price = ''
    opisanie = ''
    if request.url.endswith('id3'):
        name = 'dress1'
        price='45000'
        opisanie = 'Da da'
    return render_template('str3.html', name = name, price = price, opisanie= opisanie)
def str4():
    name = ''
    price = ''
    opisanie = ''
    if request.url.endswith('id4'):
        name = 'dress1'
        price='30000'
        opisanie = 'Da da'
    return render_template('str4.html', name = name, price = price, opisanie= opisanie)
def str5():
    name = ''
    price = ''
    opisanie = ''
    if request.url.endswith('id5'):
        name = 'dress1'
        price='30000'
        opisanie = 'Da da'
    return render_template('str5.html', name = name, price = price, opisanie= opisanie)
def str6():
    name = ''
    price = ''
    opisanie = ''
    if request.url.endswith('id6'):
        name = 'dress1'
        price='30000'
        opisanie = 'Da da'
    return render_template('str6.html', name = name, price = price, opisanie= opisanie)

folder = os.getcwd()

app=Flask(__name__, template_folder=folder, static_folder=folder)

app.add_url_rule('/', 'katalog', katalog, methods = ["post", 'get'])

app.add_url_rule('/str1', 'str1', str1, methods = ["post", 'get'])
app.add_url_rule('/str2', 'str2', str2, methods = ["post", 'get'])
app.add_url_rule('/str3', 'str3', str3, methods = ["post", 'get'])
app.add_url_rule('/str4', 'str4', str4, methods = ["post", 'get'])
app.add_url_rule('/str5', 'str5', str5, methods = ["post", 'get'])
app.add_url_rule('/str6', 'str6', str6, methods = ["post", 'get'])

app.run()