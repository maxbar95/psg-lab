import csv
with open("F1.csv", encoding="utf-8") as f:
    matchs = list(csv.DictReader(f))

print(len(matchs), "matchs lus")
psg = 0
for m in matchs:
    dom = m["HomeTeam"]
    ext = m["AwayTeam"]
    bd = int(m["FTHG"])
    be = int(m["FTAG"])
    if dom == "Paris SG" and bd > be:
        psg += 3
    if ext == "Paris SG" and be > bd:
        psg += 3
    if dom == "Paris SG" and bd == be:
        psg += 1
    if ext == "Paris SG" and be == bd:
        psg += 1 
print("PSG :", psg, "points")