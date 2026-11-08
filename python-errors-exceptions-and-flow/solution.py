def validate_age(age: int) -> int:
    if not 0 <= age <= 150:
        raise ValueError("age must be between 0 and 150")
    return age
    
    """
    Return `age` if it is an int from 0 to 150 inclusive.
    Otherwise raise a ValueError whose message is exactly
      "age must be between 0 and 150"
    """
    pass


def level_three(log: list) -> None:
    log.append("L3 start")
    raise RuntimeError("boom")
    log.append("L3 end")
    
    """
    Do these steps, in order:
      1. Append the string "L3 start" to `log`.
      2. Raise a RuntimeError with the message "boom".
      3. Append the string "L3 end" to `log`.
    (Step 3 must be written, and it must never run.)
    """
    pass


def level_two(log: list) -> None:
    log.append("L2 start")
    level_three(log)
    log.append("L2 end")
    """
    Append "L2 start" to `log`, call level_three(log), then
    append "L2 end" to `log`.
    """
    pass


def level_one(log: list) -> None:
    log.append("L1 start")
    level_two(log)
    log.append("L1 end")
    """
    Append "L1 start" to `log`, call level_two(log), then
    append "L1 end" to `log`.
    """
    pass


def first_element(items: list):
    return items[0]
    """
    Return the first element of `items` by indexing position 0.
    Do not check for an empty list: an empty list should make
    Python itself raise an IndexError.
    """
    pass
