#!../venv/bin/python
"""   File: permissions.py
Reading and Modifying umask Values
Learn usage of the following library function:
    os.umask()  (and it quirk!)
"""
import os

def umask(desired_umask=None):
    """
    Returns the user mask.
    If no parameter is specified or if it is out of range,
    the user mask is restored.
    Else it is set to desired_umask.
    """
    no_permissions = 0b111111  # Maximum security!
    if ((desired_umask is None)
    or (not(0<=desired_umask<=no_permissions))):
        mask = os.umask(no_permissions)
        assert no_permissions == os.umask(mask)
        return mask
    else:
        return os.umask(desired_umask)

if __name__ == "__main__":
    inverting_mask = 0b111111111
    mask = umask()
    print("User mask is {:09b}; using inverting mask of {:09b}"
                .format(mask, inverting_mask))
    print("we get the following privileges: {0:9b} or {0:3o}."
                .format(mask ^ inverting_mask))
    assert umask() == umask()

