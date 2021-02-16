testdata = {
    'NewZealand': {'position': 1, "matches": 27, "points": 3198, "rating": 118},
    'India': {'position': 2, "matches": 32, "points": 3000, "rating": 108},
    'Australia': {'position': 3, "matches": 31, "points": 3198, "rating": 100},
    'England': {'position': 4, "matches": 26, "points": 2098, "rating": 90},
    'Pakistan': {'position': 5, "matches": 29, "points": 3001, "rating": 85},
    'South Africa': {'postion': 6, "matches": 27, "points": 3199, "rating": 80},
    'Srilanka': {'postion': 7, "matches": 28, "points": 2000, "rating": 70},
    'West Indies': {'postion': 8, "matches": 30, "points": 1500, "rating": 60},
    'Bangladesh': {'postion': 9, "matches": 31, "points": 1400, "rating": 50},
}

# print(testdata['India']['position'])

team=input("Enter the team name")
property=input("Enter property name")

if team in testdata:
    if property in testdata[team]:
        print("Team Name:",team)
        print(property,":",testdata[team][property])
    else:
        print("OOps, That property is not a valid property")
else:
    print("OOps, Check the team name")
