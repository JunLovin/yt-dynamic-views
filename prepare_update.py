def prepare_update_video_body(video_item):
    current_snippet = video_item["snippet"]
    current_statistics = video_item["statistics"]

    category_id = str(current_snippet["categoryId"])
    view_count = str(current_statistics["viewCount"])
    current_title = current_snippet["title"]

    new_title = f'This video has {view_count} views'

    description = current_snippet.get('description', '')
    tags = current_snippet.get('tags', [])

    updated_body = {
        'id': video_item['id'],
        'snippet': {
            'categoryId': category_id,
            'title': new_title,
            'description': description,
            'tags': tags
        },
    }
    return current_title, new_title, updated_body