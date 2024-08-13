# gradio-test
这个测试仓库用于测试SNH48口袋48模型微调后的InternLM2.5-7B-chat模型。需要torch==2.1.2以避免RuntimeError: "triu_tril_cuda_template" not implemented for 'BFloat16'(https://github.com/meta-llama/llama3/issues/110)


WARNING: 'git lfs clone' is deprecated and will not be updated
          with new flags from 'git clone'
'git clone' has been updated in upstream Git to have comparable
speeds to 'git lfs clone'.

OSError: You seem to have cloned a repository without having git-lfs installed. Please install git-lfs and run `git lfs install` followed by `git lfs pull` in the folder you cloned.

python=3.10 gradio=3.50.2 streamlit=1.32.0 torch=2.1.2

Nvidia A1024GB  8vCPU32GB
