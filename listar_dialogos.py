from telethon import TelegramClient

api_id = 23359448  # Substitua pelo seu API ID, sem aspas
api_hash = '636ff685b7256d648a23306c46e5223a'  # Substitua pelo seu API Hash, com aspas

client = TelegramClient('session_listar', api_id, api_hash)

async def main():
    print('Listando canais e grupos disponíveis:')
    async for dialog in client.iter_dialogs():
        if dialog.is_channel or dialog.is_group:
            print(f'Nome: {dialog.name} | ID: {dialog.id}')

with client:
    client.loop.run_until_complete(main()) 