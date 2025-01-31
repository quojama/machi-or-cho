from flask import Flask, render_template_string, request

app = Flask(__name__)

quiz_data = [
    {"station_name": "淡路町",     "select_A": "あわじまち",       "select_B": "あわじちょう",     "answer_section": "select_B", "answer": "あわじちょう"},
    {"station_name": "板橋本町",   "select_A": "いたばしほんまち", "select_B": "いたばしほんちょう", "answer_section": "select_B", "answer": "いたばしほんちょう"},
    {"station_name": "稲荷町",     "select_A": "いなりまち",       "select_B": "いなりちょう",     "answer_section": "select_B", "answer": "いなりちょう"},
    {"station_name": "岩本町",     "select_A": "いわもとまち",     "select_B": "いわもとちょう",   "answer_section": "select_B", "answer": "いわもとちょう"},
    {"station_name": "上野御徒町", "select_A": "うえのおかちまち", "select_B": "かみおかちちょう", "answer_section": "select_A", "answer": "うえのおかちまち"},
    {"station_name": "牛込柳町",   "select_A": "うしごめやなぎまち", "select_B": "うしごめやなぎちょう", "answer_section": "select_B", "answer": "うしごめやなぎちょう"},
    {"station_name": "内幸町",     "select_A": "うちさいわいまち", "select_B": "うちさいわいちょう", "answer_section": "select_B", "answer": "うちさいわいちょう"},
    {"station_name": "永福町",     "select_A": "えいふくまち",     "select_B": "えいふくちょう",   "answer_section": "select_B", "answer": "えいふくちょう"},
    {"station_name": "荏原町",     "select_A": "えばらまち",       "select_B": "えばらちょう",     "answer_section": "select_A", "answer": "えばらまち"},
    {"station_name": "大井町",     "select_A": "おおいまち",       "select_B": "おおいちょう",     "answer_section": "select_A", "answer": "おおいまち"},
    {"station_name": "大手町",     "select_A": "おおてまち",       "select_B": "おおてちょう",     "answer_section": "select_A", "answer": "おおてまち"},
    {"station_name": "大森町",     "select_A": "おおもりまち",     "select_B": "おおもりちょう",   "answer_section": "select_A", "answer": "おおもりまち"},
    {"station_name": "御徒町",     "select_A": "おかちまち",       "select_B": "おかちちょう",     "answer_section": "select_A", "answer": "おかちまち"},
    {"station_name": "小川町",     "select_A": "おがわまち",       "select_B": "おがわちょう",     "answer_section": "select_A", "answer": "おがわまち"},
    {"station_name": "金町",       "select_A": "かなまち",         "select_B": "かなちょう",       "answer_section": "select_A", "answer": "かなまち"},
    {"station_name": "要町",       "select_A": "かなめまち",       "select_B": "かなめちょう",     "answer_section": "select_B", "answer": "かなめちょう"},
    {"station_name": "上町",       "select_A": "かみまち",         "select_B": "かみちょう",       "answer_section": "select_A", "answer": "かみまち"},
    {"station_name": "神谷町",     "select_A": "じんぼうまち",     "select_B": "かみやちょう",     "answer_section": "select_B", "answer": "かみやちょう"},
    {"station_name": "茅場町",     "select_A": "かやばまち",       "select_B": "かやばちょう",     "answer_section": "select_B", "answer": "かやばちょう"},
    {"station_name": "錦糸町",     "select_A": "きんしまち",       "select_B": "きんしちょう",     "answer_section": "select_B", "answer": "きんしちょう"},
    {"station_name": "京成金町",   "select_A": "けいせいかなまち", "select_B": "けいせいかなちょう", "answer_section": "select_A", "answer": "けいせいかなまち"},
    {"station_name": "麹町",       "select_A": "こうじまち",       "select_B": "こうじちょう",     "answer_section": "select_A", "answer": "こうじまち"},
    {"station_name": "小伝馬町",   "select_A": "こでんままち",     "select_B": "こでんまちょう",   "answer_section": "select_B", "answer": "こでんまちょう"},
    {"station_name": "栄町",       "select_A": "さかえまち",       "select_B": "さかえちょう",     "answer_section": "select_B", "answer": "さかえちょう"},
    {"station_name": "桜新町",     "select_A": "さくらしんまち",   "select_B": "さくらしんちょう", "answer_section": "select_A", "answer": "さくらしんまち"},
    {"station_name": "椎名町",     "select_A": "しいなまち",       "select_B": "しいなちょう",     "answer_section": "select_A", "answer": "しいなまち"},
    {"station_name": "信濃町",     "select_A": "しなのまち",       "select_B": "しなのちょう",     "answer_section": "select_A", "answer": "しなのまち"},
    {"station_name": "新御徒町",   "select_A": "しんおかちまち",   "select_B": "しんおかちちょう", "answer_section": "select_A", "answer": "しんおかちまち"},
    {"station_name": "新富町",     "select_A": "しんとみまち",     "select_B": "しんとみちょう",   "answer_section": "select_B", "answer": "しんとみちょう"},
    {"station_name": "神保町",     "select_A": "じんぼうまち",     "select_B": "じんぼうちょう",   "answer_section": "select_B", "answer": "じんぼうちょう"},
    {"station_name": "末広町",     "select_A": "すえひろまち",     "select_B": "すえひろちょう",   "answer_section": "select_B", "answer": "すえひろちょう"},
    {"station_name": "宝町",       "select_A": "たからまち",       "select_B": "たからちょう",     "answer_section": "select_B", "answer": "たからちょう"},
    {"station_name": "田町",       "select_A": "たまち",           "select_B": "でんちょう",       "answer_section": "select_A", "answer": "たまち"},
    {"station_name": "田原町",     "select_A": "たわらまち",       "select_B": "たわらちょう",     "answer_section": "select_A", "answer": "たわらまち"},
    {"station_name": "千鳥町",     "select_A": "ちどりまち",       "select_B": "ちどりちょう",     "answer_section": "select_B", "answer": "ちどりちょう"},
    {"station_name": "東陽町",     "select_A": "とうようまち",     "select_B": "とうようちょう",   "answer_section": "select_B", "answer": "とうようちょう"},
    {"station_name": "仲御徒町",   "select_A": "なかおかちまち",   "select_B": "なかおかちちょう", "answer_section": "select_A", "answer": "なかおかちまち"},
    {"station_name": "中野富士見町","select_A": "なかのふじみまち","select_B": "なかのふじみちょう","answer_section": "select_B", "answer": "なかのふじみちょう"},
    {"station_name": "永田町",     "select_A": "ながたまち",       "select_B": "ながたちょう",     "answer_section": "select_B", "answer": "ながたちょう"},
    {"station_name": "人形町",     "select_A": "にんぎょうまち",   "select_B": "にんぎょうちょう", "answer_section": "select_B", "answer": "にんぎょうちょう"},
    {"station_name": "練馬春日町", "select_A": "ねりまかすがまち", "select_B": "ねりまかすがちょう","answer_section": "select_B", "answer": "ねりまかすがちょう"},
    {"station_name": "浜町",       "select_A": "はままち",         "select_B": "はまちょう",       "answer_section": "select_B", "answer": "はまちょう"},
    {"station_name": "浜松町",     "select_A": "はままつまち",     "select_B": "はままつちょう",   "answer_section": "select_B", "answer": "はままつちょう"},
    {"station_name": "馬喰町",     "select_A": "ばくろまち",       "select_B": "ばくろちょう",     "answer_section": "select_B", "answer": "ばくろちょう"},
    {"station_name": "府中本町",   "select_A": "ふちゅうほんまち", "select_B": "ふちゅうほんちょう","answer_section": "select_A", "answer": "ふちゅうほんまち"},
    {"station_name": "方南町",     "select_A": "ほうなんまち",     "select_B": "ほうなんちょう",   "answer_section": "select_B", "answer": "ほうなんちょう"},
    {"station_name": "南砂町",     "select_A": "みなみすなまち",   "select_B": "みなみすなちょう", "answer_section": "select_A", "answer": "みなみすなまち"},
    {"station_name": "門前仲町",   "select_A": "もんぜんなかまち", "select_B": "もんぜんなかちょう","answer_section": "select_B", "answer": "もんぜんなかちょう"},
    {"station_name": "有楽町",     "select_A": "ゆうらくまち",     "select_B": "ゆうらくちょう",   "answer_section": "select_B", "answer": "ゆうらくちょう"},
    {"station_name": "六町",       "select_A": "ろくまち",         "select_B": "ろくちょう",       "answer_section": "select_B", "answer": "ろくちょう"}
]

html_index = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>東京都内の「～町駅」50問クイズ</title>
  <!-- Bootstrap CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-color: #f8f9fa;
      padding-top: 2rem;
      padding-bottom: 2rem;
    }
    h1 {
      margin-bottom: 1.5rem;
      text-align: center;
      font-weight: bold;
    }
    ol {
      padding-left: 1rem;
    }
    li {
      margin-bottom: 1.2rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>東京都内の「～町駅」50問クイズ</h1>
    <p class="text-center mb-4">「まち」or「ちょう」どっちか分かるかな？</p>
    <form method="POST" action="/submit">
      <ol>
      {% for quiz in quiz_data %}
        <li>
          <strong>{{ quiz.station_name }}</strong>：
          <div class="form-check">
            <input class="form-check-input" type="radio" id="q_{{ loop.index0 }}_A" name="q_{{ loop.index0 }}" value="select_A" required>
            <label class="form-check-label" for="q_{{ loop.index0 }}_A">{{ quiz.select_A }}</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" id="q_{{ loop.index0 }}_B" name="q_{{ loop.index0 }}" value="select_B" required>
            <label class="form-check-label" for="q_{{ loop.index0 }}_B">{{ quiz.select_B }}</label>
          </div>
        </li>
      {% endfor %}
      </ol>
      <div class="text-center">
        <button type="submit" class="btn btn-primary btn-lg">採点する</button>
      </div>
    </form>
  </div>
</body>
</html>
"""

html_result = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>結果発表</title>
  <!-- Bootstrap CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-color: #f8f9fa;
      padding-top: 3rem;
      padding-bottom: 3rem;
    }
    .score-container {
      max-width: 600px;
      margin: 0 auto;
      text-align: center;
    }
    .score {
      font-size: 2.5rem;
      font-weight: bold;
      color: #0d6efd; /* Bootstrapのprimaryカラー */
    }
  </style>
</head>
<body>
  <div class="container score-container">
    <h1 class="mb-4">結果発表</h1>
    <p class="score">あなたの得点は<br>{{ score }} / 100 点</p>
    <p>お疲れさまでした！</p>
    <a href="/" class="btn btn-secondary mt-3">トップに戻る</a>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(html_index, quiz_data=quiz_data)

@app.route("/submit", methods=["POST"])
def submit():
    # 採点する
    score = 0
    for i, quiz in enumerate(quiz_data):
        user_choice = request.form.get(f"q_{i}")
        if user_choice == quiz["answer_section"]:
            score += 2

    return render_template_string(html_result, score=score)

if __name__ == "__main__":
    app.run(debug=True)
