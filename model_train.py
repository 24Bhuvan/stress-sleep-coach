import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from utils.preprocessing import load_data, create_targets


DATA_PATH = "data.csv"
MODEL_PATH = "model.pkl"


def main():
    # -----------------------
    # Load + Prepare Data
    # -----------------------
    df = load_data(DATA_PATH)
    df = create_targets(df)

    feature_cols = [
        "Gender",
        "Age",
        "Occupation",
        "Sleep Duration",
        "Physical Activity Level",
        "BMI Category",
    ]

    X = df[feature_cols]
    y_stress = df["Stress_Class"]
    y_sleep = df["Sleep_Class"]

    categorical_cols = ["Gender", "Occupation", "BMI Category"]
    numeric_cols = ["Age", "Sleep Duration", "Physical Activity Level"]

    # -----------------------
    # Preprocessing Pipeline
    # -----------------------
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", StandardScaler(), numeric_cols),
        ]
    )

    # -----------------------
    # Build Pipelines
    # -----------------------
    stress_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )

    sleep_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )

    # -----------------------
    # Train-Test Split (Stratified)
    # -----------------------
    X_train, X_test, y_stress_train, y_stress_test = train_test_split(
        X, y_stress, test_size=0.2, random_state=42, stratify=y_stress
    )

    X_train2, X_test2, y_sleep_train, y_sleep_test = train_test_split(
        X, y_sleep, test_size=0.2, random_state=42, stratify=y_sleep
    )

    # -----------------------
    # Train
    # -----------------------
    stress_pipeline.fit(X_train, y_stress_train)
    sleep_pipeline.fit(X_train2, y_sleep_train)

    # -----------------------
    # Evaluate
    # -----------------------
    stress_preds = stress_pipeline.predict(X_test)
    sleep_preds = sleep_pipeline.predict(X_test2)

    print(f"Stress Model Accuracy: {accuracy_score(y_stress_test, stress_preds):.2f}")
    print(f"Sleep Model Accuracy: {accuracy_score(y_sleep_test, sleep_preds):.2f}")

    # -----------------------
    # Save full pipelines
    # -----------------------
    joblib.dump(
        {
            "stress_model": stress_pipeline,
            "sleep_model": sleep_pipeline,
        },
        MODEL_PATH,
    )

    print("Models saved as model.pkl")


if __name__ == "__main__":
    main()