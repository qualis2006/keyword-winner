from flask import Flask, render_template, request
import google_keyword

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
  key1 = request.args.get('keyword1')
  key2 = request.args.get('keyword2')
  print("key1: ", key1, "key2: ", key2)

  #if key1 is None or key2 is None: # keyword is null string
  #if key1 == "" or key2 == "": # keyword is null string
  if not key1  or not key2 : # keyword is null string
    errorMsg = "첫번째 키워드와 두번째 키워드 모두 입력하세요!!"
    return render_template('index.html', errorMsg=errorMsg)
  else:
    value1 = google_keyword.get_keyword_number(key1)
    value2 = google_keyword.get_keyword_number(key2)

    data = {key1:value1, key2:value2 }

    return render_template('index.html', data=data)


if __name__=="__main__":
  app.run(debug=True)