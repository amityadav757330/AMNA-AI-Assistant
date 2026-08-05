"""
=========================================
AMNA AI Assistant
User Profile Model
=========================================
"""


class UserProfile:

    def __init__(self):

        self.name = ""

        self.city = ""

        self.college = ""

        self.favorite_language = ""

        self.favorite_ide = ""

        self.interests = []

    # -------------------------
    # Convert object to dictionary
    # -------------------------

    def to_dict(self):

        return {
            "name": self.name,
            "city": self.city,
            "college": self.college,
            "favorite_language": self.favorite_language,
            "favorite_ide": self.favorite_ide,
            "interests": self.interests
        }

    # -------------------------
    # Load dictionary
    # -------------------------

    @classmethod
    def from_dict(cls, data):

        profile = cls()

        profile.name = data.get("name", "")

        profile.city = data.get("city", "")

        profile.college = data.get("college", "")

        profile.favorite_language = data.get("favorite_language", "")

        profile.favorite_ide = data.get("favorite_ide", "")

        profile.interests = data.get("interests", [])

        return profile

    # -------------------------
    # Update Profile
    # -------------------------

    def update(self, data):

        for key, value in data.items():

            if key == "interest":

                if value not in self.interests:
                    self.interests.append(value)

                continue

            if hasattr(self, key):

                setattr(self, key, value)