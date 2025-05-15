from telethon import TelegramClient
import csv

api_id = 23359448  # Seu API ID
api_hash = '636ff685b7256d648a23306c46e5223a'  # Seu API Hash

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Buscando o grupo pelo nome
    target_group_name = 'DI Membros'  # Nome exato do grupo
    target_group = None

    async for dialog in client.iter_dialogs():
        if dialog.name == target_group_name:
            target_group = dialog
            break

    if not target_group:
        print(f'Grupo \"{target_group_name}\" não encontrado!')
        return

    members = await client.get_participants(target_group)

    # Salvar os membros em um arquivo CSV
    with open('members.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for member in members:
            writer.writerow({
                'id': member.id,
                'first_name': member.first_name,
                'last_name': member.last_name
            })

with client:
    client.loop.run_until_complete(main()) 