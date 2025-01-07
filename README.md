# Evaluating LLMs on Finno-Ugric Languages

Task configurations and datasets for [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) as described in the paper *How Well do LLMs know Finno-Ugric Languages? A Systematic Assessment* (NoDaLiDa/Baltic-HLT 2025).

## Setup

Download and install [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (the task configurations are verified to work with the version `0.4.7`).

🚨 For most of the tasks, the datasets are automatically downloaded from HuggingFace. However, we use a modification of [belebele-smugri](https://huggingface.co/datasets/tartuNLP/belebele-smugri) which separates a small development set from the given test set. This is needed for in-context demonstrations. We also use a modification of [TyDiQA](https://huggingface.co/datasets/google-research-datasets/tydiqa) that includes a small subset of Finnish questions from the `secondary_task` subset of TyDiQA.

Therefore the paths to these datasets must be given manually in respective task configurations. Specifically, the value of `dataset_path` in the yaml files of `tasks/belebele-smugri` must be changed to the full path of `data/belebele-smugri` and in `tasks/tydiqa-fi` to the full path of `data/tydiqa-fi`. You can either do it manually or run the script:

`./update_paths.sh`

After that, copy the tasks located in `tasks` to `lm-evaluation-harness/lm_eval/tasks/`:

`cp -r tasks/* lm-evaluation-harness/lm_eval/tasks/`

## Evaluate

TBA

