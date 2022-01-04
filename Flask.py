from flask import Flask, request, jsonify
from werkzeug.utils import redirect
import json

app = Flask(__name__)

@app.route("/")
def a():
	return redirect("/data")

@app.route("/<name>")
def b(name):
	return '<h1>Gor, %s</h1>' % (name)

@app.route("/baidu")
def baidu():
	return redirect("https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20190109%2F0d90a00746124a93974ae89916d8d6cf.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1642742815&t=b2e9a0b2ce56cf42ce448a2eb8c2eda4")	

@app.route("/Matt")
def test():
	return redirect("https://pic1.zhimg.com/80/v2-87d2938ef4f6e5229da0a1767ba76db5_1440w.png")	

@app.route("/data", methods=["POST"])
def data():
	info = request.get_json()
	get_id = info.get("id")
	get_infection = info.get("infection")
	get_contactNum = info.get("contactNum")
	if (get_contactNum >= 3):
		return jsonify(id=get_id, contactNum=get_contactNum, infection="Danger")
	else:
		return jsonify(id=get_id, contactNum=get_contactNum, infection="Nope")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)