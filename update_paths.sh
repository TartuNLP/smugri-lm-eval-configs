#!/bin/bash

TASKS_DIR="tasks"
DATA_DIR="data"

for SUBFOLDER in "$DATA_DIR"/*; do
    echo "Processing subfolder: $SUBFOLDER"
    # If subfolder is belebele-smugri
    if [[ "$SUBFOLDER" == *belebele-smugri* ]]; then
        YAML_FILE1="$TASKS_DIR/belebele-smugri/cot/_cot_smugri_yaml"
        YAML_FILE2="$TASKS_DIR/belebele-smugri/cot_zero/_cot_zero_smugri_yaml"
        YAML_FILE3="$TASKS_DIR/belebele-smugri/fewshot/_fewshot_smugri_yaml"
        YAML_FILE4="$TASKS_DIR/belebele-smugri/fewshot_gen/_fewshot_smugri_gen_yaml"
        FULL_PATH=$(realpath "$SUBFOLDER")
        sed -i "s|^dataset_path:.*|dataset_path: $FULL_PATH|" "$YAML_FILE1"
        sed -i "s|^dataset_path:.*|dataset_path: $FULL_PATH|" "$YAML_FILE2"
        sed -i "s|^dataset_path:.*|dataset_path: $FULL_PATH|" "$YAML_FILE3"
        sed -i "s|^dataset_path:.*|dataset_path: $FULL_PATH|" "$YAML_FILE4"
    fi
    if [[ "$SUBFOLDER" == *tydiqa-fi* ]]; then
        FULL_PATH=$(realpath "$SUBFOLDER")
        YAML_FILE1="$TASKS_DIR/tydiqa-fi/fewshot_cot_fi.yaml"
        YAML_FILE2="$TASKS_DIR/tydiqa-fi/fewshot_gen_fi.yaml"
        sed -i "s|^dataset_path:.*|dataset_path: $FULL_PATH|" "$YAML_FILE1"
        sed -i "s|^dataset_path:.*|dataset_path: $FULL_PATH|" "$YAML_FILE2"
    fi
done

