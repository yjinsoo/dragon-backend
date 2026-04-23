from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

class Instance:
    def __init__(self, name, cpu, ram):
        self.name = name
        self.cpu = cpu
        self.ram = ram


async def provision_resource(resource_name, delay):
    print(f"⚙️ {resource_name} 할당 시작...")
    await asyncio.sleep(delay)
    return f"{resource_name} 완료"

@app.get("/create-server")
async def create_server(name: str = "web-server", cpu: int = 2, ram: int = 4):
  start_time = time.time()

  instance = Instance(name, cpu, ram)

  tasks = [
    provision_resource("Network", 3),
    provision_resource("Disk", 5),
    provision_resource("CPU", 2),
  ]

  await asyncio.gather(*tasks)

  end_time = time.time()

  return {
          "message": "인스턴스 생성 완료!",
          "server_info": {
              "name": instance.name,
              "cpu": instance.cpu,
              "ram": f"{instance.ram}GB"
          },
          "elapsed_time": f"{end_time - start_time:.2f}s"
      }  
