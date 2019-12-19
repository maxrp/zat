"""Utilities for differential behavior based on interactivity."""


def is_interactive():
    """Returns True if interactive, false if not."""
    import __main__ as main
    return not hasattr(main, '__file__')
