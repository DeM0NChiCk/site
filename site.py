from flask import Flask, render_template, url_for, request, redirect
import os

app = Flask(__name__)
app.add_url_rule('/', 'index', index)
app.run