from enum import Enum, auto
from functools import update_wrapper

from typing import Any, Type, Callable
from inspect import signature

from abc import ABC, abstractmethod


_entry_points:dict[type, list[str]] = {}


class DpiEntryPoint:

    def __init__(self, func):
        self.func = func
        self.owner_class = None

    def __set_name__(self, owner, method_name):
        self.owner_class = owner
        entry_point_names = _entry_points.get(self.owner_class, [])
        entry_point_names.append(method_name)
        _entry_points.update({self.owner_class: entry_point_names})

    def __get__(self, instance, owner):
        if instance is None:
            return self.func
        def wrapper(*args, **kwargs):
            return self.func(instance, *args, **kwargs)
        update_wrapper(wrapper, self.func)
        return wrapper


class Implementation(ABC):

    def __init__(self, object_type:Type, implementation_type:Type, collection:'ServiceCollection'):
        self.implementation_type = implementation_type
        self.object_type = object_type
        self.collection = collection

    @abstractmethod
    def get_service(self) -> Any:
        pass

    def _build_service(self, cls_t: Type) -> Any:
        entry_points: list[Callable]
        try:
            entry_points = [getattr(cls_t, p) for p in _entry_points[cls_t]]
        except KeyError:
            raise RuntimeError(f"""the type '{cls_t.__name__}' has no methods marked with 'DpiEntryPoint'""")
        entry_points = sorted(entry_points, key=lambda p: len(signature(p).parameters))
        for entry_point in entry_points:
            all_params_available: bool = True
            prams_to_use: list[Any] = []
            for param_name, param in signature(entry_point).parameters.items():
                if param_name == 'self':
                    continue
                val = self.collection.get_service(param.annotation)
                if val is None:
                    all_params_available = False
                    print(f"missing parameter of type:{param.annotation}")
                    break
                else:
                    prams_to_use.append(val)
            if all_params_available:
                instance = object.__new__(object)
                instance = cls_t.__new__(cls_t, instance)
                entry_point(instance, *prams_to_use)
                return instance
        raise RuntimeError(f"unable to construct the type '{cls_t.__name__}'")


class SingletonImplementation(Implementation):

    def __init__(self, object_type:Type, implementation_type:Type, collection:'ServiceCollection', instance:Any|None = None):
        super().__init__(object_type, implementation_type, collection)
        self.__singleton : Any | None = instance

    def get_service(self) -> Any:
        if self.__singleton is not None:
            return self.__singleton
        self.__singleton = self._build_service(self.object_type)
        return self.__singleton


class TransientImplementation(Implementation):

    def __init__(self, object_type:Type, implementation_type:Type, collection:'ServiceCollection'):
        super().__init__(object_type, implementation_type, collection)

    def get_service(self) -> Any:
        service = self._build_service(self.object_type)
        return service


class ServiceCollection:

    def __init__(self):
        self.__services:dict[Type,Implementation] = {}
        self.register_singleton_instance(ServiceCollection, self)

    def __getitem__(self, index:Type) -> Any | None:
        return self.get_service(index)

    def register_singleton_for_type(self, cls_t:Type, reg_t:Type):
        implementation = SingletonImplementation(cls_t, reg_t, self)
        self.__services[implementation.implementation_type] = implementation

    def register_singleton(self, cls_t:Type):
        self.register_singleton_for_type(cls_t, cls_t)

    def register_singleton_instance(self, cls_t:Type, instance:Any):
        implementation = SingletonImplementation(cls_t, cls_t, self, instance)
        self.__services[implementation.implementation_type] = implementation

    def register_transient(self, cls_t:Type):
        self.register_singleton_for_type(cls_t, cls_t)

    def register_transient_for_type(self, cls_t:Type, reg_t:Type):
        implementation = TransientImplementation(cls_t, reg_t, self)
        self.__services[implementation.implementation_type] = implementation

    def get_service(self, t:Type) -> Any | None:
        implementation = self.__services.get(t)
        if implementation is None:
            raise RuntimeError(f"no service for '{t.__name__}' was registered")
        service = implementation.get_service()
        return service
