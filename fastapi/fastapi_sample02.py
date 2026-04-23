'''
API 주소: /delete-project

입력 파라미터:
project_name: 삭제할 프로젝트 이름 (기본값: "temp-project")
force: 강제 삭제 여부 (타입: bool, 기본값: False)

내부 로직:
함수 내부에 async def delete_db()와 async def delete_storage()라는 중첩 함수를 정의하세요.
delete_db는 2초, delete_storage는 1초가 소요됩니다. (asyncio.sleep 사용)
만약 force가 True이면 두 함수를 동시에(gather) 실행하고, False이면 순차적으로(await 따로따로) 실행하세요.
결과 반환: 총 소요 시간과 함께 "삭제 완료" 메시지를 JSON으로 반환하세요.
'''

from fastapi import FastAPI
import asyncio, time
