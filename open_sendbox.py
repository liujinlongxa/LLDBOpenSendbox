import lldb
import os


def open_sendbox(debugger, command, result, internal_dict):
    frame = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread(
    ).GetSelectedFrame()
    options = lldb.SBExpressionOptions()
    options.SetTrapExceptions(False)
    value = frame.EvaluateExpression('NSHomeDirectory()', options)
    error = value.GetError()

    if error.Fail():
        print(error)
        return

    path_str = str(value)
    sendbox_dir = path_str.split('@')[1]
    print("sendbox path:" + sendbox_dir)
    os.system('open ' + sendbox_dir)
