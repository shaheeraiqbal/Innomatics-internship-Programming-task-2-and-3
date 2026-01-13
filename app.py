from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    # Get 'name' from query parameter
    name = request.args.get("name", "")
    
    # Convert to uppercase
    upper_name = name.upper()
    
    return render_template("index.html", name=upper_name)

if __name__ == "__main__":
    app.run(debug=True)
