from typing import Type

class BaseEvent:
    pass

class ItemCreatedEvent(BaseEvent):
    def __init__(self, item_id: int):
        self.item_id = item_id

class ItemListedEvent(BaseEvent):
    pass

def publish_event(mediator, event: Type, *args, **kwargs):
    return mediator.publish(event, *args, **kwargs)
