from typing import Any, Mapping, Optional, Sequence, SupportsInt, Tuple, Union, overload

class Event:
    type: int
    @overload
    def __init__(self, type: int, dict: Mapping[str, Any]) -> None: ...
    @overload
    def __init__(self, type: int, **attributes: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

_EventTypes = Union[SupportsInt, Tuple[SupportsInt, ...], Sequence[SupportsInt]]

def pump() -> None: ...
def get(eventtype: _EventTypes = ..., pump: bool = ...) -> Sequence[Event]: ...
def poll() -> Event: ...
def wait() -> Event: ...
def peek(eventtype: _EventTypes = ..., pump: bool = ...) -> bool: ...
def clear(eventtype: _EventTypes = ..., pump: bool = ...) -> None: ...
def event_name(type: int) -> str: ...
def set_blocked(type: Optional[_EventTypes]) -> None: ...
def set_allowed(type: Optional[_EventTypes]) -> None: ...
def get_blocked(type: int) -> bool: ...
def set_grab(grab: bool) -> None: ...
def get_grab() -> bool: ...
def post(event: Event) -> None: ...
def custom_type() -> int: ...

