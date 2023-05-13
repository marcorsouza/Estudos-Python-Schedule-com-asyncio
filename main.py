import asyncio
import random
import time
import schedule

class CustomSleep:
    
    def __init__(self, seconds_sleep) -> None:
        self.seconds_sleep = seconds_sleep
    
    def sleep(self):
        print(f"\nVou dormir por {self.seconds_sleep} segundos")
        time.sleep(self.seconds_sleep)
        

class Cenario1:
    async def async_run(self):
        seconds_sleep = random.randrange(1,10)
        await asyncio.get_event_loop().run_in_executor(None, CustomSleep(seconds_sleep).sleep)
        print(f"\nCenario 1 foi executado após {seconds_sleep} segundos")
        
class Cenario2:
    async def async_run(self):
        seconds_sleep = random.randrange(1,10)
        await asyncio.get_event_loop().run_in_executor(None, CustomSleep(seconds_sleep).sleep)
        print(f"\nCenario 2 foi executado após {seconds_sleep} segundos")        
        
class ScheduleManager:
    def __init__(self) -> None:
        self.c1 = Cenario1()
        self.c2 = Cenario2()

    async def cenario1_async(self):
        print('\ncenario1 async')
        await self.c1.async_run()

    async def cenario2_async(self):
        print('\ncenario2 async')
        await self.c2.async_run()

    def job(self):
        print("\nI'm working...")
        
    def advised_sched(self):
        # Agenda a execução dos cenários
        schedule.every(10).seconds.do(lambda: asyncio.ensure_future(manager.cenario1_async()))
        schedule.every(10).seconds.do(lambda: asyncio.ensure_future(manager.cenario2_async()))

        # Agenda a execução da tarefa de background
        schedule.every(2).seconds.do(manager.job)

    async def start(self):
        self.advised_sched()

        while True:
            schedule.run_pending()

            # Aguarda um curto intervalo para que outras tarefas possam ser executadas
            await asyncio.sleep(1)

if __name__ == '__main__':
    def test_async():
        print('tests asyncio - begin')
        c1 = Cenario1()
        c2 = Cenario2()

        async def run_cenarios():
            await asyncio.gather(c1.async_run(), c2.async_run())

        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_cenarios())
        print('tests asyncio - end')
    
    manager = ScheduleManager()

    # Inicia o loop de eventos do asyncio
    asyncio.run(manager.start())
