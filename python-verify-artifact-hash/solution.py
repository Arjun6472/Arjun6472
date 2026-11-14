import hashlib
import hmac

_SUPPORTED = ("sha256", "sha384", "sha512")


def verify_artifact(data: bytes, allowed: list[str]) -> bool:
    parsed = []
    for entry in allowed:
        algorithm, seprator, expected = entry.partition(":")
        if not seprator or algorithm not in _SUPPORTED:
            raise ValueError(f"unsupported hash entry: {entry!r}")
        parsed.append((algorithm, expected.lower()))
    for algorithm, expected in parsed:
        actual = hashlib.new(algorithm, data).hexdigest()
        if hmac.compare_digest(actual, expected):
            return True
    return False
    """
    `allowed` holds entries of the form "<algorithm>:<hex digest>",
    e.g. "sha256:2cf24d...". Supported algorithms: sha256, sha384, sha512.

    Return True if the digest of `data` matches ANY allowed entry
    (hex digits compare case-insensitively), otherwise False.
    An empty `allowed` list returns False.

    Raise ValueError if ANY entry is malformed (no ":" separator) or uses
    an unsupported algorithm, even if an earlier entry would have matched.
    Compare digests with hmac.compare_digest.
    """
    # TODO: implement this, see the Theory tab for the rules.
    pass
