from flask import *

# configure app
app = Flask(__name__)

flag_option = '__utflag__'
flag = 'utflag{verbose_errors_make_senpai_sad}'
options = ['Broccoli 🥦', 'Eggplant 🍆', 'Garlic 🧄', flag_option]

@app.route('/veg', methods=['POST'])
def process_vote():
    veg = request.form.get('veg')
    if veg:
        if veg == flag_option:
            isAdmin = request.form.get('isAdmin')
            print(isAdmin)
            if isAdmin == 'True' or isAdmin == 'true' or isAdmin == '1':
                return redirect(url_for('index', favVeg=flag))
            else:
                return redirect(url_for('index', 
                    favVeg='AttributeError: \'NoneType\' field \'isAdmin\' has no attribute \'isTrue\''))
        return redirect(url_for('index', favVeg=veg))
    else:
        return redirect(url_for('index'))

@app.route('/', methods=['GET'])
def index(favVeg=None):
    favVeg = request.args.get('favVeg')
    if favVeg:
        # Flask doesn't play nice with emojis, so gotta do some extra work here.
        for option in options:
            if option.startswith(favVeg):
                return render_template('index.html', options=options, favVeg=option)
            return render_template('index.html', options=options, favVeg=favVeg)
    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
