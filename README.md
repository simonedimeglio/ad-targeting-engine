# Ad Targeting Engine Mockup

## Overview

This project implements a mockup of an ad targeting engine, demonstrating how user data can be used to serve personalized advertisements. It uses Python and Flask to create a basic API that simulates the ad targeting process.

## Features

- Simulates user profiles with age and interests
- Matches ads to users based on targeting criteria
- Provides a simple API endpoint to serve targeted ads

## Technologies Used

- Python 3.7+
- Flask
- JSON for data storage

## Installation and Usage

1. Clone the repository:

   ```
   git clone https://github.com/simonedimeglio/ad-targeting-engine-mockup.git
   ```

2. Navigate to the project directory:

   ```
   cd ad-targeting-engine-mockup
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```
   python app.py
   ```

5. Access the API at `http://localhost:5000/serve_ad/<user_id>`, where `<user_id>` is one of the user IDs in the `users.json` file (e.g., user1, user2, user3).

## API Endpoint

- `GET /serve_ad/<user_id>`: Returns user data and a served ad based on the user's profile.

Example response:

```json
{
  "user_data": {
    "age": 25,
    "interests": ["tech", "gaming", "sports"]
  },
  "ad_served": {
    "category": "gaming",
    "message": "Buy the latest console!"
  }
}
```

## Customization

To modify the available users or ads, edit the JSON files in the `data/` directory.

## Future Enhancements

- Implement more complex targeting algorithms
- Add more user attributes for targeting (e.g., location, browsing history)
- Create a front-end interface to visualize the targeting process
- Implement real-time user data updates

## Contributing

Contributions to improve the mockup or extend its functionality are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created by [Simone Di Meglio](https://github.com/simonedimeglio)
