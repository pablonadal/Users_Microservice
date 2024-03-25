from app import createapp

app = createapp()

app.appcontext().push()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)