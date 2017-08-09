from bottle import route, run, template, static_file, get, post, delete, request
# from sys import argv
import json
import pymysql

# pip install mysql

connection = pymysql.connect(host='sql11.freesqldatabase.com',
                             user='sql11189253',
                             password='HttzudApwV',
                             db='sql11189253',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

@get("/admin")
def admin_portal():
    return template("pages/admin.html")

# Create a category
@post("/category")
def create_category(name):
    try:
        with connection.cursor() as cursor:
            name = request.POST.get("name")
            sql_query = "INSERT INTO category (id,name) VALUES (0,{})".format(name)
            cursor.execute(sql_query)
            cursor.commit() #-->only if update database
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS','CAT_ID':id,'CODE':201})

    except Exception:
        return json.dumps({'STATUS':'ERROR','MSG':'INTERNAL ERROR'})

# Delete a category
@delete("/category/<id>")
def delete_category(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE * FROM product WHERE category = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()

            return json.dumps({'STATUS': 'SUCCESS', 'PRODUCTS': result, 'CODE': 200})

    except Exception:
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

# list categories --WORKS
@get("/categories")
def list_category():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM category"
            cursor.execute(sql)
            result = cursor.fetchall()

            return json.dumps({'STATUS': 'SUCCESS', 'CATEGORIES': result, 'CODE': 200})

    except Exception:
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

# list all products --WORKS
@get("/products")
def list_products():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product;"
            cursor.execute(sql)
            result = cursor.fetchall()

            return json.dumps({'STATUS': 'SUCCESS', 'PRODUCTS': result, 'CODE': 200})

    except Exception:
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

# Getting a product--WORKS
@get("/product/<id>")
def get_product(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product WHERE id = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS': 'SUCCESS', 'PRODUCTS': result, 'CODE': 200})

    except Exception as e:
        print (repr(e))
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

# List all products by category--WORKS
@get("/category/<id>/products")
def list_products_by_category(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product WHERE category = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()

            return json.dumps({'STATUS': 'SUCCESS', 'PRODUCTS': result, 'CODE': 200})

    except Exception:
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7030)  # 127.0.0.1 if have another server already running


if __name__ == '__main__':
    main()
