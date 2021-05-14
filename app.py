from flask import Flask, request, render_template
from random import choice
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story
from lists import *
from nav import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "some_key"
debug = DebugToolbarExtension(app)

nav_bar = Nav.get_nav()

@app.route('/')
def home():
    inputs = choice(questions)
    index_story = questions.index(inputs)
    return render_template("home.html", nav_bar = nav_bar, inputs = inputs, index = index_story)

@app.route('/<path>')
def general(path):
    return eval(path)()
    


def story():
    try:
        args_form ={key: request.args[key] for key in request.args.keys()}

        story_text = "".join(stories[int(args_form['index'])])
        del args_form['index']

        story_obj = Story(args_form, story_text)
        story = story_obj.generate(args_form)

        return render_template("story.html", nav_bar = nav_bar, story = story)
    except:
        return render_template("story.html", nav_bar = nav_bar, story = "There is no a story here")



