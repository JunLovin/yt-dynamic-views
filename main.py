# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
from dotenv import load_dotenv
from prepare_update import prepare_update_video_body
from video_data import get_video_data
from auth import get_authenticated_service
from update_video import update_video_title

import googleapiclient.errors
import time

load_dotenv()

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

VIDEO_ID = os.getenv('VIDEO_ID')


def run_updater_loop():
    youtube = get_authenticated_service()

    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{timestamp}] Starting video checking")

        try:
            video_item = get_video_data(youtube, VIDEO_ID)
            current_title, new_title, updated_body = prepare_update_video_body(video_item)

            print(f"{timestamp} - Current video title: {current_title}")
            print(f"{timestamp} - View from API: {video_item['statistics']['viewCount']}")

            if current_title == new_title:
                print(f"{timestamp} - Title is up-to-date '{new_title}'")
            else:
                print(f"{timestamp} - Title change detected: Old='{current_title}', New='{new_title}'. Proceeding with update...")
                updated_title = update_video_title(youtube, updated_body)
                print(f"{timestamp} - Video title updated successfully!")
                print(f"{timestamp} - New title: '{updated_title}'")

        except ValueError as ve:
            print(f"{timestamp} - Error during data retrieval: {ve}")
        except googleapiclient.errors.HttpError as e:
            print(f"{timestamp} - An HTTP error {e.resp.status} occurred:\n{e.content.decode('utf-8')}")
        except Exception as e:
            print(f"{timestamp} - Unexpected error: {e}")

        finally:
            print(f"{timestamp} - Waiting {900/60} minutes for the check...")
            time.sleep(900)


if __name__ == "__main__":
    run_updater_loop()
