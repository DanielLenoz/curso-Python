import asyncio
import random 

async def process_data(data):
    print(f'Procesando canciondes de {data}...')
    #Simular una operación
    random_number = random.randint(1,10)
    await asyncio.sleep(random_number)
    print(f'cancion de {data} numero {random_number}. procesado.')
    return "cancion descargada"

async def main():
    print('Inicio de procesamiento de descarga')
    result = await process_data('BARAK ')
    print(f'Resultado: {result}')

asyncio.run(main())
asyncio.run(main())
asyncio.run(main())
asyncio.run(main())
asyncio.run(main())