def event_serializer(event) -> dict:
    return {
        "id": str(event["_id"]),
        "title": event["title"],
        "description": event.get("description"),
        "start_time": event["start_time"],
        "end_time": event["end_time"]
    }
