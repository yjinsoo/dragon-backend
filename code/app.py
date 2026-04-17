from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # 프론트엔드와 통신 허용

# Gmail 설정 (환경변수 권장)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
MAIL_USER = "본인계정@gmail.com" 
MAIL_PASS = os.getenv("MAIL_PASSWORD") # Jenkins에서 주입할 비밀번호

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        
        # 1. 데이터 가공
        date_obj = datetime.strptime(data['date'], '%Y-%m-%d')
        subject = f"부서운영비 사용승인요청 ({date_obj.strftime('%m/%d')})"
        total_amt = f"{data['mealExp'] + data['snackExp']:,}"
        names_str = ", ".join(data['participants'])
        
        # 2. HTML 메일 본문 생성 (이미지 양식 반영)
        html_content = f"""
        <html>
        <body>
            <p>안녕하세요 파트장님.</p>
            <p>하기 사유로 부서운영비 사용 승인 요청드립니다.</p>
            <table border="1" style="border-collapse: collapse; width: 100%; max-width: 600px; text-align: center;">
                <tr style="background-color: #f2f2f2;">
                    <th width="20%">집행자</th><td>{data['executor']} 매니저</td>
                    <th width="20%">승인자</th><td>{data['approver']} 파트장</td>
                </tr>
                <tr>
                    <th style="background-color: #f2f2f2;">집행 일자</th>
                    <td colspan="3">{data['date']}</td>
                </tr>
                <tr>
                    <th style="background-color: #f2f2f2;">집행 금액</th>
                    <td colspan="3">{total_amt} 원 (규정식비외 추가분 및 간식비)</td>
                </tr>
                <tr>
                    <th style="background-color: #f2f2f2;">집행처/구매처</th>
                    <td colspan="3">{data['vendor']}</td>
                </tr>
                <tr>
                    <th style="background-color: #f2f2f2;">내용/대상</th>
                    <td colspan="3" style="text-align: left; padding: 10px;">
                        부서운영비-규정식비 외 추가분 {data['count']}명({names_str})<br>
                        부서운영비-간식비 {data['count']}명({names_str})
                    </td>
                </tr>
            </table>
            <p>위와 같이 승인 요청드립니다.</p>
            <p>감사합니다.<br>{data['executor']} 드림</p>
        </body>
        </html>
        """

        # 3. 메일 발송 로직
        msg = MIMEMultipart()
        msg['From'] = MAIL_USER
        msg['To'] = "파트장님메일@test.com" # 실제 수신자
        msg['Subject'] = subject
        msg.attach(MIMEText(html_content, 'html'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(MAIL_USER, MAIL_PASS)
        server.sendmail(MAIL_USER, msg['To'], msg.as_string())
        server.quit()

        return jsonify({"status": "success", "message": "Email sent successfully!"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
