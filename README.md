<h1>Agendando tarefas de forma assíncrona com Schedule e Asyncio em Python</h1>
Agendar tarefas de forma assíncrona é um desafio comum na programação moderna. Felizmente, existem várias ferramentas disponíveis para ajudar a lidar com essa tarefa, incluindo o pacote Schedule e a biblioteca Asyncio em Python. Juntos, esses dois recursos podem ser usados para criar uma programação assíncrona eficiente e confiável de tarefas.

O Schedule fornece uma maneira fácil de agendar tarefas em um horário específico ou em intervalos regulares, enquanto o Asyncio é uma biblioteca para programação assíncrona que permite executar tarefas em paralelo, melhorando a eficiência e a velocidade do programa. Juntos, essas ferramentas oferecem uma solução poderosa para agendamento de tarefas em Python, permitindo que os desenvolvedores automatizem suas rotinas de trabalho de forma mais eficaz e sem precisar se preocupar com problemas de concorrência.

<h2>Importando as bibliotecas necessárias</h2> 
Neste tópico, as bibliotecas necessárias para implementação do código são importadas, incluindo o asyncio, o schedule e o time.

```python
import asyncio
import random
import time
import schedule
```

<h2>Criando uma classe para representar o tempo de espera personalizado</h2>
Este tópico apresenta a definição da classe CustomSleep, que representa um tempo de espera personalizado, para ser utilizado nos cenários.

```python
class CustomSleep:
    
    def __init__(self, seconds_sleep) -> None:
        self.seconds_sleep = seconds_sleep
    
    def sleep(self):
        print(f"\nVou dormir por {self.seconds_sleep} segundos")
        time.sleep(self.seconds_sleep)

```

<h2>Criando classes para representar os cenários a serem executados</h2>
Neste tópico, são definidas as classes que representam os cenários a serem executados, cada uma com um tempo de espera personalizado.

```python
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
```

<h2>Criando uma classe para gerenciar o Schedule e as tarefas</h2>
Este tópico apresenta a classe ScheduleManager, que é responsável por gerenciar o Schedule e as tarefas a serem executadas.

```python
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
```

<h2>Agendando a execução dos cenários</h2>
O agendamento da execução dos cenários é feito usando a biblioteca Schedule. Para isso, é definido um objeto da classe ScheduleManager, que contém duas funções assíncronas: cenario1_async e cenario2_async. Essas funções utilizam as classes Cenario1 e Cenario2 para executar um tempo de espera personalizado seguido de uma mensagem de conclusão do cenário. Em seguida, é chamada a função advise_sched para agendar a execução dos cenários, definindo um intervalo de 10 segundos para cada um. Para agendar a execução assíncrona, é utilizado o método ensure_future do asyncio.

```python
def advised_sched(self):
    # Agenda a execução dos cenários
    schedule.every(10).seconds.do(lambda: asyncio.ensure_future(manager.cenario1_async()))
    schedule.every(10).seconds.do(lambda: asyncio.ensure_future(manager.cenario2_async()))
```

<h2>Agendando a execução da tarefa de background</h2>
Além da execução dos cenários, o programa também possui uma tarefa de background que é executada em um intervalo menor de tempo. Essa tarefa é definida pela função job, que simplesmente imprime a mensagem "I'm working...". Para agendar a execução dessa tarefa, é chamada a função advise_sched novamente, dessa vez definindo um intervalo de 2 segundos para a tarefa. O agendamento é feito usando o mesmo método do Schedule e também é executado de forma assíncrona.

```python
def advised_sched(self):
    # Agenda a execução dos cenários
    schedule.every(10).seconds.do(lambda: asyncio.ensure_future(manager.cenario1_async()))
    schedule.every(10).seconds.do(lambda: asyncio.ensure_future(manager.cenario2_async()))

    # Agenda a execução da tarefa de background
    schedule.every(2).seconds.do(manager.job)
```

<h2>Iniciando o loop de eventos do Asyncio</h2>
O loop de eventos do Asyncio é iniciado chamando a função start da classe ScheduleManager dentro do método run do asyncio. Essa função faz o agendamento das tarefas usando a função advise_sched e, em seguida, executa um loop infinito que chama a função run_pending do Schedule e aguarda um curto intervalo de tempo para que outras tarefas possam ser executadas. Esse intervalo é definido usando o método sleep do asyncio.

```python
async def start(self):
    self.advised_sched()

    while True:
        schedule.run_pending()

        # Aguarda um curto intervalo para que outras tarefas possam ser executadas
        await asyncio.sleep(1)

if __name__ == '__main__':
    manager = ScheduleManager()

    # Inicia o loop de eventos do asyncio
    asyncio.run(manager.start())
```

<h2>Executando o programa principal</h2>
Por fim, o programa principal é executado chamando a função start da classe ScheduleManager dentro do loop de eventos do Asyncio. Essa função faz o agendamento das tarefas usando a função advise_sched e, em seguida, executa um loop infinito que chama a função run_pending do Schedule e aguarda um curto intervalo de tempo para que outras tarefas possam ser executadas.

```python
if __name__ == '__main__':
    manager = ScheduleManager()

    # Inicia o loop de eventos do asyncio
    asyncio.run(manager.start())
```
Se você gostou deste artigo e quer ver mais exemplos de como utilizar Python e Asyncio em seus projetos, confira o repositório completo no GitHub. Sinta-se à vontade para contribuir com sugestões, melhorias ou mesmo usar o código como base para seus próprios projetos. Esperamos que este artigo tenha sido útil e inspirador para você!"

🔗E aqui está o <a href="https://github.com/marcorsouza/async_schedule_manager">link</a> para o repositório no Github
