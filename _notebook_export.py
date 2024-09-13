# @title This script is used to export the notebook to Markdown
import subprocess
import nbconvert
import sys
import jupyter

def exportNotebook(strNotebookFileInput, strExportFileOutput):
    cmd="jupyter nbconvert "+strNotebookFileInput+" --to markdown --output "+strExportFileOutput
    try:
      subprocess.run([sys.executable,cmd]) # no error but no results
      # subprocess.run([cmd]) # failed
      # subprocess.run(["jupyter", "nbconvert", strNotebookFileInput, "--to", "markdown", "--output", strExportFileOutput]) # no error but no results
    except:
      print("failed")
    print(cmd)
    # subprocess.check_call(["jupyter", "nbconvert", strNotebookFileInput, "--to", "markdown", "--output", strExportFileOutput]) # only works locally
