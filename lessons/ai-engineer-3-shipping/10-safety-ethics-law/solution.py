PROHIBITED = {"social_scoring", "harmful_manipulation", "face_scraping", "emotion_recognition_work_school"}
HIGH = {"hiring", "student_grading", "credit_scoring", "essential_services", "critical_infrastructure",
        "policing", "migration", "medical_device"}
TRANSPARENCY = {"chatbot", "generated_media"}


def risk_tier(use):
    if len(use & PROHIBITED) > 0:
        return "prohibited"
    if len(use & HIGH) > 0:
        return "high"
    if len(use & TRANSPARENCY) > 0:
        return "transparency"
    return "minimal"


def disclose(answer):
    tag = "[AI-generated] "
    if answer.startswith(tag):
        return answer
    return tag + answer


def selection_rates(decisions):
    totals = {}
    accepted = {}
    for group, ok in decisions:
        totals[group] = totals.get(group, 0) + 1
        accepted[group] = accepted.get(group, 0)
        if ok:
            accepted[group] = accepted[group] + 1
    rates = {}
    for group in totals:
        rates[group] = accepted[group] / totals[group]
    return rates


def four_fifths_ok(decisions):
    rates = selection_rates(decisions)
    top = max(rates.values())
    for group in rates:
        if rates[group] < 0.8 * top:
            return False
    return True


print(risk_tier({"chatbot", "hiring"}), disclose("Hello!"))
d = [("A", True)] * 50 + [("A", False)] * 50 + [("B", True)] * 30 + [("B", False)] * 70
print(selection_rates(d), four_fifths_ok(d))
