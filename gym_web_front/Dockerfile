FROM node:14.17.3

WORKDIR /gym_web_front

COPY . .

RUN npm install
RUN npm install react-scripts@3.4.1 -g 

EXPOSE 3000

CMD ["npm", "start"]
