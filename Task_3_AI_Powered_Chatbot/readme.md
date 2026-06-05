# AI Powered Chatbot

## Overview

This project is an AI-powered chatbot developed using Python and FastAPI. The chatbot is capable of answering user queries based on a predefined knowledge base. It uses fuzzy string matching to understand user questions and provide the most relevant response.

## Features

- AI-powered question answering system
- Fuzzy matching for intelligent response generation
- REST API built using FastAPI
- Easy-to-expand knowledge base
- Lightweight and cloud-deployment ready

## Technologies Used

- Python
- FastAPI
- FuzzyWuzzy
- Uvicorn

## Project Structure

Task_3_AI_Powered_Chatbot/

├── main.py

├── chatbot.py

├── knowledge_base.py

├── requirements.txt

└── README.md

## How It Works

1. The user sends a question to the chatbot.
2. The chatbot compares the question with entries in the knowledge base.
3. Fuzzy string matching is used to find the closest question.
4. If a match is found, the chatbot returns the corresponding answer.
5. Otherwise, it returns a default response.

## Sample Questions

- What is Cloud Computing?
- What is SQL Injection?
- What is FastAPI?
- What is MySQL?
- What is AI?

## API Endpoints

### Home Endpoint

GET /

Returns application status.

### Chat Endpoint

GET /chat?message=your_question

Returns chatbot response.

## Installation

Install dependencies:

pip install -r requirements.txt

## Run the Application

uvicorn main:app --reload

## Swagger Documentation

Open:

http://127.0.0.1:8000/docs

to test the chatbot API.

## Future Enhancements

- Integration with OpenAI APIs
- Database-driven knowledge base
- User conversation history
- Voice-enabled chatbot
- Cloud deployment on AWS

## Author

Sahil Chaudhary