# BiasLens

## Project Overview  
BiasLens is an analytical platform that examines media bias in news coverage.  
Users can search for a topic and compare how different news outlets report on it, with automated bias analysis.

## Project Structure  
- `client/` — React.js frontend with TailwindCSS  
- `server/` — Node.js backend (Express)  
- `analyzer/` — Python NLP service (FastAPI or Flask)  
- `data/` — Sample news data for development  
- `docker-compose.yml` — Docker configuration connecting all components

## Getting Started

### Frontend Setup  
```bash
cd client  
npm install  
npm run dev  
