import ast
import inspect
from collections.abc import Callable
from types import CodeType
from typing import Any

from Programms.Mod.DatabaseCollection import DatabaseCollection
from Programms.Mod.DatabaseContext import DatabaseContext


class DesignTimeService:
    IS_DESIGN_TIME:bool = False
    __contexts_to_map:list['DatabaseContext'] = []
    __registered_types:list[type] = []
    __buffered_types:list[type] = []

    @staticmethod
    def register_context_for_mapping(context:DatabaseContext):
        properties:dict[str, Any] = context.__dict__
        for prop in properties.keys():
            if isinstance(properties[prop], DatabaseCollection):
                DesignTimeService.__contexts_to_map.append(properties[prop])

    @staticmethod
    def on_initialized():
        for context in DesignTimeService.__contexts_to_map:
            context

    @staticmethod
    def register_data_type(t:type):
        if t not in DesignTimeService.__registered_types:
            DesignTimeService.__registered_types.append(t)

    @staticmethod
    def is_type_registered(t:type):
        return t in DesignTimeService.__registered_types



class Expr:
    """Records operations instead of executing them."""
    def __init__(self, name="obj"):
        self.ops = []
        self._name = name

    def __getattr__(self, name):
        child = Expr(f"{self._name}.{name}")
        return child

    def __eq__(self, other):
        node = ExprNode(self, "==", other)
        self.ops.append(node)
        return node

    def __ne__(self, other):
        return ExprNode(self, "!=", other)

    def __lt__(self, other):
        node = ExprNode(self, "<",  other)
        self.ops.append(node)
        return node

    def __le__(self, other):
        node = ExprNode(self, "<=", other)
        self.ops.append(node)
        return node

    def __gt__(self, other):
        node = ExprNode(self, ">",  other)
        self.ops.append(node)
        return node

    def __ge__(self, other):
        node = ExprNode(self, ">=", other)
        self.ops.append(node)
        return node

    def __repr__(self):
        node = self._name
        self.ops.append(node)
        return node


class ExprNode:
    """Represents a comparison expression."""
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self, obj):
        """Actually execute the expression against a real object."""
        left_val = obj
        for part in str(self.left).split(".")[1:]:  # skip "obj"
            left_val = getattr(left_val, part)
        ops = {
            "==": lambda a, b: a == b,
            "!=": lambda a, b: a != b,
            "<":  lambda a, b: a < b,
            "<=": lambda a, b: a <= b,
            ">":  lambda a, b: a > b,
            ">=": lambda a, b: a >= b,
        }
        return ops[self.op](left_val, self.right)

    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"


def inspect_lambda(fn):
    proxy = Expr("obj")
    expr = fn(proxy)
    return expr

def test_function() -> int:
    return 5

# Usage
#lam = lambda x: x > test_function() and x < 10

#ops = inspect_lambda(lam)
#print(ops)  # [('>', 5), ('<', 10)]


import textwrap
def test_compile_with_lambda():
    lam = lambda x: x > test_function() and x < 10
    code_str = """
    def bump(x):
        return x + 1

    debug_me = (lambda y: bump(y))(41)
    print();
    print(debug_me)

    """

    def recursive_dump(ast_tree:ast.Module):
        for b in ast_tree.body:
            print(ast.dump(b))
            if hasattr(b, 'value') and hasattr(b.value, 'body'):
                recursive_dump(b.value.body.values)

    code_str = inspect.getsource(lam)
    print(code_str)
    dedented_code_str = textwrap.dedent(code_str)
    tree = ast.parse(dedented_code_str, mode='exec')
    recursive_dump(tree)
        #if isinstance(b, ast.Expr):
        #    print(b.value)
        #if isinstance(b, ast.Assign):

test_compile_with_lambda()