# --------------------------------------------------
# Lesson 18 Build 2: Fine-Tuning Dataset Readiness Checker
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Assess whether a dataset is ready for fine-tuning based on
# quantity, quality, formatting, relevance, evaluation readiness,
# risk controls, and deployment clarity.
# --------------------------------------------------


def score_yes_no(value, yes_points=2, no_points=0):
    if value.lower().strip() in ["yes", "y", "high", "ready"]:
        return yes_points
    return no_points


def score_quality(value):
    value = value.lower().strip()

    if value in ["very high", "excellent"]:
        return 4

    if value in ["high", "good"]:
        return 3

    if value in ["medium", "acceptable"]:
        return 2

    if value in ["low", "poor", "weak"]:
        return 0

    return 1


def score_examples(number_of_examples):
    try:
        examples = int(number_of_examples)
    except ValueError:
        examples = 0

    if examples >= 1000:
        return 5

    if examples >= 500:
        return 4

    if examples >= 100:
        return 3

    if examples >= 50:
        return 2

    if examples >= 20:
        return 1

    return 0


def generate_dataset_readiness_report(
    dataset_name,
    use_case,
    number_of_examples,
    input_output_quality,
    format_consistency,
    domain_relevance,
    duplicate_checked,
    bias_checked,
    sensitive_data_checked,
    human_review_done,
    validation_set_available,
    evaluation_set_available,
    baseline_available,
    expected_behavior_clear,
    deployment_purpose_clear,
    cost_estimated
):
    """
    Generate dataset readiness report for fine-tuning.
    """

    score = 0

    score += score_examples(number_of_examples)
    score += score_quality(input_output_quality)
    score += score_quality(format_consistency)
    score += score_quality(domain_relevance)
    score += score_yes_no(duplicate_checked, yes_points=2)
    score += score_yes_no(bias_checked, yes_points=2)
    score += score_yes_no(sensitive_data_checked, yes_points=2)
    score += score_yes_no(human_review_done, yes_points=3)
    score += score_yes_no(validation_set_available, yes_points=3)
    score += score_yes_no(evaluation_set_available, yes_points=3)
    score += score_yes_no(baseline_available, yes_points=2)
    score += score_yes_no(expected_behavior_clear, yes_points=3)
    score += score_yes_no(deployment_purpose_clear, yes_points=2)
    score += score_yes_no(cost_estimated, yes_points=2)

    max_score = 40
    percentage = round((score / max_score) * 100, 1)

    if percentage < 40:
        readiness_level = "Not ready"
        recommendation = (
            "Do not fine-tune yet. Improve dataset size, quality, formatting, "
            "review, evaluation, and baseline comparison first."
        )

    elif percentage < 65:
        readiness_level = "Partially ready"
        recommendation = (
            "The dataset may support experimentation, but it is not ready for serious fine-tuning. "
            "Run a small pilot only after improving weak areas."
        )

    elif percentage < 80:
        readiness_level = "Ready for pilot fine-tuning"
        recommendation = (
            "The dataset is strong enough for a controlled pilot fine-tuning experiment. "
            "Do not deploy until the fine-tuned model beats the baseline."
        )

    else:
        readiness_level = "Ready for controlled fine-tuning"
        recommendation = (
            "The dataset appears ready for controlled fine-tuning, provided cost, privacy, "
            "evaluation, and deployment controls are in place."
        )

    report = f"""
# Fine-Tuning Dataset Readiness Report

## 1. Dataset Name

{dataset_name}

## 2. Use Case

{use_case}

---

# 3. Dataset Readiness Inputs

Number of examples:
{number_of_examples}

Input-output quality:
{input_output_quality}

Format consistency:
{format_consistency}

Domain relevance:
{domain_relevance}

Duplicate examples checked:
{duplicate_checked}

Bias checked:
{bias_checked}

Sensitive data checked:
{sensitive_data_checked}

Human review completed:
{human_review_done}

Validation set available:
{validation_set_available}

Evaluation set available:
{evaluation_set_available}

Baseline available:
{baseline_available}

Expected behavior clear:
{expected_behavior_clear}

Deployment purpose clear:
{deployment_purpose_clear}

Cost estimated:
{cost_estimated}

---

# 4. Readiness Score

Score:
{score} / {max_score}

Percentage:
{percentage}%

Readiness level:
{readiness_level}

---

# 5. Recommendation

{recommendation}

---

# 6. Interpretation

Fine-tuning data must be more than a pile of examples.

A usable fine-tuning dataset should have:
- Enough examples for the task.
- Clean input-output pairs.
- Consistent formatting.
- Strong domain relevance.
- Human-reviewed examples.
- Duplicates removed.
- Sensitive data removed or controlled.
- Bias and representation risks checked.
- A validation set.
- An evaluation set.
- A baseline model result for comparison.

If these are missing, fine-tuning may simply train the model to repeat poor structure, weak reasoning, or biased examples.

---

# 7. ResearchLab Guidance

For the ResearchLab RAG Assistant, fine-tuning data should not be collected randomly.

Possible useful fine-tuning examples later:
- Research question generation examples.
- Literature synthesis examples.
- Evidence limitation statements.
- Postharvest terminology extraction examples.
- Structured academic answer examples.
- Reviewer-style critique examples.
- Grant concept refinement examples.

But for now, improve:
- RAG corpus quality.
- Metadata structure.
- Evaluation logs.
- Source attribution.
- Human-reviewed answer examples.

Your future fine-tuning dataset should come from repeated, reviewed, high-quality outputs, not raw experiments.
"""
    return report.strip()


print("\nFine-Tuning Dataset Readiness Checker")
print("Lesson 18: Build 2")
print("Type 'exit' anytime to stop.\n")

while True:
    dataset_name = input("Enter dataset name: ")

    if dataset_name.lower().strip() in ["exit", "quit", "stop"]:
        print("Fine-tuning dataset readiness checker ended.")
        break

    use_case = input("Enter fine-tuning use case: ")
    number_of_examples = input("Number of examples available: ")
    input_output_quality = input("Input-output quality, low / medium / high / very high: ")
    format_consistency = input("Format consistency, low / medium / high / very high: ")
    domain_relevance = input("Domain relevance, low / medium / high / very high: ")
    duplicate_checked = input("Have duplicates been checked? yes / no: ")
    bias_checked = input("Has bias or representation risk been checked? yes / no: ")
    sensitive_data_checked = input("Has sensitive/private data been checked? yes / no: ")
    human_review_done = input("Has human expert review been done? yes / no: ")
    validation_set_available = input("Is a validation set available? yes / no: ")
    evaluation_set_available = input("Is an evaluation set available? yes / no: ")
    baseline_available = input("Do you have baseline model results? yes / no: ")
    expected_behavior_clear = input("Is the expected model behavior clear? yes / no: ")
    deployment_purpose_clear = input("Is the deployment purpose clear? yes / no: ")
    cost_estimated = input("Has fine-tuning cost been estimated? yes / no: ")

    report = generate_dataset_readiness_report(
        dataset_name=dataset_name,
        use_case=use_case,
        number_of_examples=number_of_examples,
        input_output_quality=input_output_quality,
        format_consistency=format_consistency,
        domain_relevance=domain_relevance,
        duplicate_checked=duplicate_checked,
        bias_checked=bias_checked,
        sensitive_data_checked=sensitive_data_checked,
        human_review_done=human_review_done,
        validation_set_available=validation_set_available,
        evaluation_set_available=evaluation_set_available,
        baseline_available=baseline_available,
        expected_behavior_clear=expected_behavior_clear,
        deployment_purpose_clear=deployment_purpose_clear,
        cost_estimated=cost_estimated
    )

    print("\nGenerated Dataset Readiness Report:\n")
    print(report)
    print("\n" + "=" * 100 + "\n")