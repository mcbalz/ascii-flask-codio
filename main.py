from flask import Flask, render_template, request
from ascii_art import create_ascii

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('input.html')

@app.route('/ascii', methods=['POST'])
def ascii():
  url = request.form['url']
  img = create_ascii(url)
  if type(img) == list:
    resp = {'valid': True, 'img': img}
  else:
    resp = {'valid': False, 'img': img}
  return render_template('art.html', ascii = resp)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000, debug=True)
