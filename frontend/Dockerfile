FROM node:lts-alpine3.15

WORKDIR /usr/src/frontend

COPY package.json package-lock.json ./
COPY .env .

RUN npm install && npm install react-scripts@5.0.0 -g
COPY . ./
EXPOSE 3000