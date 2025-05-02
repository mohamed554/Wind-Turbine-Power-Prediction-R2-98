# Wind Turbine Power Prediction (R² ≈ 0.98)

Wind Turbine Power Prediction From Historical Data Using Machine Learning
![Wind Turbine SCADA Dataset](https://d12oja0ew7x0i8.cloudfront.net/images/Article_Images/ImageForArticle_21371_16457084545525256.jpg)

## Motivation

As the world shifts towards sustainable energy, optimizing wind turbine performance is crucial.  
This project leverages the Wind Turbine SCADA dataset to build machine-learning models that can accurately predict turbine power output.  
By doing so, we can improve energy yield forecasting  

---

## Project Structure

- **wind-turbine-power-prediction-r-98-19.ipynb**  
  Your exploratory notebook with data cleaning, feature engineering, modeling (CatBoost, XGBoost, etc.), and evaluation.

- **download_dataset.py**  
  A small script to fetch the raw CSV files from Kaggle.

- **requirements.txt**  
  Lists all Python dependencies required to run the notebook and the download script.

---

## Installation

Install the required libraries:
```bash
pip install -r requirements.txt
```

Download the data:
```bash
python download_dataset.py
```

Open the notebook:
```bash
jupyter notebook wind-turbine-power-prediction-r-98-19.ipynb
```

---

## License

MIT Commons Clause © mohamed554
