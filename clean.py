import pandas as pd

INPUT_FILE = "Sleep_health_and_lifestyle_dataset.csv"
OUTPUT_FILE = "data.csv"

def main():
    df = pd.read_csv(INPUT_FILE)

    df = df[
        [
            "Gender",
            "Age",
            "Occupation",
            "Sleep Duration",
            "Physical Activity Level",
            "BMI Category",
            "Stress Level",
            "Quality of Sleep",
        ]
    ]

    df = df.drop_duplicates()
    df = df.dropna()

    df.to_csv(OUTPUT_FILE, index=False)
    print("Cleaned data saved as data.csv")

if __name__ == "__main__":
    main()