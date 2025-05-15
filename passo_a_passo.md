# Passo a Passo para Exportar Membros de um Canal no Telegram

1. **Criar um Bot no Telegram**
   - Abra o Telegram e procure pelo BotFather.
   - Use o comando `/newbot` para criar um novo bot.
   - Siga as instruções para nomear seu bot e obter o token de acesso.

2. **Obter suas credenciais da API do Telegram**
   - Acesse https://my.telegram.org/ e faça login com seu número de telefone.
   - Clique em "API development tools" e crie um novo aplicativo para obter seu `API_ID` e `API_HASH`.

3. **Configurar o Script**
   - No arquivo `export_members.py`, substitua:
     - `'API_ID'` pelo seu API ID
     - `'API_HASH'` pelo seu API Hash
     - `'YOUR_BOT_TOKEN'` pelo token do seu bot
     - `'channel_username'` pelo @username do canal que você administra

4. **Executar o Script**
   - No terminal, execute:
     ```bash
     python export_members.py
     ```

5. **Verificar o Arquivo de Saída**
   - Após a execução, verifique o arquivo `members.csv` na mesma pasta do script para ver a lista de membros exportados.

### Observações
- O bot precisa ser administrador do canal para conseguir exportar os membros.
- A API do Telegram possui limites de taxa. Se o canal for muito grande, pode ser necessário aguardar entre execuções.
- O arquivo CSV conterá as colunas: `id`, `first_name` e `last_name` de cada membro. 