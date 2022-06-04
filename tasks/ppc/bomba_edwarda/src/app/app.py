# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, session, redirect, url_for
import db_controller as db
import random, json

app = Flask(__name__)
GOAL = 300
wire_colors = ['red', 'white', 'blue', 'yellow', 'black']
app.config['SECRET_KEY'] = '89dyfgudsihg7aerguy764gfoeah7gfo'


class Bomb:
    def __init__(self, wires=None, serial=None):
        if wires is None:
            number_of_wires = random.randint(3, 6)
            self.wires = [wire_colors[random.randint(0, 4)] for i in range(number_of_wires)]
        else:
            self.wires = wires
        if serial is None:
            self.serial = serial_num_gen()
        else:
            self.serial = serial
        self.defuse_wire = defuser(self.wires, self.serial)

    def is_defused(self, wire):
        return self.defuse_wire == wire

    def __repr__(self):
        return self.wires, self.serial

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=2)


def defuser(wires, serial):
    number_of_wires = len(wires)
    if number_of_wires == 3:
        if 'red' not in wires:
            return 1
        elif wires[2] == 'white':
            return 2
        elif wires.count('blue') > 1:
            blues = [i for i, x in enumerate(wires) if x == 'blue']
            return blues[-1]
        else:
            return 2

    elif number_of_wires == 4:
        if wires.count('red') > 1 and int(serial[5])%2 == 1:
            reds = [i for i, x in enumerate(wires) if x == 'red']
            return reds[-1]
        elif wires[3] == 'yellow' and 'red' not in wires:
            return 0
        elif wires.count('blue') == 1:
            return 0
        elif wires.count('yellow') > 1:
            return 3
        else:
            return 1

    elif number_of_wires == 5:
        if wires[4] == 'black' and int(serial[5])%2 == 1:
            return 3
        elif wires.count('red') == 1 and wires.count('yellow') > 1:
            return 0
        elif 'black' not in wires:
            return 1
        else:
            return 0

    elif number_of_wires == 6:
        if 'yellow' not in wires and int(serial[5])%2 == 1:
            return 2
        elif wires.count('yellow') == 1 and wires.count('white') > 1:
            return 3
        elif 'red' not in wires:
            return 5
        else:
            return 3


def serial_num_gen():
    num = []
    for ch in range(5):
        num.append(chr(random.choice([random.randint(65, 78), random.randint(80, 90), random.randint(48, 57)])))
    num.append(str(random.randint(0, 9)))
    return ''.join(num)


@app.route('/')
@app.route('/index')
def index():
    if 'token' in session:
        user = db.get_user(session.get('token'))
        if user is None:
            user = db.create_user()
    else:
        user = db.create_user()
    session['token'] = user.token
    return render_template('index.html', user=user)


@app.route('/bomb', methods=["GET", "POST"])
def bomb():
    if 'token' in session:
        user = db.get_user(session.get('token'))
        if user is not None:
            if user.progress != GOAL:
                task_solved = False
                is_defused = None
                if request.method == "POST":
                    curr_bomb = json.loads(session.get('bomb'))
                    curr_bomb = Bomb(curr_bomb['wires'], curr_bomb['serial'])
                    form = request.form
                    wire = int(form.get("wire"))
                    is_defused = curr_bomb.is_defused(wire)
                    print(wire, curr_bomb.wires)
                    if is_defused:
                        db.count_defuse(user)
                    else:
                        db.reset_progress(user)
                curr_bomb = Bomb()
                session['bomb'] = curr_bomb.toJSON()
            else:
                curr_bomb = Bomb()
                is_defused = True
                task_solved = True
            return render_template('bomb.html', wires=curr_bomb.wires, serial=curr_bomb.serial, is_defused=is_defused, user=user, task_solved=task_solved)
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1999)
