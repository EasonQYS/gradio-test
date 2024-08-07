import gradio as gr
import os
import shutil

def process_file(fileobj):
    print(fileobj)
    path = "./" + os.path.basename(fileobj)  #NB*
    shutil.copyfile(fileobj.name, path)
    return path

demo = gr.Interface(
    fn=process_file,
    inputs=[
        "file",
    ],
    outputs="text"
)
demo.launch(server_name='0.0.0.0')
