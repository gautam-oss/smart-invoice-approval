# Smart Invoice Approval System

AI-powered invoice processing system with automated approval workflow using Gemini API.

## 🚀 Features

- **AI-Powered Extraction**: Automatically extract invoice details using Google's Gemini API
- **Smart Approval**: Auto-approve low-risk invoices, flag high-value ones for review
- **Anomaly Detection**: Detect duplicates and unusual amounts
- **Real-time Dashboard**: Monitor all invoices and their processing status
- **Complete Audit Trail**: Track all actions and decisions

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: Django 4.2 + Django REST Framework
- **Workflow Automation**: n8n
- **AI**: Google Gemini API
- **Database**: PostgreSQL
- **Infrastructure**: Docker & Docker Compose

## 📋 Prerequisites

- Docker Desktop installed
- Git Bash (Windows) or Terminal (Mac/Linux)
- Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

## 🏗️ Project Structure

```
smart-invoice-approval/
├── docker-compose.yml          # Docker services configuration
├── backend/                    # Django application
│   ├── config/                 # Django settings
│   ├── invoices/               # Main app
│   ├── static/                 # CSS, JS, Images
│   ├── templates/              # HTML templates
│   └── media/                  # Uploaded files
├── n8n/                        # n8n workflows
└── docs/                       # Documentation
```

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd smart-invoice-approval
```

### 2. Create Environment File

```bash
cp .env.example .env
```

Edit `.env` and add your Gemini API key.

### 3. Build and Start Services

```bash
docker-compose up --build
```

Wait for all services to start. You should see:
- ✅ PostgreSQL ready
- ✅ Django migrations applied
- ✅ Django server running on port 8000
- ✅ n8n running on port 5678

### 4. Access the Application

- **Django App**: http://localhost:8000
- **Django Admin**: http://localhost:8000/admin
- **n8n Dashboard**: http://localhost:5678 (user: admin, pass: admin123)
- **API Health Check**: http://localhost:8000/api/health/

## 📝 Development Progress

- [x] **Phase 1**: Environment Setup ✅
- [ ] **Phase 2**: Django Models
- [ ] **Phase 3**: REST API
- [ ] **Phase 4**: Frontend - Upload Page
- [ ] **Phase 5**: n8n Workflow Setup
- [ ] **Phase 6**: Gemini API Integration
- [ ] **Phase 7**: AI Decision Logic
- [ ] **Phase 8**: Update Django from n8n
- [ ] **Phase 9**: Frontend - Dashboard
- [ ] **Phase 10**: Invoice Detail Page

## 🧪 Testing Phase 1

Run these commands to verify everything is working:

```bash
# Check all containers are running
docker-compose ps

# Test Django health endpoint
curl http://localhost:8000/api/health/

# Check n8n is accessible
curl http://localhost:5678

# View Django logs
docker-compose logs django

# View n8n logs
docker-compose logs n8n

# View database logs
docker-compose logs db
```

## 🛠️ Useful Commands

```bash
# Start services
docker-compose up

# Start in detached mode
docker-compose up -d

# Stop services
docker-compose down

# Rebuild containers
docker-compose up --build

# View logs
docker-compose logs -f

# Access Django shell
docker-compose exec django python manage.py shell

# Run Django commands
docker-compose exec django python manage.py <command>

# Access database
docker-compose exec db psql -U invoiceuser -d invoicedb
```

## 📚 Documentation

- [Setup Guide](docs/SETUP.md) - Detailed setup instructions
- [API Documentation](docs/API.md) - API endpoints reference
- [Architecture](docs/ARCHITECTURE.md) - System design overview
- [n8n Workflow Guide](docs/n8n-workflow-guide.md) - n8n configuration

## 🐛 Troubleshooting

### Containers won't start

```bash
docker-compose down -v
docker-compose up --build
```

### Port already in use

Change ports in `docker-compose.yml`:
```yaml
ports:
  - "8001:8000"  # Change 8000 to 8001
```

### Database connection issues

```bash
# Recreate database volume
docker-compose down -v
docker-compose up
```

## 📄 License

MIT License - feel free to use this project for learning!

## 🤝 Contributing

This is a learning project. Feel free to fork and experiment!

## 📧 Contact

For questions or issues, create an issue in the repository.

---

**Status**: Phase 1 Complete ✅ - Ready for Phase 2 (Django Models)