# Evaluating LLMs on Finno-Ugric Languages

Task configurations and datasets for [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) as described in the paper *How Well do LLMs know Finno-Ugric Languages? A Systematic Assessment* (NoDaLiDa/Baltic-HLT 2025).

## Benchmarks

This repository contains task configurations for following benchmarks:

- [belebele-smugri](https://huggingface.co/datasets/tartuNLP/belebele-smugri)
- [sib-smugri](https://huggingface.co/datasets/tartuNLP/sib-smugri)
- [xcopa-et]() (i.e. for Estonian subset of XCOPA)
- [flores-smugri](https://huggingface.co/datasets/tartuNLP/flores-smugri-pairs)
- [tydiqa-fi](https://huggingface.co/datasets/google-research-datasets/tydiqa) (i.e for Finnish subset of TyDiQA)
- [estqa](https://huggingface.co/datasets/TalTechNLP/EstQA) 

## Setup

Download and install [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (the task configurations are verified to work with the version `0.4.7`).

🚨 For most of the tasks, the datasets are automatically downloaded from HuggingFace. However, we use a modification of [belebele-smugri](https://huggingface.co/datasets/tartuNLP/belebele-smugri) which separates a small development set from the given test set. This is needed for in-context demonstrations. We also use a modification of [TyDiQA](https://huggingface.co/datasets/google-research-datasets/tydiqa) which separates Finnish questions from the `secondary_task` subset of TyDiQA. Note that in our experiments we only use a small subset of Finnish questions from TyDiQA to make it roughly equivalent to the size of EstQA.

Therefore the paths to these datasets must be given manually in respective task configurations. Specifically, the value of `dataset_path` in the yaml files of `tasks/belebele-smugri` must be changed to the full path of `data/belebele-smugri` and in `tasks/tydiqa-fi` to the full path of `data/tydiqa-fi`. You can either do it manually or run the script:

`./set_paths.sh`

After that, copy the tasks located in `tasks` to `lm-evaluation-harness/lm_eval/tasks/`:

`cp -r tasks/* lm-evaluation-harness/lm_eval/tasks/`

## Tasks

We define multiple task configurations for each benchmark. The configurations differ by the evaluation method which is either 1) log likelihood (for multiple choice benchmarks); 2) answer generation and its comparison with the correct answer (open-ended benchmarks such as QA); 3) answer generation (and comparison with the correct answer) preceeded by intermediate reasoning steps (chain-of-thought (CoT)).

Each evaluation method is meant to be used in zero-shot or few-shot (1, 3 or 5) setting.

🚨 Note that CoT evaluation with few-shot requires hand-crafted examples with intermediate reasoning steps which therefore can not be directly sampled from the fewshot split. Instead, we define separate task configuration for each CoT + few-shot combination where the function for `doc_to_text` field provides the correct number of examples. Therefore **all tasks that use CoT should be run with `--num_fewshot 0`**. File `evaluate_all_tasks.sh` lists all such tasks (`NO_SHOT_TASKS`).

## Evaluation

Please take a look at the example script `evaluate_all_tasks.sh` for the complete list of tasks and other evaluation details.
