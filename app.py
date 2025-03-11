import os
from flask import Flask, request, render_template
import vertexai
from vertexai.generative_models import GenerativeModel

#from google import genai
#from google.genai.types import HttpOptions

# CONFIGURATION
PROJECT_ID = "peppy-web-452401-v7"
REGION = "us-central1"

# Vertex AI 초기화 (환경 변수 GOOGLE_APPLICATION_CREDENTIALS 또는 ADC가 설정되어 있어야 합니다.)
vertexai.init(project=PROJECT_ID, location=REGION)

model = GenerativeModel("gemini-pro")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendation = None  # 기본적으로 결과는 없음
    if request.method == "POST":
        # 폼 데이터 읽기
        yesterday_lunch = request.form.get("yesterday_lunch")
        breakfast_today = request.form.get("breakfast_today")
        mood = request.form.get("mood")
        food_preference = request.form.get("food_preference")
        
        # 사용자 입력을 바탕으로 프롬프트 생성
        prompt = (
            f"어제 점심은 {yesterday_lunch}, 오늘 아침은 {breakfast_today}를 먹었고, "
            f"오늘 기분은 {mood}이며, 먹고 싶은 음식은 {food_preference}입니다. "
            "이 정보를 바탕으로 추천할 만한 점심 메뉴를 제안해 주세요."
        )
        
        # Vertex AI의 Gemini 모델을 사용해 콘텐츠 생성 요청
        response = model.generate_content(prompt)
        recommendation = response.text  # 응답에서 텍스트 추출

    # GET 요청이나 POST 후 결과 모두 index.html 템플릿을 렌더링합니다.
    return render_template("index.html", recommendation=recommendation)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)




# # Initialize client
# client = genai.Client(api_key=API_KEY, http_options=HttpOptions(api_version="v1"))
# response = client.models.generate_content(
#     model="gemini-2.0-flash-001",
#     contents="짧게 대답해줘. 지금 나는 밥을 먹고 싶은데 음식을 추천해줘.",
# )
# print(response.text)
# Example response:
# Okay, let's break down how AI works. It's a broad field, so I'll focus on the ...
#
# Here's a simplified overview:
# ...
