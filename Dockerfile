FROM node:16.0.0-alpine

COPY [".", "/usr/app"]

WORKDIR /usr/app

RUN npm install

EXPOSE 4000

CMD [ "npm", "start" ]