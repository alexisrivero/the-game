def hook(callback, suppress=False, on_remove=lambda: None):
    """
    Installs a global listener on all available keyboards, invoking `callback`
    each time a key is pressed or released.

    The event passed to the callback is of type `keyboard.KeyboardEvent`,
    with the following attributes:
    - `name`: an Unicode representation of the character (e.g. "&") or
    description (e.g.  "space"). The name is always lower-case.
    - `scan_code`: number representing the physical key, e.g. 55.
    - `time`: timestamp of the time the event occurred, with as much precision
    as given by the OS.
    Returns the given callback for easier development.
    """
    append, remove = _listener.add_handler, _listener.remove_handler

    append(callback)
