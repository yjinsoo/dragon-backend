from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
# 실무 구조(같은 도메인/Proxy)에서는 CORS가 필수는 아니지만, 테스트 편의를 위해 추가합니다.
CORS(app)

# 로그 설정 (컨테이너 로그에서 확인 가능하도록)
logging.basicConfig(level=logging.INFO)

@app.route('/send-email', methods=['POST'])
def receive_data():
    try:
        data = request.json
        
        # 프론트엔드에서 보낸 데이터 로그 출력
        app.logger.info("---------- 영수증 데이터 수신 ----------")
        app.logger.info(f"집행일자: {data.get('date')}")
        app.logger.info(f"집행처: {data.get('vendor')}")
        app.logger.info(f"금액: 식비({data.get('mealExp'):,}) / 간식비({data.get('snackExp'):,})")
        app.logger.info(f"집행자: {data.get('executor')} / 승인자: {data.get('approver')}")
        app.logger.info(f"참석인원: {data.get('count')}명 ({', '.join(data.get('participants', []))})")
        app.logger.info("---------------------------------------")

        # 일단 성공 응답만 보냄 (나중에 여기서 Gmail 발송 로직 추가)
        return jsonify({
            "status": "success", 
            "message": "백엔드가 데이터를 성공적으로 수신했습니다."
        }), 200

    except Exception as e:
        app.logger.error(f"에러 발생: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # 컨테이너 환경에서는 0.0.0.0 으로 띄워야 외부(Service)에서 접근 가능합니다.
    app.run(host='0.0.0.0', port=5000)
