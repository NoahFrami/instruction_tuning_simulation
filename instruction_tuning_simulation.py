"""
From Prompting to Instruction Tuning
Name: Noah C Frami
Date: 10/21/2026
"""

from dataclasses import dataclass
from typing import List


@dataclass
class ExperimentResult:
    task_name: str
    prompt_type: str
    prompt_text: str
    model_output: str
    followed_instructions: bool
    notes: str


# -----------------------------
# PRINTING FUNCTIONS
# -----------------------------
def print_result(result: ExperimentResult) -> None:
    print("=" * 70)
    print(f"Task: {result.task_name}")
    print(f"Prompt Type: {result.prompt_type}")

    print("\nPrompt:")
    print(result.prompt_text)

    print("\nModel Output:")
    print(result.model_output)

    print(f"\nFollowed Instructions: {result.followed_instructions}")
    print(f"Notes: {result.notes}")
    print("=" * 70)
    print()


def compare_results(prompt_only: ExperimentResult, instruction_tuned: ExperimentResult) -> None:
    print("#" * 70)
    print(f"COMPARISON FOR TASK: {prompt_only.task_name}")
    print("#" * 70)

    print("\nPrompt-Only Output:")
    print(prompt_only.model_output)

    print("\nInstruction-Tuned Output:")
    print(instruction_tuned.model_output)

    print("\nAnalysis:")

    # Write your comparison analysis here
    if instruction_tuned.followed_instructions and not prompt_only.followed_instructions:
        print("- The Instruction tuned version improved task following behavior.")
    elif instruction_tuned.followed_instructions == prompt_only.followed_instructions:
        print("- The behavior stayed roughly the same.")
    else:
        print("- The instruction tuned model did not clearly improve the behavior.")

    print(f"- Prompt only notes: {prompt_only.notes}")
    print(f"- Instruction Tuned notes: {instruction_tuned.notes}")

    print()


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main() -> None:
    results: List[ExperimentResult] = []

    # ===================================================
    # TASK 1 (REQUIRED)
    # ===================================================

    # Task 1: Translation
    prompt_only_1 = ExperimentResult(
        task_name="Translation",
        prompt_type="Prompt-Only",
        prompt_text="Translate into Spanish: Hello",
        model_output="Hello there! How are you today?",
        followed_instructions=False,
        notes="The response continued the phrase rather than translating it."
    )

    instruction_1 = ExperimentResult(
        task_name="Translation",
        prompt_type="Instruction-Tuned",
        prompt_text=(
            "Instruction: Translate to Spanish\n"
            "Input: Good Morning\n"
            "Output: Buenos Diasa\n\n"
            "Instruction:Translate to Spanish\n"
            "Input: Thank You\n"
            "Output: Gracias\n\n"
            "Instruction: Translate to Spanish\n"
            "Input: Hello\n"
            "Output:"
        ),
        model_output="Hola",
        followed_instructions=True,
        notes="The demonstrations helped the model produce the requested format"
    )

    results.append(prompt_only_1)
    results.append(instruction_1)

    # ===================================================
    # TASK 2 Simple Explanation
    # ===================================================

    prompt_only_2 = ExperimentResult(
        task_name="Explain gravity to a Child",
        prompt_type="Prompt-Only",
        prompt_text="Explain gravity to a 6-year-old.",
        model_output="Gravity is a fundamental force of attraction between objects with mass,"
                     "described by classical and relativistic physics",
        followed_instructions=False,
        notes="The answer is relevant, but is not appropriate for a 6 year old."
    )

    instruction_2 = ExperimentResult(
        task_name="Explain gravity to a Child",
        prompt_type="Instruction-Tuned",
        prompt_text=(
            "Instruction: Explain a science idea to a young child using simple words.\n"
            "Input: Photosynthesis\n"
            "Output: Plants use sunlight ot make their own food.\n\n"
            "Instruction: Explain a science idea to a young child using simple words.\n"
            "Input: Evaporation\n"
            "Output: Water can turn into an invisable gas and go up into the air.\n\n"
            "Instruction: Explain a science idea to a young child using simple words.\n"
            "Input: Gravity\n"
            "Output: "

        ),
        model_output="Gravity is what makes things fall down instead of floating away.",
        followed_instructions=True,
        notes="The examples guide the tone, length and difficulty level."
    )

    results.append(prompt_only_2)
    results.append(instruction_2)

    # ===================================================
    # TASK 3 Summarization
    # ===================================================

    paragraph = (
        "The school science fair will take place next Friday in the Gymnasium."
        "Students from grades 6 through 8 will present projects on biology, chemistry,"
        "physics, and engineering. Families are invited to attend in the evening."
    )

    prompt_only_3 = ExperimentResult(
        task_name="Summarization",
        prompt_type="Prompt-Only",
        prompt_text=f"Summarize the following paragraph: {paragraph}.",
        model_output=(
            "the school science fair will take place next Friday in the gymnasium and,"
            "students will present projects."
        ),
        followed_instructions=True,
        notes="This one worked decently without demonstrations")




    instruction_3 = ExperimentResult(
        task_name="Summarization",
        prompt_type="Instruction-Tuned",
        prompt_text=(
            "Instruction: Summarize the paragraph in one short sentence. \n"
            "Input: The town library is holding a sale this weekend with fiction, history and children books.\n"
            "Output: The library is holding a weekend book sale.\n\n"
            "Instruction: Summarize the paragraph in one short sentence. \n"
            "Input: The art club will meet tuesday after school to prepare paintings for the Spring Showcase.\n"
            "Output: The art club will meet tuesday to prepare for the showcase.\n\n"
            "Instruction: Summarize the paragraph in one short sentence. \n"
            f"Input: {paragraph}\n"
            "Output: "
        ),
        model_output="The school will host a science fair next friday with student projects and family attendance.",
        followed_instructions=True,
        notes="The demonstrations made the summary more concise"
    )

    results.append(prompt_only_3)
    results.append(instruction_3)

    # ===================================================
    # REQUIRED FAILURE CASE
    # ===================================================

    failure_case = ExperimentResult(
        task_name="Failure Case: Complex Reasoning",
        prompt_type="Instruction-Tuned",
        prompt_text=(
            "Instruction: Solve the problem step by step and give the final answer.\n"
            "Input: If a train leaves at 2:15 PM and arrives at 5:45 PM, how long was the trip.\n"
            "Output: The trip lasted 3 hours and 30 minutes.\n\n"
            "Instruction: Solve the problem step by step and give the final answer.\n"
            "Input: A store had 50 apples, sold 18, and then received 12 more. How many apples are there.\n"
            "Output: 50 - 18 = 32. Then 32 + 12 = 44. Final Answer: 44.\n\n"
            "Instruction: Solve the problem step by step and give the final answer.\n"
            "Input: John has 3 boxes with 8 markers in each box and buys 5 more markers. How many markers does John have?\n"
            "Output:"
        ),
        model_output="3 + 8 * 5 = 16. Final Answer: 16.",
        followed_instructions=False,
        notes=(
            "The model fallowed the format but failed the reasoning.\n"
            "- It added instead of multiplying 3 * 8 first.\n"
        )
    )

    results.append(failure_case)

    # ===================================================
    # PRINT RESULTS
    # ===================================================
    print("\nALL RESULTS\n")

    for result in results:
        print_result(result)

    # ===================================================
    # COMPARISONS
    # ===================================================
    compare_results(prompt_only_1, instruction_1)
    compare_results(prompt_only_2, instruction_2)
    compare_results(prompt_only_3, instruction_3)


if __name__ == "__main__":
    main()