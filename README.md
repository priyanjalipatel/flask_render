
Deployment Summary: Breast Cancer Prediction Web App

Project Title: Breast Cancer Tumor Classifier
Model: Random Forest Classifier using top 15 features
Dataset: Breast Cancer Wisconsin Diagnostic Dataset (`sklearn.datasets.load_breast_cancer`)
Deployment Type: Web Application (HTML + Flask) + API
Hosting Platform: Render (Free Cloud Hosting)

---

Steps Followed

1. Data Preparation:

   * Loaded the breast cancer dataset from `scikit-learn`.
   * Selected the top 15 most relevant features using `SelectKBest` with `f_classif`.

2. Model Building:

   * Trained a compact `RandomForestClassifier` with `n_estimators=25`, `max_depth=6`.
   * Evaluated accuracy on test data (approx. \~94–96%).
   * Saved the model as `model.joblib` using `joblib.dump()`.

3. Web App Development:

   * Created a Flask app (`app.py`) to load the saved model and take 15 inputs via a form.
   * Designed a user-friendly HTML form (`index.html`) for the input interface.
   * Rendered prediction output directly on the webpage (malignant or benign).

4. API Integration:

   * Exposed a POST endpoint `/predict` to receive form data and return prediction results dynamically.

5. Deployment:

   * Used Render.com (free tier) to deploy the web app.
   * Created `requirements.txt`, `Procfile`, and pushed the project to GitHub.
   * Linked GitHub repository to Render for auto-deployment.

---

### Outcome

* A live, browser-accessible breast cancer classifier that accepts 15 feature values and predicts whether a tumor is malignant or benign.
* Fully functional on free cloud infrastructure (Render).
* Project includes both web form interface and API logic.

