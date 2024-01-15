from typing import Type, Union, Any

class Mediator:
    def __init__(self):
        self.handlers = {}

    def add_handler(self, event_type: Type, handler: callable):
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)

    def publish(self, event_type: Type, *args, **kwargs) -> Union[None, Any]:
        if event_type in self.handlers:
            for handler in self.handlers[event_type]:
                result = handler(*args, **kwargs)
                if result is not None:
                    return result
        return None

mediator = Mediator()
