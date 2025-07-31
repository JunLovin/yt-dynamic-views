def get_video_data(youtube_service, video_id):
    request = youtube_service.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()

    if not response['items']:
        raise ValueError(f"Video with ID: {video_id} not found")

    return response['items'][0]
