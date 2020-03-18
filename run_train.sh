pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
python run_classifier_with_tfhub.py --data_dir data \
  --task_name cola \
  --bert_hub_module_handle data/pretrained \
  --output_dir output \
  --do_train true --use_fp32
