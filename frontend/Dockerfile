FROM node:lts-alpine3.15

WORKDIR /usr/src/frontend

COPY .env.example .env
COPY . ./

RUN npm install && npm install react-scripts@5.0.0 -g
EXPOSE 3000