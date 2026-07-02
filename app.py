from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    result=None
    if request.method=="POST":
        result={"status":"Suspicious","score":42,"threats":["QR code missing","Unknown issuer"]}
    return render_template("index.html",result=result)
if __name__=="__main__":
    app.run(debug=True)
