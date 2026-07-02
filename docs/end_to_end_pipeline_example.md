# End-to-End Pipeline Example

This example demonstrates the public-facing logic of the PromptCraft pipeline
without disclosing the private provider orchestration backend.

## 1. Raw input excerpt
See [`../samples/contract_input_excerpt.sol`](../samples/contract_input_excerpt.sol) for a short excerpt from a public benchmark contract.

## 2. Prompt excerpt
See [`prompt_excerpt_zero_shot.md`](prompt_excerpt_zero_shot.md) for a sanitized zero-shot prompt excerpt.

## 3. Representative raw model-output excerpt
See [`../samples/raw_model_output_excerpt.txt`](../samples/raw_model_output_excerpt.txt).
This file is a **sanitized representative excerpt** rather than a full provider
response log. It is included to show the kind of semi-structured text that the
private cleaning pipeline must normalize.

## 4. Cleaned / final structured artifact
See [`../samples/cleaned_structured_output_sample.csv`](../samples/cleaned_structured_output_sample.csv).
This file shows the final structured representation used by downstream public
summaries and human evaluation.

## Why this example is partial
The public artifact exposes enough evidence to understand the paper's data flow
and verify summary tables, but it does not expose the complete provider-specific
backend, full prompt library, or production response logs.
