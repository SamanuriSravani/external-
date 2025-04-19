from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Just printing to console to simulate server-side handling
    print("Form submitted!")
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
