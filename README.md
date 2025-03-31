# Aira Beauty - Your Premium Beauty Destination

<img src="appaira/static/images/logo1.png" alt="Aira Beauty Logo" width="200" height="auto">

A modern e-commerce platform for premium beauty products, built with Django and designed with a focus on user experience and aesthetic appeal.

🌐 **Live Demo:** https://airarepo.onrender.com

## ✨ Features

### 🛍️ Shopping Experience
- Browse products across multiple categories:
  - Skincare
  - Makeup
  - Hair Care
  - Fragrance
  - Bath & Body
- Real-time cart updates with AJAX
- Dynamic product filtering by brand
- Responsive product cards with hover effects
- Modern, intuitive navigation

### 👤 User Features
- User authentication (login/register)
- Personalized shopping experience
- Secure checkout process
- Order history tracking

### 💫 Design & UI
- Clean, modern interface
- Responsive design for all devices
- Beautiful gradient banners
- Interactive product cards
- Toast notifications for user feedback
- Smooth animations and transitions

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Bootstrap 5
- **Icons:** Font Awesome
- **Notifications:** Toastr.js
- **Database:** SQLite (development)

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/airarepo.git
cd airarepo
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your browser

## 📁 Project Structure

```
airarepo/
├── appaira/
│   ├── static/
│   │   └── images/
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── skincare.html
│   │   │   ├── makeup.html
│   │   │   ├── hair.html
│   │   │   ├── fragrance.html
│   │   │   └── bathbody.html
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── manage.py
│   └── requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

- **Alice Rodgers** - [GitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Bootstrap for the responsive framework
- Font Awesome for the beautiful icons
- Toastr.js for the elegant notifications
- All the beauty brands featured in the project

---

Made with ❤️ by Alice Rodgers
