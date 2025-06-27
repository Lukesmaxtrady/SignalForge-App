version: "3.8"
services:
  backend:
    build: ./main
    ports:
      - "8000:8000"
    env_file:
      - ./main/.env
    volumes:
      - ./main:/app
    depends_on:
      - mongo
  mongo:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - ./mongo_data:/data/db
