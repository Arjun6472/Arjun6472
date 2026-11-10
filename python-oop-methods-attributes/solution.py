class Accumulator:
    """
    Keeps a running total.

    __init__(self):
        Set the attribute `total` to 0.

    add(self, x):
        Add `x` to self.total, then return `self` (so calls can
        be chained).

    value(self):
        Return the current total.
    """

    def __init__(self):
        self.total = 0
        pass

    def add(self, x):
        self.total += x
        return self
        pass

    def value(self):
        return self.total
        pass


def add_via_class(acc, x):
    return Accumulator.add(acc, x)
    """
    Add `x` to the Accumulator `acc` by calling the method
    THROUGH THE CLASS, not through the instance: use
    Accumulator.add(acc, x). Return the value returned by that
    call.
    """
    pass


def bound_method_target(method):
    return method.__self__
    """
    `method` is a bound method (for example acc.add). Return the
    instance it is bound to, using the method's __self__
    attribute.
    """
    pass


def chain_adds(acc, numbers: list):
    for number in numbers:
        acc.add(number)
    return acc
    """
    Add every number in `numbers` to `acc` using method calls
    that return `self`, building one chained expression per
    number (do not store intermediate results). Return `acc`.
    An empty list changes nothing.
    """
    pass


class Tracker:
    count = 0
    """
    Counts how many Tracker instances have been created.

    Define a CLASS attribute `count`, initialized to 0.

    __init__(self, label):
        Store `label` as an instance attribute, and increase the
        class attribute Tracker.count by 1 (assign through the
        class, not through self).
    """

    def __init__(self, label):
        self.label = label
        Tracker.count = Tracker.count + 1
        pass


def where_is_attribute(obj, attr: str) -> str:
    if attr in obj.__dict__:
        return "instance"
    if hasattr(obj, attr):
        return "class"
    return "missing"
    """
    Report where the attribute with the string label `attr` would
    be found for `obj`. Return exactly one of:
      "instance"  if it is in obj's own attributes (obj.__dict__)
      "class"     if it is not in obj's own attributes but is
                  found through the class (hasattr is True)
      "missing"   if the attribute does not exist at all
    """
    pass


def shadow_count(tracker, value: int) -> None:
    tracker.count = value
    """
    Make the given Tracker instance report `value` for `.count`
    WITHOUT changing the shared class attribute Tracker.count:
    assign the attribute through the instance. Return nothing.
    """
    pass
