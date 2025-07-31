# YouTube Dynamic Video Title Updater

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python script designed to automatically update a YouTube video's title to display its current view count. This script runs continuously, checking for view increments and updating the title to reflect the latest statistics, helping to create dynamic and engaging content.

## Features

* **Automated View Count Display:** Keeps your video title updated with the latest view count.
* **Persistent Authentication:** Uses OAuth2 refresh tokens to maintain access without requiring repeated manual logins.
* **Quota Optimization:** Smartly updates the title only when the view count changes, conserving your YouTube Data API daily quota.
* **Preserves Metadata:** Ensures existing video descriptions, tags, and other snippet data are not lost during updates.
* **Configurable Update Interval:** Easily adjust how often the script checks for new views.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.x
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/JunLovin/yt-dynamic-views.git](https://github.com/JunLovin/yt-dynamic-views.git)
    cd yt-dynamic-views
    ```
2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### YouTube API Setup

1.  **Enable the YouTube Data API v3:**
    * Go to the [Google Cloud Console](https://console.cloud.google.com/).
    * Create a new project or select an existing one.
    * Navigate to "APIs & Services" > "Dashboard".
    * Click "+ Enable APIs and Services" and search for "YouTube Data API v3". Enable it.

2.  **Create OAuth Consent Screen:**
    * In the Google Cloud Console, go to "APIs & Services" > "OAuth consent screen".
    * Configure your consent screen (User type: External, App name, User support email, Developer contact information). You usually only need basic information for personal use.

3.  **Create OAuth 2.0 Client ID:**
    * Go to "APIs & Services" > "Credentials".
    * Click "+ Create Credentials" > "OAuth client ID".
    * Select "Desktop app" as the application type.
    * Give it a name (e.g., `YouTube Updater Desktop`).
    * Click "Create".
    * A dialog will appear with your Client ID and Client Secret. Click "Download JSON".
    * **Rename the downloaded JSON file to `client_secret.json`** and place it in the root directory of your project (where `main.py` is located).

## Usage

1.  **Update `create a .env file` (Just like .env.example):**
    * Open `.env`.
    * Add in `VIDEO_ID=` your actual YouTube video ID.

2.  **Run the script for the first time:**
    ```bash
    python main.py
    ```
    * The first time you run it, a browser window will open. You will need to sign in with your Google account and grant the necessary permissions for the script to manage your YouTube videos.
    * After successful authentication, `token.json` will be created in your project directory. This file stores your credentials securely for future runs. **Do NOT share this file or upload it to GitHub!**

3.  **Continuous Operation:**
    * Once the `token.json` file is created, the script will run continuously in your terminal, checking for view count updates every 15 minutes.
    * It will print status messages to the console indicating checks and updates.

## Project Structure

Your project is structured to separate concerns, making it more organized:

```plaintext
your-repo-name/
├── venv/                       # Python Virtual Environment (ignored by .gitignore)
├── .gitignore                  # Specifies files/directories to ignore in Git
├── client_secret.json          # Your downloaded API credentials (ignored by .gitignore)
├── main.py                     # The main script that orchestrates the updates
├── token.json                  # Stores your authentication tokens (generated, ignored by .gitignore)
├── auth.py                     # (Optional: Could contain get_authenticated_service function)
├── video_data.py               # (Optional: Could contain get_video_data function)
├── prepare_update.py           # (Optional: Could contain prepare_video_update_body function)
└── update_video.py             # (Optional: Could contain update_video_title function)
└── requirements.txt            # Lists Python dependencies
```

## Troubleshooting

- `AttributeError: 'str' object has no attribute 'keys'` **or browser opening** repeteadly: This indicates an issue with token.json. Delete the token.json file and run the script again to re-authenticate and regenerate it.
- **Video title not updating despite views changing in YouTube Studio:**
    - Ensure your `VIDEO_ID` in `.env` is correct.
    - Verify your internet connection.
    - Be aware that for very new videos or videos with extremely low view counts, YouTube's API might have a slight delay in reflecting the absolute latest view count compared to YouTube Studio. Performing an action like liking or commenting on the video can sometimes "poke" the API to refresh faster.
    - Check your [Google Cloud Console API Dashboard](https://console.cloud.google.com/apis/dashboard) for the YouTube Data API v3 to ensure you haven't exceeded your daily quota (unlikely for a single video).
-**"An HTTP error occurred"**: Check the HTTP status code (e.g., 403 Forbidden means permission issue, 404 Not Found means video ID might be wrong). The error message will often provide more details.

## Contributing

Feel free to fork this repository, open issues, or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
[Google Developers](https://developers.google.com/youtube/v3/) for the YouTube Data API.

[google-auth-oauthlib](https://github.com/googleapis/google-auth-library-python-oauthlib) for seamless OAuth2 integration.