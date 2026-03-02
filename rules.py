# ----------------------------------
# Stress & Sleep Recommendation Rules
# ----------------------------------

def get_stress_tip(stress_level: str) -> str:
    if stress_level == "Low":
        return "Your stress level is low. Maintain your routine and continue regular physical activity."

    elif stress_level == "Medium":
        return "Your stress level is moderate. Consider short breaks, light exercise, and structured daily planning."

    elif stress_level == "High":
        return "Your stress level is high. Practice deep breathing, reduce workload where possible, and prioritize rest."

    else:
        return "Stress level unavailable."


def get_sleep_tip(sleep_quality: str) -> str:
    if sleep_quality == "Good":
        return "Your sleep quality is good. Maintain a consistent bedtime and healthy lifestyle habits."

    elif sleep_quality == "Poor":
        return "Your sleep quality is poor. Reduce screen time before bed and aim for 7–8 hours of sleep."

    else:
        return "Sleep quality unavailable."