BLOCKED_WORDS = [
    "hack",
    "malware",
    "ransomware",
    "phishing",
    "credit card fraud",
    "wifi"
]

def is_safe(text):

    text = text.lower()

    for word in BLOCKED_WORDS:
        if word in text:
            return False

    return True