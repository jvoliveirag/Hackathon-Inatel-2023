# Definir a imagem base do Node.js com a versão desejada
FROM node:14-alpine

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo package.json e package-lock.json (se existir)
COPY package*.json ./

# Instalar as dependências do projeto
RUN npm install

# Copiar o restante dos arquivos da aplicação
COPY . .

# Compilar a aplicação Next.js
RUN npm run build

# Definir o comando padrão para iniciar o servidor
CMD ["npm", "start"]
