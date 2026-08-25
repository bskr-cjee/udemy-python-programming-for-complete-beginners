# 1. Create a dictionary
user_profile = {
    "username": "coder_99",
    "email": "coder@example.com",
    "experience_years": 4,
    "is_active": True,
    "skills": ["Python", "SQL", "Git"]
}

# 2. Access values using keys
print(user_profile["username"])          # Output: coder_99
print(user_profile.get("email"))         # Output: coder@example.com

# 3. Add a new key-value pair
user_profile["location"] = "New York"

# 4. Modify an existing value
user_profile["experience_years"] = 5

# 5. Remove a key-value pair
del user_profile["is_active"]

# 6. Check if a key exists
if "skills" in user_profile:
    print("Skills are listed.")

# 7. Loop through the dictionary
print("\nLooping through the dictionary")
for key, value in user_profile.items():
    print(f"{key}: {value}")
