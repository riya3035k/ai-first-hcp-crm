# AI-First HCP CRM

An AI-powered Healthcare Professional (HCP) Customer Relationship Management system designed to manage HCP information and interactions efficiently.

## Features

- Log new HCP interactions
- Update existing interactions
- Search for Healthcare Professionals (HCPs)
- View HCP interaction history
- Schedule follow-ups
- AI-powered chat assistant
- Natural language interaction with CRM operations

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Groq API
- AI Agent with tool calling

### Frontend
- React
- Vite
- Redux
- JavaScript
- CSS

### Database
- Relational Database

## API Endpoints

- `POST /interactions` - Create an interaction
- `PUT /interactions/{interaction_id}` - Update an interaction
- `GET /hcps/search` - Search for an HCP
- `GET /hcps/{hcp_id}/history` - Get interaction history
- `POST /interactions/{interaction_id}/followup` - Schedule a follow-up
- `POST /chat` - Chat with the AI agent

## Security

Environment variables and sensitive information such as API keys and database credentials are stored in a `.env` file. The `.env` file is excluded from Git using `.gitignore`.

## Project Structure

AI-First-HCP-CRM
- `backend/` - FastAPI backend, database, and AI agent
- `frontend/` - React frontend application

## Author

Riya Kumari