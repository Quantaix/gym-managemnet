# Fitness World Web Application

This project is a web-based application for "Fitness World," aimed at providing an interactive platform for a gym to showcase its services, memberships, and facilities. Built with Flask, HTML, and CSS, it includes an intuitive user interface with dedicated pages for home, about, and membership details.

## Project Purpose
The goal of this project is to create a seamless user experience for gym members and prospective clients. Users can explore membership plans, learn about the gym, and contact the gym for further details.

## Features
- **Homepage:** Welcomes users and introduces the gym.
- **About Us Page:** Provides details about the gym's mission, trainers, and facilities.
- **Membership Page:** Displays membership plans with features and pricing.
- **Contact Section:** Allows users to send inquiries through a form.

## Project Structure
```
project-directory/
├── app.py           # Main Flask application
├── static/
│   └── style.css    # Stylesheet for the web pages
├── templates/
│   ├── hi.html      # Homepage template
│   ├── membership.html # Membership page template
│   ├── aboutus.html # About Us page template
└── README.md        # Documentation (this file)
```

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.7+
- Flask (`pip install flask`)

## How to Run the Project Locally
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd project-directory
   ```

2. **Install required packages:**
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
   Install Flask:
   ```bash
   pip install flask
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```
   The application will start at `http://127.0.0.1:5000/`.

4. **Access the web pages:**
   - Homepage: `http://127.0.0.1:5000/`
   - About Us: `http://127.0.0.1:5000/about`
   - Membership: `http://127.0.0.1:5000/member`

## Usage
- Open the application in a browser using the URLs mentioned above.
- Navigate through the pages using the navigation bar.
- Explore membership options and contact the gym via the form provided on the membership page.

## Future Improvements
- Add dynamic content using a database.
- Enhance the contact form with email integration.
- Optimize responsiveness for mobile devices.
- Include a detailed "About Us" page content.

## Contributing
Feel free to fork this repository and submit pull requests with improvements or new features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
Enjoy using the Fitness World Web Application to build a stronger, healthier you!
