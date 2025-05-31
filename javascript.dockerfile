FROM node:18-alpine

WORKDIR /code
COPY . /code
CMD ["node", "/code/code.js"]
