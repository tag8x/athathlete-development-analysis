from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        isim = request.form.get("isim")
        yas = request.form.get("yas")
        cinsiyet = request.form.get("cinsiyet")
        spor_dali = request.form.get("spor_dali")
        pozisyon = request.form.get("pozisyon")
        antrenman_suresi = request.form.get("antrenman_suresi")
        beslenme_duzeni = request.form.get("beslenme_duzeni")
        uyku_aliskanliklari = request.form.get("uyku_aliskanliklari")
        
        # Gelen verileri burada işleyebilir veya kaydedebilirsiniz.
        return f"Veri alındı: {isim}, {yas}, {cinsiyet}, {spor_dali}, {pozisyon}, {antrenman_suresi}, {beslenme_duzeni}, {uyku_aliskanliklari}"
    
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
