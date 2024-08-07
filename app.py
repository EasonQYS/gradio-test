import gradio as gr
import os
import shutil
print(os.system('ls -la'))
print('***********')
print(os.system('ls -la '))

with gr.Blocks() as demo:
    file_path = gr.FileExplorer(root_dir='./')

demo.launch()


'''
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
'''
