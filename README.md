📱 Phone Resale Price Prediction – Machine Learning Project
🧠 Project Overview

This project predicts the resale price of smartphones using machine learning.
By entering phone specifications and years of use, users can quickly estimate the resale value.

📊 Dataset

The dataset contains smartphone specifications and resale prices.

Features:

brand: Brand of the phone (e.g., Samsung, Apple)

ram: RAM in GB

storage: Storage in GB

battery: Battery capacity in mAh

main_camera: Main camera resolution in MP

front_camera: Front camera resolution in MP

original_price: Original price in ₹

years_of_use: Years of usage

Target:

resale_price: Predicted resale price in ₹

⚙️ Technologies Used

Programming Language: Python

Libraries: pandas, numpy, scikit-learn, pickle, streamlit

📁 Project Structure
Phone-Resale-Price-ML-Project/
│
├── data/
│   └── phone_prices.csv          # Dataset with phone specs and resale prices
│
├── model/
│   └── phone_resale_model.pkl    # Trained Random Forest model + LabelEncoder
│
├── app.py                        # Streamlit web application
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

🚀 How to Run the Application
1. Clone the repository
git clone https://github.com/VarshaYadav634/Phone-Resale-Price-ML-Project.git
cd Phone-Resale-Price-ML-Project

2. Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run app.py


Open the link shown in the terminal to access the app in your browser.

📈 Model Evaluation

Algorithm: Random Forest Regressor (Regression)

Metrics:

Mean Absolute Error (MAE): Average prediction error in ₹

R² Score: Variance explained by the model

Approximate Accuracy (%):

Accuracy % = (1 - MAE / Average Resale Price) * 100

🧪 Future Enhancements

Try Gradient Boosting / XGBoost for better accuracy

Add features like screen size, processor type, phone condition

Deploy as a mobile application
