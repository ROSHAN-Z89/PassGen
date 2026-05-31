from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

lower_alpha = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
upper_alpha = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
sp_char = list('!@#$%^&*()_-+={},[]|\\:;\'\"<>?/')

def passgen(length, use_upper=True, use_numbers=True, use_special=True):
    all_chars = lower_alpha.split(',')
    if use_upper:
        all_chars += upper_alpha.split(',')
    if use_numbers:
        all_chars += list('0123456789')
    if use_special:
        all_chars += sp_char

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = int(data.get('length', 12))
    use_upper = data.get('use_upper', True)
    use_numbers = data.get('use_numbers', True)
    use_special = data.get('use_special', True)

    if length < 4 or length > 128:
        return jsonify({'error': 'Length must be between 4 and 128'}), 400

    password = passgen(length, use_upper, use_numbers, use_special)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
