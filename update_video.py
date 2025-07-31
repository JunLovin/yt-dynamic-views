def update_video_title(youtube_service, updated_body):
    request = youtube_service.videos().update(
        part="snippet",
        body=updated_body
    )

    response = request.execute()
    return response['snippet']['title']