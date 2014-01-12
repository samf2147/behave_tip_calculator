from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/results', methods=['POST'])
def results():
    meal_cost = float(request.form['meal_cost'])
    tip_percentage = float(request.form['tip_percentage'])
    if(meal_cost < 0 or tip_percentage < 0):
        return render_template('error.html')
    else:
		tip = 0.01 * meal_cost * tip_percentage
		return render_template('results.html', tip='${0:.2f}'.format(tip))

if __name__ == '__main__':
    app.run(debug=True)

