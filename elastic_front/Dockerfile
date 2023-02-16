#FROM node:19.4.0
#
#WORKDIR /app
#ENV PATH /app/node_modules/.bin:$PATH
#
#COPY package*.json ./
#RUN npm install
#
#COPY . .
#
#EXPOSE 8080
#CMD npm run dev

FROM node:19.4.0 as develop-stage

WORKDIR /app
COPY package*.json ./
RUN yarn install

COPY . .

FROM develop-stage as build-stage
RUN yarn build

FROM nginx:latest as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]