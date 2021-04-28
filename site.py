from flask import Flask, render_template, url_for, request, redirect
import os

def katalog():
    
    return render_template('katalog.html')

def str2():
    name = ''
    imgname = ''
    price = ''
    opisanie = ''
    if request.url.endswith('id1'):
        imgname = 'https://raw.githubusercontent.com/DeM0NChiCk/site/main/dress.jpg?token=ATSNQYX2CGJN6ANRWOSM5BTARGIIO'
        name = 'dress1'
        price='30000'
        opisanie = 'Da da'
    if request.url.endswith('id2'):
        imgname = 'https://drive.google.com/file/d/1DbOs01BDNeGKC6y-XbOEZ33t_iefmIb0/view?usp=sharing'
        name = 'dress2'
        price='40000'
        opisanie = 'Da da'
    if request.url.endswith('id3'):
        imgname = 'https://drive.google.com/file/d/1d34jcP_lHkKSb5B1j8fW4NedWCJQHdi2/view?usp=sharing'
        name = 'dress1'
        price='45000'
        opisanie = 'Da da'
    if request.url.endswith('id4'):
        imgname = 'https://drive.google.com/file/d/16AuKe71OKRRQZcuE28WMkZ9AlG_pV94U/view?usp=sharing'
        name = 'dress1'
        price='30000'
        opisanie = 'Da da'
    if request.url.endswith('id5'):
        imgname = 'https://drive.google.com/file/d/1Qmxg48gue8_mCi6LfK-5N5Gp-8cNtctB/view?usp=sharing'
        name = 'dress1'
        price='30000'
        opisanie = 'Da da'
    if request.url.endswith('id6'):
        imgname = 'https://drive.google.com/file/d/1whxCORnrcqFnEfVWZ1z_Se__wZkBFrJn/view?usp=sharing'
        name = 'dress1'
        price='30000'
        opisanie = 'Da da'

    return render_template('str2.html', name = name, image = imgname, price = price, opisanie= opisanie)

folder = os.getcwd()

app=Flask(__name__, template_folder=folder, static_folder=folder)

app.add_url_rule('/', 'katalog', katalog, methods = ["post", 'get'])

app.add_url_rule('/str2', 'str2', str2, methods = ["post", 'get'])



app.run()