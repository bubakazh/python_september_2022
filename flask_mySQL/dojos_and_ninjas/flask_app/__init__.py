
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.secret_key = "shizukani"

DATABASE = "dojos_and_ninjas"