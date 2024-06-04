from flask import Flask, render_template ,request, jsonify
from nlp import ROBO
import csv

app = Flask(__name__)

@app.route('/')
def charts():
    return render_template('charts.html')



@app.route('/datatables' , endpoint = 'datatables_net')
def index():
    data = []
    with open('/home/maaz/Desktop/PAI_Project/csv/new_data.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return render_template('datatables.html', data=data)







@app.route('/chatbot')
def chatbot():
    data = []
    with open('/home/maaz/Desktop/PAI_Project/i221388_AI_C/data.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return render_template('chatbot.html', data=data)

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    user_input = data.get('input', '')
    ROBO(user_input )
    
    return render_template('chatbot.html')





if __name__ == '__main__':
    app.run(debug=True)
