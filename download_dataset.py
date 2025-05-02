"""
download_dataset.py

Script to download the Wind Turbine SCADA dataset using kagglehub.
"""

import kagglehub

def main():
    path = kagglehub.dataset_download("berkerisen/wind-turbine-scada-dataset")
    print("Path to dataset files:", path)

if __name__ == "__main__":
    main()
