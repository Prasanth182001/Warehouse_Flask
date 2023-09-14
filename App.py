from flask import Flask,render_template,url_for,request,flash,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

# Database connection

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Prasanth@182001"
app.config["MYSQL_DB"]="inventory"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
sql=MySQL(app)



@app.route("/")
def products():
    connect=sql.connection.cursor()
    connect.execute("select * from products")
    result=connect.fetchall()
    return render_template("products.html",data=result)



@app.route("/add_p",methods=['POST','GET'])
def add_product():
    if request.method=="POST" and request.form['a_product'] and request.form['a_quantity']:
        try:
            product=request.form['a_product']
            quantity=request.form['a_quantity']

            connect=sql.connection.cursor()
            connect.execute("insert into products (P_NAME,QUANTITY) value (%s,%s)",[product,quantity])
            sql.connection.commit()
            connect.close()
            flash("Product added successfully")
        except:
            flash("Error in insert opration")
        finally:
            return redirect(url_for('products'))
    return render_template("add_product.html")



@app.route("/edit_p/<string:id>",methods=['POST','GET'])
def edit_product(id):
    if request.method=='POST' and request.form['e_product'] and request.form['e_quantity']:
        try:
            product=request.form['e_product']
            quantity=request.form['e_quantity']
            connect=sql.connection.cursor()
            connect.execute("update products set P_NAME=%s,QUANTITY=%s where ID=%s",[product,quantity,id])
            sql.connection.commit()
            connect.close()
            flash("Product detailes updated..")
        except:
            flash("Error in update opration..")
        finally:
            return redirect(url_for("products"))
    connect=sql.connection.cursor()
    connect.execute("select * from products where ID=%s",[id])
    result=connect.fetchone()
    return render_template("edit_product.html", e_data=result)



@app.route("/delete_p/<string:id>",methods=['POST','GET'])
def delete_product(id):
    connect=sql.connection.cursor()
    connect.execute("delete from products where ID=%s",[id])
    sql.connection.commit()
    connect.close()
    flash("Product detailes deleted..")
    return redirect(url_for('products'))



@app.route("/location")
def locations():
    connect=sql.connection.cursor()
    connect.execute("select * from locations")
    result=connect.fetchall()
    return render_template("location.html",data_l=result)



@app.route("/add_l",methods=['POST','GET'])
def add_location():
    if request.method=="POST" and request.form['a_location'] :
        try:
            location=request.form['a_location']

            connect=sql.connection.cursor()
            connect.execute("insert into locations (LOCATIONS) value (%s)",[location])
            sql.connection.commit()
            connect.close()
            flash("location added successfully")
        except:
            flash("Error in insert opration")
        finally:
            return redirect(url_for('locations'))

    return render_template("add_location.html")



@app.route('/edit_l/<string:id>',methods=['POST','GET'])
def edit_location(id):
    if request.method=='POST' and request.form['e_location']:
        try:
            location=request.form['e_location']
            connect=sql.connection.cursor()
            connect.execute("update locations set LOCATIONS=%s where ID=%s",[location,id])
            sql.connection.commit()
            connect.close()
            flash("Locations updated successfully..")
        except:
            flash("Error in update opration..")
        finally:
            return redirect(url_for("locations"))
    connect=sql.connection.cursor()
    connect.execute("select * from locations where Id=%s",[id])
    result=connect.fetchone()
    return render_template("edit_location.html",l_data=result)



@app.route('/delete_l/<string:id>',methods=['POST','GET'])
def delete_location(id):
    connect=sql.connection.cursor()
    connect.execute("delete from locations where ID=%s",[id])
    sql.connection.commit()
    connect.close()
    flash("Location deleted successfully..")
    return redirect(url_for("locations"))



@app.route("/transfer")
def transfer():
    connect=sql.connection.cursor()
    connect.execute("select * from transfers")
    result=connect.fetchall()
    return render_template("transfer.html",t_data=result)



@app.route("/add_t",methods=['POST','GET'])
def add_transfer():
    if request.method=='POST' and request.form['a_from'] and request.form['a_to'] and request.form['a_pro'] and request.form['a_qty'] and request.form['a_time']:
        try:
          from_l=request.form['a_from']
          to_l=request.form['a_to']
          pdt=request.form['a_pro']
          qty=request.form['a_qty']
          time=request.form['a_time']

          connect=sql.connection.cursor()
          connect.execute("insert into transfers (FROM_L,TO_L,PRODUCT,QUANTITY,TIMESTAMP) value (%s,%s,%s,%s,%s)",[from_l,to_l,pdt,qty,time])
          sql.connection.commit()
          connect.close()
          flash("Transfer added succcessfully..")
        except:
            flash("Error in insert opration...")
        finally:
            return redirect(url_for("transfer"))

    connect=sql.connection.cursor()
    connect.execute("select * from products")
    result=connect.fetchall()
    connect_ = sql.connection.cursor()
    connect_.execute("select * from locations")
    result_ = connect_.fetchall()
    return render_template("add_transfer.html",datas=result,dt=result_)



@app.route("/edit_t<string:id>",methods=['POST','GET'])
def edit_transfer(id):
    if request.method=="POST" and request.form['e_from'] and request.form['e_to'] and request.form['e_pro'] and request.form['e_qty'] and request.form['e_time']:
        try:
            from_l = request.form['e_from']
            to_l = request.form['e_to']
            pdt = request.form['e_pro']
            qty = request.form['e_qty']
            time = request.form['e_time']
            connect=sql.connection.cursor()
            connect.execute("update transfers set FROM_L=%s,TO_L=%s,PRODUCT=%s,QUANTITY=%s,TIMESTAMP=%s",[from_l,to_l,pdt,qty,time])
            sql.connection.commit()
            connect.close()
            flash("Transfer updated successfully...")
        except:
            flash("Error in update opration...")
        finally:
            return redirect(url_for("transfer"))

    connect=sql.connection.cursor()
    connect.execute("select * from transfers where ID=%s",[id])
    result=connect.fetchone()
    return render_template("edit_transfer.html",data_t=result)



@app.route('/delete_t/<string:id>',methods=['POST','GET'])
def delete_transfer(id):
    connect=sql.connection.cursor()
    connect.execute("delete from transfers where ID=%s",[id])
    sql.connection.commit()
    connect.close()
    flash("transfer deleted successfully..")
    return redirect(url_for("transfer"))



if __name__ == '__main__':
    app.secret_key="abcd123"
    app.run(debug=True)