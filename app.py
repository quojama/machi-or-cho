import json
import random

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "YOUR_SECRET_KEY"  # セッション機能を使う場合に必須（任意の文字列に変更してください）

# JSONデータ読み込み
with open("quiz_data.json", "r", encoding="utf-8") as f:
    original_quiz_data = json.load(f)

@app.route("/")
def index():
    # クイズをシャッフルしたコピーを作り、セッションに保存
    quiz_data_shuffled = original_quiz_data[:]  # シャローコピー
    random.shuffle(quiz_data_shuffled)
    session["quiz_data"] = quiz_data_shuffled

    return render_template("index.html", quiz_data=quiz_data_shuffled)

@app.route("/submit", methods=["POST"])
def submit():
    # セッションに保存したクイズ順序を取得
    quiz_data_shuffled = session.get("quiz_data", [])

    # 採点
    score = 0
    for i, quiz in enumerate(quiz_data_shuffled):
        user_choice = request.form.get(f"q_{i}")
        if user_choice == quiz["answer_section"]:
            score += 2  # 1問あたり2点

    return render_template("result.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)
