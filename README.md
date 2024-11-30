# Generate a Dataset for Preference Optimization of Meditron

## Pipeline

### 1st step: Generate prompts using GPT-4o

Using GPT-4o and synthetic few-shot examples similar to the ones on the MOOVE platform, generate prompts that health care workes could be asking to Meditron. It is important to have enough diversity in the questions, such that there is no over-fitting.

### 2nd step: Generate several responses using Meditron-3

Using Meditron-3 generate 3 - 6 answers per prompt generated in step 1. To be able to do preference optimization in step 3 it is important that the temperature while generating the different answers is high, such that there is enough difference in the generated answers. To run Meditron, use 4 - 5 A100 GPUs on the EPFL RCP cluster.

### 3rd step: Assign each answer a score using nvidia/Llama-3.1-Nemotron-70B-Reward model

Using nvidia/Llama-3.1-Nemotron-70B-Reward model, each of the 3 - 6 answers gets a score. This score will later be used to perform direct preference optimization (DPO) on Meditron-3.

### Further steps

nvidia/Llama-3.1-Nemotron-70B-Reward model used is not fine-tuned for the medical domain. An interesting and promising step would be to first fine tune the reward model for the medical domain before using it to assign scores.