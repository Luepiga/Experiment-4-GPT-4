
def build_prompt(profile, feedback=""):
    return f"""
You are a personalized recommendation assistant.

USER PROFILE
Name: {profile['name']}
Age: {profile['age']}
Background: {profile['background']}
Interests: {profile['interests']}
Skill Level: {profile['skill_level']}
Preference: {profile['preference']}
Goal: {profile['goal']}
Number Required: {profile['number']}

USER FEEDBACK:
{feedback if feedback else "No feedback provided."}

Generate exactly {profile['number']} personalized recommendations.

Prioritize the user's stated interests, skill level, goal,
and preferred learning style. Respect all exclusions in feedback.

For each recommendation provide:
1. Name
2. Suitability score from 0 to 100
3. Reason it matches the user's profile
4. Explanation of its usefulness

Rank the recommendations from highest to lowest suitability.
Use clear headings and numbered items.
Do not claim scores are objectively measured.
"""
