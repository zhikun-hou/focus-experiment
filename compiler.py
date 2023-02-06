
import sys


def handleDlg(instruction,line_id):
    if(not instruction.startswith("dlg = gui.DlgFromDict")):
        return []
    # 把这行和后面两行注释掉
    return [line_id,line_id+1,line_id+2]

def handleLog(instruction,line_id):
    if(not instruction.startswith("log")):
        return []
    # 隐藏本行即可
    return [line_id]

def handleExp(instruction,line_id):
    if(instruction.startswith("thisExp.")):
        return [line_id]

    if(instruction.startswith("thisExp = data.ExperimentHandler")):
        return [line_id,line_id+1,line_id+2,line_id+3,line_id+4]
    
    return []


if __name__ == "__main__":

    lines = []
    lines_to_hide = []

    with open(sys.argv[1],"r",encoding="utf-8") as script:

        lines = script.readlines()

        for idx in range(len(lines)):
            instruction = lines[idx].lstrip(' ')
            hide1 = handleDlg(instruction,idx)
            hide2 = handleLog(instruction,idx)
            hide3 = handleExp(instruction,idx)
            to_hide = [*hide1,*hide2,*hide3]
            lines_to_hide.extend(to_hide)

    for idx in lines_to_hide:
        lines[idx] = "# "+lines[idx]
    
    for idx in range(len(lines)):
        instruction = lines[idx].lstrip(' ')
        if(instruction.startswith("# --- Import packages ---")):
            if(not lines[idx+1].lstrip(' ').startswith("from loader import *")):
                lines.insert(idx+1,"from loader import *\n")

    with open(sys.argv[1], "w",encoding="utf-8") as file:
        script = "".join(lines)
        file.write(script)
        file.close()
        
        