import functools
from collections.abc import Callable
from typing import Any

from Programms.Mod.DesignTimeService import DesignTimeService


class DatabaseContext:

    def __init__(self):
        super().__init__()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"{cls.__name__} just derived from DatabaseContext!")
        original_init:Callable[[Any, Any, Any], None] | None = cls.__init__ if '__init__' in cls.__dict__ else None

        @functools.wraps(original_init or cls.__init__)
        def patched_init(self, *args_, **kwargs_):
            if original_init:
                original_init(self, *args_, **kwargs_)
            else:
                super(cls, self).__init__(*args_, **kwargs_)
            DesignTimeService.register_context_for_mapping(self)

        cls.__init__ = patched_init