from flask import Flask, render_template, url_for, request, redirect
import os

def katalog():
    return render_template('katalog.html')

def str2():
    return render_template('str2.html')

folder = os.getcwd()

app=Flask(__name__, template_folder=folder, static_folder=folder)

app.add_url_rule('/', 'katalog', katalog) # methods = ["post", 'get'])

#app.add_url_rule('/', 'str2', str2) # methods = ["post", 'get'])



app.run()