from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    b1_depo=1005298673
    b2_depo=193250138
    b3_depo=240947552
    b4_depo=247629636

    b1_cair=993235088
    b2_cair=190931136
    b3_cair=238056181
    b4_cair=244658080

    b1_tampung=993088088
    b2_tampung=190907136
    b3_tampung=238026181
    b4_tampung=244622080

    b1_tf=147000
    b2_tf=24000
    b3_tf=30000
    b4_tf=36000

    return render_template(
        "index.html",
        b1_depo=f"{b1_depo:,}",
        b2_depo=f"{b2_depo:,}",
        b3_depo=f"{b3_depo:,}",
        b4_depo=f"{b4_depo:,}",
        total_depo=f"{b1_depo+b2_depo+b3_depo+b4_depo:,}",

        b1_cair=f"{b1_cair:,}",
        b2_cair=f"{b2_cair:,}",
        b3_cair=f"{b3_cair:,}",
        b4_cair=f"{b4_cair:,}",
        total_cair=f"{b1_cair+b2_cair+b3_cair+b4_cair:,}",

        b1_tampung=f"{b1_tampung:,}",
        b2_tampung=f"{b2_tampung:,}",
        b3_tampung=f"{b3_tampung:,}",
        b4_tampung=f"{b4_tampung:,}",
        total_tampung=f"{b1_tampung+b2_tampung+b3_tampung+b4_tampung:,}",

        b1_tf=f"{b1_tf:,}",
        b2_tf=f"{b2_tf:,}",
        b3_tf=f"{b3_tf:,}",
        b4_tf=f"{b4_tf:,}",
        total_tf=f"{b1_tf+b2_tf+b3_tf+b4_tf:,}"
    )

app.run(debug=True)
