# 🚕 Taxi Fare Prediction (From Scratch)

A **multivariate linear regression model implemented from scratch** to predict taxi fares using real-world Chicago taxi trip data.  
Built to understand **machine learning fundamentals**, not production pricing systems.

---

## 📊 Dataset
- **Source:** Chicago Taxi Trips  
- **Size:** ~30,000 records  
- **Features:** `TRIP_MILES`, `TRIP_SECONDS`  
- **Target:** `FARE` (excluding tips, tolls, extras)

---

## 🧠 Model
Linear regression model trained using **manual gradient descent**:

Fare = m1*x + m2*x2 + c

(x - Trip Miles, x2 - Trip Seconds)


### Key Concepts
- Gradient Descent (from scratch)
- Feature normalization (z-score)
- Train–test separation
- Prediction on unseen data
- Avoiding data leakage

---

## ⚙️ Feature Normalization
Both features are normalized using training data statistics:

x_norm = (x − mean) / std


Normalization parameters are reused during testing and prediction.

---

## 🧪 Training & Testing
- **Training:** ~30,000 records  
- **Testing:** 636 unseen records  
- Optimized using **Mean Squared Error**

---

## 📈 Visualization
Model performance is visualized using an **Actual vs Predicted Fare** scatter plot.

---

## 🖥️ Example Prediction

Enter trip miles: 10
Enter trip seconds: 2400
Predicted Fare: $30.80