from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# write a function that will show a page with a form on it
# the index route will handle rendering the HTML form

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got the POST info")
    print(request.form)
    # Never render a template on a POST request.
    # To avoid this, redirect to the index route.
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
