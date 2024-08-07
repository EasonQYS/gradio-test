import gradio as gr
import os
import shutil
print(os.system('ls -la'))
print('***********')
print(os.system('pwd'))

def do2(fileobj):
    print(fileobj.name)
    path = "./" + os.path.basename(fileobj.name)  #NB*
    shutil.copyfile(fileobj.name, path)
    return path

with gr.Blocks() as demo:
    file_path = gr.FileExplorer(root_dir='./')
    with gr.Row():
        f1 = gr.File()
        b2 = gr.Button("语音转文本")
        f2 = gr.File()
    b2.click(do2, inputs=f1,outputs=f2)

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
