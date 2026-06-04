# SQL Injection Protection System

## Overview

A FastAPI-based cloud security system designed to prevent SQL injection attacks and protect sensitive user information using AES encryption.

## Features

- SQL Injection Detection
- AES-256 Style Encryption using Fernet
- Secure User Registration
- MySQL Database Integration
- Double-Layer Security Architecture

## Technologies Used

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Cryptography

## Security Layers

### Layer 1: SQL Injection Detection

The system scans user inputs for common SQL injection patterns such as:

- OR 1=1
- DROP TABLE
- UNION SELECT
- DELETE FROM

### Layer 2: Data Encryption

User passwords are encrypted before being stored in the database.

## API Endpoints

### GET /

Returns application status.

### POST /register

Registers a user securely.

### GET /users

Displays registered users.

## How to Run

Install dependencies:

pip install -r requirements.txt

Start the server:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs