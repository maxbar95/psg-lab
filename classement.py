import csv
with open("F1.csv", encoding="utf-8") as f:
    matchs = list(csv.DictReader(f))

print(len(matchs), "matchs lus")
points = {}
for m in matchs:
    dom = m["HomeTeam"]
    ext = m["AwayTeam"]
    bd = int(m["FTHG"])
    be = int(m["FTAG"])
    points.setdefault(dom, 0)
    points.setdefault(ext, 0)
    if bd > be:
        points[dom] += 3
    if be > bd:
        points[ext] += 3
    if bd == be:
        points[dom] += 1
        points[ext] += 1

classement = sorted(points.items(), key=lambda x: x[1], reverse=True)
for rang, (equipe, pts) in enumerate(classement, start=1):
    print(rang, equipe, pts)