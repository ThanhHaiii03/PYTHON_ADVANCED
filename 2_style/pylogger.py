# STYLE ***************************************************************************
# content = assignment
#
# date    = 2025-03-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

# original: logging.init.py

def findCaller(self) -> tuple:
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    frame = currentframe()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.

    DEFAULT_CALLER_INFO = ("(unknown file)", 0, "(unknown function)")

    if frame is not None:
        frame = frame.frame_back
    caller_infor = DEFAULT_CALLER_INFO
    while hasattr(frame, "frame_code"):
        code_object = frame.frame_code
        file_name = os.path.normcase(code_object.code_filename)

    #If this frame is the logger file itself → ignore
        if file_name == _srcfile:
            frame = frame.frame_back
            continue
        caller_infor = (code_object.code_filename, frame.frame_lineno, code_object.code_name)
        break
    return caller_infor

# How can we make this code better?


