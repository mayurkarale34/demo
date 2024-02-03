
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_user', methods=['POST'])
def register_user():
    try:
        connection = app._engine.connect()
        transaction = connection.begin()

        request_data = dict(request.form)
        insert_query = f"insert into user_master(first_name, last_name, city_name, blood_group) values('{request_data['first_name']}', '{request_data['last_name']}', '{request_data['city_name']}', '{request_data['blood_group']}')"

        connection.execute(text(insert_query))

        transaction.commit()
        connection.close()

        return redirect('/')
    except Exception as e:
        transaction.rollback()
        connection.close()
        print(str(e))
        return redirect('/')