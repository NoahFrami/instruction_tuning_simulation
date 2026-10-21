# From Prompting to Instruction Tuning

**Name:** Noah C Frami  
**Date:** 10/21/2026

## Project Description
This project compares prompt-only responses with instruction-tuned style examples to see how examples can improve a language model's ability to follow instructions.

The program uses sample model outputs to compare performance on different tasks.

## Project Goals
- Compare prompt-only and instruction-tuned style prompts.
- Test how examples affect model responses.
- Check if the model follows instructions.
- Identify situations where the model still makes mistakes.

## Tasks
The program includes the following experiments:

1. **Translation:** Translate English words into Spanish.
2. **Simple Explanation:** Explain gravity in simple words for a child.
3. **Summarization:** Summarize a school science fair announcement.
4. **Failure Case:** Test complex reasoning with a math word problem.

## How It Works
The program uses a Python dataclass called `ExperimentResult` to store:
- Task name
- Prompt type
- Prompt text
- Model output
- Whether instructions were followed
- Notes about the results

It prints each experiment and compares prompt-only results with instruction-tuned style results.

## Requirements
- Python 3.10 or newer
- No external libraries required

## How to Run
1. Download or clone this repository.
2. Open the project in PyCharm or another Python editor.
3. Run `main` in `from_prompting_to_instruction_tuning.py` (or the filename used in your repository).
4. Review the printed results and comparisons.

## Results
The experiments demonstrate that examples can help guide a model's responses, including the format, tone, and length.

However, examples do not guarantee correct reasoning. The failure case shows that a model can follow a response format but still get a math problem wrong.

## Limitations
This project uses predefined sample outputs rather than calling a live AI model. The instruction-tuned examples demonstrate an in-context prompting approach and do not actually train or fine-tune a model.

## Conclusion
This project shows how providing examples can improve task consistency, but models still need to be checked for accuracy, especially when solving reasoning problems.
