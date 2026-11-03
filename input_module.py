
def collect_profile():
    print("\n===== USER PROFILE COLLECTION =====")

    profile = {
        "name": input("Enter Name: ").strip(),
        "age": input("Enter Age: ").strip(),
        "background": input("Educational/Professional Background: ").strip(),
        "interests": input("Enter Interests: ").strip(),
        "skill_level": input("Enter Skill Level: ").strip(),
        "preference": input("Preferred Category/Type: ").strip(),
        "goal": input("Enter Goal: ").strip()
    }

    while True:
        try:
            profile["number"] = int(
                input("Number of Recommendations: ")
            )
            if profile["number"] > 0:
                break
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

    return profile
