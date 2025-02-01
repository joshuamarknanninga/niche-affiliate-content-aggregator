# Niche Affiliate Content Aggregator

A full-stack web application for curating and monetizing affiliate products, featuring a Python/Flask backend and React frontend.

![App Screenshot](./screenshot.png)

## Features

- **Product Aggregation**: Curate products from multiple affiliate programs
- **Smart Filtering**: Category-based filtering and search functionality
- **Click Tracking**: Monitor affiliate link performance with analytics
- **Responsive Design**: Mobile-friendly interface
- **Admin Dashboard**: Basic analytics and traffic insights (WIP)

## Technologies Used

**Backend**:
- Python 3.12
- Flask
- Flask-CORS
- Flask-Limiter
- SQLite/Redis

**Frontend**:
- React 18
- Vite
- CSS Modules
- React Router

## Installation

### Backend Setup

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/niche-affiliate-aggregator.git
cd niche-affiliate-aggregator/backend

niche-affiliate-aggregator/
├── backend/
│   ├── app.py               # Main application logic
│   ├── requirements.txt     # Python dependencies
│   ├── init_db.py           # Database initialization
│   └── affiliate.db         # SQLite database (auto-generated)
└── frontend/
    ├── src/
    │   ├── components/      # React components
    │   ├── pages/           # Page layouts
    │   ├── App.jsx          # Root component
    │   └── main.jsx         # Entry point
    ├── public/              # Static assets
    └── vite.config.js       # Build configuration

    Contributing
Fork the repository

Create feature branch: git checkout -b feature/new-feature

Commit changes: git commit -m 'Add some feature'

Push to branch: git push origin feature/new-feature

Open a Pull Request

License
MIT License - See LICENSE for details

Acknowledgements
Product data from Amazon Associates

UI components inspired by Tailwind CSS

Initial project structure from Full Stack Flask/React Blueprint