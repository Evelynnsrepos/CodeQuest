PROHIBITED = {"social_scoring", "harmful_manipulation", "face_scraping", "emotion_recognition_work_school"}
HIGH = {"hiring", "student_grading", "credit_scoring", "essential_services", "critical_infrastructure",
        "policing", "migration", "medical_device"}
TRANSPARENCY = {"chatbot", "generated_media"}


def risk_tier(use):
    return "minimal"


def disclose(answer):
    return answer


def selection_rates(decisions):
    return {}


def four_fifths_ok(decisions):
    return True


print(risk_tier({"chatbot", "hiring"}), disclose("Hello!"))
d = [("A", True)] * 50 + [("A", False)] * 50 + [("B", True)] * 30 + [("B", False)] * 70
print(selection_rates(d), four_fifths_ok(d))
