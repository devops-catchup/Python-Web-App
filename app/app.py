
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        name = request.form['name']
        method = request.form['payment']
        coupon = request.form['coupon']
        return redirect(url_for('thankyou', name=name, method=method, coupon=coupon))
    return render_template('payment.html')

@app.route('/thankyou')
def thankyou():
    name = request.args.get('name')
    method = request.args.get('method')
    coupon = request.args.get('coupon')
    return render_template('thankyou.html', name=name, method=method, coupon=coupon)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(host="0.0.0.0", port=port)
