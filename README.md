# HargaHuni AI 🏠🔮

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  [![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  [![Build Status](https://img.shields.io/badge/Status-Prototype-orange)]()

**AI-powered house price predictor** tailored for the Jabodetabek region. Leverages XGBoost regression and a modern web UI to estimate property values based on user inputs.

---

## ✨ Features

* 🧠 **Smart Prediction:** Utilizes XGBoost (v1.5.0) for accurate price forecasting
* 🌍 **Regional Scope:** Focused on Jakarta, Bogor, Depok, Tangerang, and Bekasi
* 🖥️ **Intuitive UI:** Interactive, responsive design with real-time feedback
* 🔄 **Real-Time Results:** Immediate prediction updates as input parameters change
* 📊 **Evaluation Metrics:** MAE, RMSE, and R² to quantify model performance

---

## 🛠️ Technologies

* **Backend:** Python 3.8+ & Flask 2.2.5
* **Model:** XGBoost 1.5.0 (optimized hyperparameters)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Database:** PostgreSQL 13 (history & locality tables)
* **Deployment:** Docker 20.x & Gunicorn 20.x
* **Python Libraries:** NumPy 1.23, pandas 1.5, scikit-learn 1.1, psycopg2 2.9

---

## 🏘️ Website UI

![HargaHuni Dashboard](Resources/pic1.png)
![HargaHuni LogIn](Resources/pic2.png)
![HargaHuni Prediction](Resources/pic3.png)
![HargaHuni Result](Resources/pic4.png)


---

## 📊 Model Performance

* **MAE (Train Data):** 0.148
* **MAE (Test Data):** 0.222

* **RMSE (Train Data):** 0.210
* **RMSE (Test Data):** 0.341

* **R² (Train Data)):** 0.966
* **R² (Test Data):** 0.907

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* Docker (optional)
* PostgreSQL 13

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/giovincentricels/ProgramDesign_.git
   cd ProgramDesign_
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** (create a `.env` file)

   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/hargahuni_db
   SECRET_KEY=your_secret_key_here
   ```

5. **Initialize the database**

   ```bash
   flask db upgrade
   ```

6. **Run the server**

   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

7. **Access the app**
   Open `http://localhost:5000` in your browser.

---

## 🔍 How It Works

1. **Open HargaHuni Website**
2. **Log In**
   Click **Login** in the navbar, enter your credentials, and submit.
3. **Go to Predict Page**
   After login, select **Predict** from the menu to access the price estimator.
4. **Enter Property Details**
   Fill in:

   * **District & City:** Jakarta, Bogor, Depok, Tangerang, Bekasi
   * **Bedrooms & Bathrooms:** Number
   * **Land & Building Size:** m²
   * **Floors:** Number of storeys
   * **Garage:** Yes/No
5. **Submit & View Estimate**
   Click **Predict** to run the model—your estimated house price appears below.

> **Tip:** Use realistic local values for highest accuracy.

---

## 🎓 Contribution

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create a new branch (`git checkout -b feature/name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

