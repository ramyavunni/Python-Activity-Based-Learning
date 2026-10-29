
teams = {}

n = int(input("Enter number of teams: "))

for i in range(n):
    name = input("Enter team name: ")
    teams[name] = [0, 0, 0, 0]  # Points, GF, GA, GD

m = int(input("Enter number of matches: "))

for i in range(m):
    a, b = input("Enter teams and goals (A B GA GB): ").split()
    ga, gb = int(input("Enter goals for " + a + ": ")), int(input("Enter goals for " + b + ": "))

    teams[a][1] += ga
    teams[a][2] += gb
    teams[b][1] += gb
    teams[b][2] += ga

    if ga > gb:
        teams[a][0] += 3
    elif gb > ga:
        teams[b][0] += 3
    else:
        teams[a][0] += 1
        teams[b][0] += 1

for name in teams:
    teams[name][3] = teams[name][1] - teams[name][2]

ranking = sorted(teams.items(),
                 key=lambda x: (x[1][0], x[1][3], x[1][1]),
                 reverse=True)

print("\n--- TOURNAMENT RANKINGS ---")
print("Rank Team Points GF GA GD")

for i, (name, s) in enumerate(ranking, 1):
    print(i, name, s[0], s[1], s[2], s[3])

