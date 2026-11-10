def build_instances(cls, count: int) -> list:
    if count <= 0:
        return []
    return [cls() for _ in range(count)]
    """
    Return a list of `count` NEW instances of the class `cls`,
    each created by calling `cls()` with no arguments. Every
    instance must be a separate object. If count <= 0, return [].
    """
    pass


def attach_point(obj, x: int, y: int) -> None:
    obj.x = x
    obj.y = y
    """
    Set two attributes on `obj`: obj.x = x and obj.y = y. If the
    attributes already exist, replace their values. Return
    nothing.
    """
    pass


def same_class(a, b) -> bool:
    return type(a) is type(b)
    """
    Return True if `a` and `b` are instances of exactly the same
    class (compare type(a) and type(b) with `is`).
    """
    pass


def attribute_snapshot(obj) -> dict:
    return dict(obj.__dict__)
    """
    Return a NEW dictionary containing a copy of the attributes
    stored on `obj` (from obj.__dict__). Changing the returned
    dictionary must not change `obj`.
    """
    pass


class Rectangle:
    """
    A rectangle with a width and a height.

    __init__(self, width, height):
        Store the two arguments as instance attributes `width`
        and `height`.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass


class Account:
    """
    A simple account record.

    __init__(self, owner, balance=0, history=None):
        Store `owner` and `balance` as attributes.
        Store `history` as an attribute holding a list of past
        transaction amounts. If `history` is None, use a NEW
        empty list for THIS instance. If a list is given, store
        an independent copy of it (list(history)), so the
        instance does not share the caller's list.
    """

    def __init__(self, owner, balance=0, history=None):
        self.owner = owner
        self.balance = balance
        if history is None:
            history = []
        self.history = list(history)
        pass


def make_rectangle(width, height):
    return Rectangle(width, height)
    """
    Return a new Rectangle with the given width and height.
    """
    pass


def attributes_of(obj) -> dict:
    return dict(obj.__dict__)

    """
    Return a NEW dictionary that is a copy of obj.__dict__.
    """
    pass
