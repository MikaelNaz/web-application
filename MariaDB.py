import mariadb
import sys
from flask import Flask, render_template, request, url_for, flash, redirect


try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3312,
        database="db_flower"
    )
    cursor = conn.cursor()

    app = Flask(__name__)


    @app.route("/")
    def home():
       return render_template("home.html")

    @app.route("/goods")
    def goods():
        cursor.execute("SELECT * FROM goods")
        value = cursor.fetchall()
        return render_template('goods.html', data=value, name='goods' )

    @app.route("/staff")
    def staff():
        cursor.execute("SELECT * FROM staff")
        value = cursor.fetchall()
        return render_template('staff.html', data=value, name='staff')


    @app.route("/procedure")
    def procedure():
        cursor.execute("CALL Procent44()")
        value = cursor.fetchall()
        return render_template('procedure.html', data=value, name='staff')

    @app.route("/orders", methods=('GET', 'POST'))
    def orders():
        flower_id = request.form.get('flower_id')
        sale_date = request.form.get('sale_date')
        sale_price = request.form.get('sale_price')
        employee_id = request.form.get('employee_id')
        print(flower_id, sale_date, sale_price, employee_id)
        try:
            cursor.execute("INSERT INTO orders (flower_id,sale_date, sale_price, employee_id) VALUES (?, ?, ?, ?)", (flower_id, sale_date, sale_price, employee_id))
            conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")
        return render_template('orders.html')




    if __name__ == "__main__":
       app.run()



except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

finally:
    conn.close()
    print('f')




