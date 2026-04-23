'''
[요구 사항]
Instance 클래스 만들기:
생성자(__init__)에서 name, cpu, ram 정보를 받아서 저장하세요.
os 모듈 활용:
서버 생성 시작 시, 현재 내 컴퓨터의 로그인 된 사용자 이름(os.getlogin())을 출력하며 "XX님이 생성을 시작합니다."라고 알리세요.
비동기 함수 provision_resource(resource_name, delay):
이 함수는 "네트워크 설정 중...", "디스크 할당 중..." 같은 메시지를 찍고 delay만큼 await asyncio.sleep()을 합니다.
main 함수 (전체 흐름 제어):
Instance 객체를 하나 만드세요. (예: 이름="Web-Server", CPU=2, RAM=4)
provision_resource를 사용해 다음 두 작업을 동시에(gather) 실행하세요.
"네트워크 설정" (3초 소요)
"디스크 할당" (2초 소요)
모든 작업이 끝나면 Instance 객체의 상세 정보와 함께 "생성 완료!"를 출력하세요.
'''


import os, time, asyncio


class Instance:
  def __init__(self, name, cpu, ram):
    self.name = name
    self.cpu =  cpu
    self.ram = ram


async def provision_resource(resource_name, delay):
  print(f"{resource_name} 설정 ({deploy}초 소요)")
  await asyncio.sleep(delay)


async def main():
  instance = [
    Instance("web-server",2,4),
    Instance("db-server",4, 8)
  ]

  setting_resource = [
    {"resource":"memory", "time":3},
    {"resource":"disk", "time":5},
    {"resource":"cpu", "time":2}
  ]

  tasks = [provision_resource(item["resource"], item["time"]) for item in setting_resource]

  await asyncio.gather(*tasks)



if __name__ == "__main__":
  asyncio.run(main())

  
