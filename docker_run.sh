docker run --gpus all -it --rm \
 -v `pwd`:/workspace \
 -v /home/jie/Develop/models/google/bert_chinese_L-12_H-768_A-12/1:/workspace/data/pretrained \
 tensorflow/tensorflow:1.14.0-gpu-py3 bash
