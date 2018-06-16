from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/hello")
def index():
	name = request.args.get('name', 'Nobody')
	
	if name:
		greeting = f"Hello, {name}"
	else:
		greeting = "Hello World"
		
	return render_template("index.html", greeting = greeting)
	
if __name__=='__main__':
	app.run()