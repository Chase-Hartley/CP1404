"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():

    score = float(input("Enter score: "))
    print(check_score(score))


def check_score(score):
    if score > 100:
        return "invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score > 0 < 50:
        return "Failed"
    else:
        return "invalid score"


main()
