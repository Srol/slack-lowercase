from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

@app.route("/request", methods = ['POST'])
def grab():
	if request.method == "POST" and request.form.get('token') == "Add slash command token here. ":
		text = request.form.get('text')
		text = text.capitalize()
		if "**" in text:
			takeApart = text.split(' ')
			backTogether = []
			for word in takeApart:
				if "**" in word:
					word = str(word).translate(None, "*")
					word = word.title()
				backTogether.append(word)
			text = " ".join(backTogether)
		payload = {"response_type": "in_channel","text": "Here is your lowercased text", "attachments": [{"text":text}]}
		return jsonify(payload)
	else:
		return "Something went wrong."