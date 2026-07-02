def analyze(text):
    threats=[]
    if "QR" not in text: threats.append("QR code missing")
    return threats
