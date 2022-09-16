# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class ArrayTest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class array_of_string(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'array_of_string':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class array_array_of_integer(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.Int64Schema
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, tuple, ]], typing.List[typing.Union[MetaOapg.items, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'array_array_of_integer':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class array_array_of_model(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @classmethod
                            @property
                            def items(cls) -> typing.Type['ReadOnlyFirst']:
                                return ReadOnlyFirst
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['ReadOnlyFirst'], typing.List['ReadOnlyFirst']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ReadOnlyFirst':
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, tuple, ]], typing.List[typing.Union[MetaOapg.items, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'array_array_of_model':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "array_of_string": array_of_string,
                "array_array_of_integer": array_array_of_integer,
                "array_array_of_model": array_array_of_model,
            }
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["array_of_string"]) -> MetaOapg.properties.array_of_string: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["array_array_of_integer"]) -> MetaOapg.properties.array_array_of_integer: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["array_array_of_model"]) -> MetaOapg.properties.array_array_of_model: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing.Literal["array_of_string", "array_array_of_integer", "array_array_of_model", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["array_of_string"]) -> typing.Union[MetaOapg.properties.array_of_string, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["array_array_of_integer"]) -> typing.Union[MetaOapg.properties.array_array_of_integer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["array_array_of_model"]) -> typing.Union[MetaOapg.properties.array_array_of_model, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing.Literal["array_of_string", "array_array_of_integer", "array_array_of_model", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        array_of_string: typing.Union[MetaOapg.properties.array_of_string, tuple, schemas.Unset] = schemas.unset,
        array_array_of_integer: typing.Union[MetaOapg.properties.array_array_of_integer, tuple, schemas.Unset] = schemas.unset,
        array_array_of_model: typing.Union[MetaOapg.properties.array_array_of_model, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArrayTest':
        return super().__new__(
            cls,
            *args,
            array_of_string=array_of_string,
            array_array_of_integer=array_array_of_integer,
            array_array_of_model=array_array_of_model,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.read_only_first import ReadOnlyFirst
