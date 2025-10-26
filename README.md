📱 **Phone Resale Price Prediction – Machine Learning Project**
🧠 Project Overview

This project leverages machine learning to predict the resale price of smartphones based on their specifications and usage history. By inputting details such as brand, RAM, storage, battery capacity, camera specifications, original price, and years of use, users can obtain an estimated resale value. This tool is particularly beneficial for consumers looking to assess the value of their devices before selling or upgrading.

📊 Dataset

The dataset comprises various smartphone models with attributes influencing resale value:

Features:

brand: Smartphone brand (e.g., Samsung, Apple, Xiaomi)

ram: RAM in GB

storage: Storage capacity in GB

battery: Battery capacity in mAh

main_camera: Main camera resolution in MP

front_camera: Front camera resolution in MP

original_price: Original purchase price in ₹

years_of_use: Duration of use in years

Target Variable:

resale_price: Estimated resale price in ₹

⚙️ Technologies Used

Programming Language: Python

Libraries & Frameworks:

pandas, numpy: Data manipulation and analysis

scikit-learn: Machine learning algorithms and tools

pickle: Model serialization

streamlit: Web application framework for deployment

📁 Project Structure
Phone-Resale-Price-ML-Project/
│
├── data/
│   └── phone_prices.csv          # Dataset containing phone specifications and resale prices
│
├── model/
│   └── phone_resale_model.pkl    # Trained machine learning model and label encoder
│
├── app.py                        # Streamlit application script
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

🚀 How to Run the Application
1. Clone the Repository
git clone https://github.com/VarshaYadav634/Phone-Resale-Price-ML-Project.git
cd Phone-Resale-Price-ML-Project

2. Set Up a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies
pip install -r requirements.txt

4. Run the Streamlit App
streamlit run app.py


This command will start a local server, and you can access the application through your web browser.

📈 Model Evaluation

The model's performance is assessed using the following metrics:

Mean Absolute Error (MAE): Measures the average magnitude of errors in predictions, expressed in ₹.

R² Score: Indicates the proportion of variance in the dependent variable that is predictable from the independent variables.

These metrics provide insights into the model's accuracy and reliability in predicting resale prices.
