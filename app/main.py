from app import init_db
# from website import init_db


app = init_db()
#init_db()

if __name__ == '__main__':
    app.run(debug=True)