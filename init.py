import os
import sys
import flask
import _thread

firstOpen = None
webapp = flask.Flask('VisualASM - WebAPP')



@webapp.route('/')
def index():
    return {'code':200}

@webapp.route('/api/v1/fristopen')
def ifFristOpen():
    return {'code':200,'result':firstOpen}


def main():
    global firstOpen
    try:
        with open('fristopen','r') as f:
            f = f
            firstOpen = False
    except FileNotFoundError:
        firstOpen = True
        with open('fristopen','w') as f:
            f.write('200')
    webapp.run(port=2333,host='0.0.0.0')

if __name__ == '__main__':
    _thread.start_new(main, ())
    os.system('python main.py')