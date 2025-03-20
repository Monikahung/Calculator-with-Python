from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".")

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = ""

    if request.method == "POST":
        try:
            angka1 = float(request.form["angka1"])
            angka2 = float(request.form["angka2"])
            operasi = request.form["operasi"]

            if operasi == "tambah":
                hasil = angka1 + angka2
            elif operasi == "kurang":
                hasil = angka1 - angka2
            elif operasi == "kali":
                hasil = angka1 * angka2
            elif operasi == "bagi":
                hasil = angka1 / angka2 if angka2 != 0 else "Error: Bagi 0"

        except:
            hasil = "Error"

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True, port=7000)