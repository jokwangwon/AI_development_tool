"""FAIL fixture — §9.4 동적 import (importlib.import_module).

기대 결과: scanner 가 'dynamic-importlib:litellm' 보고.
"""
import importlib


def lazy_load_provider() -> object:
    return importlib.import_module("litellm")  # 의도적 위반
