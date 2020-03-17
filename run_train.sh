python run_classifier_with_tfhub.py --data_dir data \
  --task_name cola \
  --bert_hub_module_handle ~/Develop/models/google/bert_chinese_L-12_H-768_A-12/1 \
  --output_dir output \
  --do_train true \
  --use_tpu false
