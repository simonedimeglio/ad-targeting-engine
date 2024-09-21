import json
from typing import Dict, List
import random

class AdTargetingEngine:
    """
    Main class for the Ad Targeting Engine.
    Handles loading of user and ad data, and performs ad targeting based on user profiles.
    """

    def __init__(self):
        """
        Initialize the AdTargetingEngine by loading user and ad data from JSON files.
        This simulates a database or data store in a real-world scenario.
        """
        self.users = self._load_json('data/users.json')
        self.ads = self._load_json('data/ads.json')

    def _load_json(self, file_path: str) -> Dict:
        """
        Helper method to load JSON data from a file.
        
        Args:
            file_path (str): Path to the JSON file.
        
        Returns:
            Dict: Loaded JSON data as a dictionary.
        """
        with open(file_path, 'r') as file:
            return json.load(file)

    def get_user_data(self, user_id: str) -> Dict:
        """
        Retrieve user data based on the user ID.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            Dict: User data including age and interests, or an empty dict if user not found.
        """
        return self.users.get(user_id, {})

    def select_ad(self, user_data: Dict) -> Dict:
        """
        Select an appropriate ad based on the user's data.
        
        Args:
            user_data (Dict): User profile data including age and interests.
        
        Returns:
            Dict: Selected ad data, or an empty dict if no matching ad is found.
        """
        matching_ads = []
        for ad in self.ads:
            if self._matches_targeting_criteria(user_data, ad['targeting']):
                matching_ads.append(ad)
        
        # Randomly select one of the matching ads to introduce variety
        return random.choice(matching_ads) if matching_ads else {}

    def _matches_targeting_criteria(self, user_data: Dict, targeting: Dict) -> bool:
        """
        Check if a user matches the targeting criteria for an ad.
        
        Args:
            user_data (Dict): User profile data.
            targeting (Dict): Ad targeting criteria.
        
        Returns:
            bool: True if the user matches the targeting criteria, False otherwise.
        """
        age = user_data.get('age', 0)
        interests = set(user_data.get('interests', []))

        # Check if user's age falls within the target age range
        age_match = targeting['age_range'][0] <= age <= targeting['age_range'][1]
        
        # Check if user has at least one interest that matches the ad's target interests
        interests_match = bool(interests & set(targeting['interests']))

        # Both age and interests must match for the ad to be considered
        return age_match and interests_match

    def serve_ad(self, user_id: str) -> Dict:
        """
        Main method to serve an ad to a user.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            Dict: Contains user data and the served ad information.
        """
        user_data = self.get_user_data(user_id)
        selected_ad = self.select_ad(user_data)
        
        return {
            "user_data": user_data,
            "ad_served": {
                "category": selected_ad.get('category', ''),
                "message": selected_ad.get('message', '')
            }
        }