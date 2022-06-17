# from email.errors import NoBoundaryInMultipartDefect
from bs4 import Script
from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.jinja_env.filters["zip"] = zip
app.config["SECRET_KEY"] = "iniSecretKeyKu2022"

@app.route("/awal")
def awal():
    # data dalam bentuk dictionary / json
    dataJson = {
        "no": [1, 2, 3, 4, 5],
        "buah": ["apel", "mangga", "semangka", "jeruk", "alpukat"],
        "hewan": ["Kelinci", "Ayam", "Bebek", "Burung", "Sapi"],
    }
    return render_template("awal.html", data = dataJson)

@app.route("/login", methods=["POST", "GET"])
def login():
    # jika tombol button di klik -> request POST
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # jika email dan password benar akan dipindah ke halaman awal
        if email == 'admin@gmail.com' and password == 'pass':
            session['email'] = email
            return redirect(url_for('awal'))
        # jika salah
        else:
            print("Password Salah")
            return redirect(url_for('login'))
            
    return render_template("login.html")

@app.route("/login")
def logout():
    return render_template("login.html")

@app.route("/sukses")
def sukses_req():
    nilai = "Anda berhasil login"
    return render_template("sukses.html", nilai=nilai)

@app.route("/indexkedua")
def indexkedua():
    if "email" in session:
        return render_template("indexkedua.html")
    else:
        return redirect(url_for('login'))

@app.route("/index")
def indexku():
    # return "<h1>Halo Flask-ku !</h1> <br> <h3>Selamat Datang</h3>"
    # memanggil render template
    # nilaiku = 100
    # belajar looping
    hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
    # conditioning / if else
    kegiatan = "bermain"
    # set variable
    return render_template("index.html", value = hari, kegiatan = kegiatan)

@app.route("/contact")
def contactku():
    return render_template("contact.html")

@app.route("/about")
def aboutku():
    return render_template("about.html")

# parsing nilai int, string
@app.route("/parsing/<int:nilaiku>") #bisa integer atau string
def ayo_parsing(nilaiku):
    return "nilainya adalah : {}".format(nilaiku)

#argumen parser
@app.route("/parsingargument")
def ayo_argument():
    data = request.args.get("nilai")
    return "nilai dari argumen parser adalah : {}".format(data)

# memparsing nilai dari url untuk mengset nilai session
@app.route("/halaman/<int:nilai>")
def session_1(nilai):
    session["nilaiku"] = nilai
    return "Berhasil mengeset nilainya"

@app.route("/halaman/lihat")
def view_session_1():
    try: # try except mirip dengan if else
        data = session["nilaiku"]
        return "nilai yang telah diset adalah : {}".format(data)
    except:
        return "Anda tidak memiliki nilai session lagi"
# logout (menghapus nilai variabel dari session, agar tidak bisa diakses)
@app.route("/halaman/logout")
def logout_session_1():
    session.pop("nilaiku")
    return "Berhasil logout / menghapus session"
""""
REDIRECT
"""
@app.route("/redirect-index")
def ayo_redirect_indexku():
    return redirect(url_for("indexku"))
@app.route("/redirect-indexkedua")
def ayo_redirect_indexkedua():
    return redirect(url_for("indexkedua"))
@app.route("/redirect-contact")
def ayo_redirect_contactku():
    return redirect(url_for("contactku"))
@app.route("/redirect-about")
def ayo_redirect_aboutku():
    return redirect(url_for("aboutku"))
""""
/REDIRECT
"""

if __name__ == '__main__':
    app.run(debug=True, port=5001) # port=x adalah untuk mengganti port