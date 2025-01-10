import asyncio
import random

async def proccesPayment(customer_name, amount):
    print('-------Iniciando proceso de pago...')
    print(f'Procesando pago de {customer_name}...')
    random_number = random.randint(1,4)
    await asyncio.sleep(random_number)
    print(f'Pago de {amount} procesado. tiempo demorado {random_number} segundos')
    return 'Pago realizado'