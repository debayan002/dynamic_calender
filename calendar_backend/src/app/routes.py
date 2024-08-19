from fastapi import APIRouter, HTTPException
from app.database import event_collection
from app.models import EventModel
from app.schemas import event_serializer
from bson import ObjectId

router = APIRouter()

# Create event
@router.post("/events/")
async def create_event(event: EventModel):
    event_dict = event.dict()
    new_event = await event_collection.insert_one(event_dict)
    return event_serializer(await event_collection.find_one({"_id": new_event.inserted_id}))

# Get all events
@router.get("/events/")
async def get_events():
    events = await event_collection.find().to_list(1000)
    return [event_serializer(event) for event in events]

# Update event
@router.put("/events/{event_id}")
async def update_event(event_id: str, event: EventModel):
    updated_event = await event_collection.update_one({"_id": ObjectId(event_id)}, {"$set": event.dict()})
    if updated_event.modified_count == 1:
        return {"msg": "Event updated successfully"}
    raise HTTPException(status_code=404, detail="Event not found")

# Delete event
@router.delete("/events/{event_id}")
async def delete_event(event_id: str):
    delete_result = await event_collection.delete_one({"_id": ObjectId(event_id)})
    if delete_result.deleted_count == 1:
        return {"msg": "Event deleted successfully"}
    raise HTTPException(status_code=404, detail="Event not found")
