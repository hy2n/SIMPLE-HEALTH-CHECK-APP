from flask import Flask, request, jsonify

app = Flask(__name__)

# 증상 목록과 그에 따른 진단 및 약 정보
symptoms_diagnosis = {
    "안구건조증": {
        "symptoms": ["눈의 건조함", "시야흐림", "눈의 가려움", "눈의 피로", "이물감"],
        "medicine": "인공눈물(히알루론산 점안액)"
    },
    "염좌": {
        "symptoms": ["통증과 압통", "부종", "관절의 움직임 제한"],
        "medicine": "파스, 소염제, 근육이완제"
    },
    "두통": {
        "symptoms": ["머리의 통증", "뇌 압박감", "빛과 소리에 예민함", "메스꺼움", "시야흐림"],
        "medicine": "이부프로펜, 아세트아미노펜, 아스피린"
    },
    "복통": {
        "symptoms": ["복부통증 및 경련", "팽만감", "가스차는 느낌", "메스꺼움", "설사또는 변비"],
        "medicine": "소화제, 부스코판, 진통제, 제산제"
    },
    # 추가적인 질병들...
}

# 증상 체크 API
@app.route('/check_symptoms', methods=['POST'])
def check_symptoms():
    data = request.json
    checked_symptoms = data.get('symptoms', [])
    
    if not checked_symptoms:
        return jsonify({"message": "증상을 선택해 주세요."}), 400

    possible_diagnoses = []
    
    for diagnosis, info in symptoms_diagnosis.items():
        # 체크된 증상과 각 질병의 증상을 비교하여 진단 가능 여부 확인
        matching_symptoms = [symptom for symptom in checked_symptoms if symptom in info['symptoms']]
        if 3 <= len(matching_symptoms) <= 5:
            possible_diagnoses.append({
                "diagnosis": diagnosis,
                "medicine": info["medicine"]
            })
    
    # 진단이 가능한 경우
    if possible_diagnoses:
        return jsonify({"possible_diagnoses": possible_diagnoses}), 200
    else:
        return jsonify({"message": "다시 체크해 주십시오."}), 400

if __name__ == '__main__':
    app.run(debug=True)
