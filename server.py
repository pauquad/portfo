from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)  # instance of Flask app, name: __main__


@app.route("/")  # decorator for everytime we hit a route or slash
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:  # mode append
#         email = data['email']
#         subject = data['subjct']
#         message = data['message']
#         file = database.write(f'\n{email},{subject},{message}')  # write data

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:  # mode append
        email = data.get('email', '')
        subject = data.get('subject', '')
        message = data.get('message', '')
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # get everything as a dict
            write_to_csv(data)  # send data to function
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'Something went wrong. Try again.'
