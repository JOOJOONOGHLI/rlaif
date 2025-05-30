Sprint Checklist: Address TA Feedback on Granular RLAIF



Dhruv:

- Pipeline finished for DPO, need to evaluate the results


Main Issues from Feedback
The example in the document is hard to understand; all three responses look too similar.

The qualitative analysis does not clearly explain why the rejected responses were considered vague.

Sprint Goals
Revise Example Set

Rewrite or select clearer example triplets (chosen / rejected / original).

Ensure differences are obvious, even to a reader unfamiliar with the project.

Include:

One case where the rejected response is off-topic.

One case where the rejected response is vague or incomplete.

One case where the rejected response is factually wrong.

Action: Assign a team member to curate and format these examples.

Strengthen Qualitative Analysis

For each example, write detailed reasoning:

Why the rejected response is worse.

Why the chosen response is better.

How this difference aligns with the reward signal or preference objective.

Action: Assign a team member to draft these points for inclusion in the write-up or as inline code comments.

Code Adjustments

Improve data filtering to prevent vague or near-identical responses from entering training pairs.

Add logging or print statements to surface example differences during training for inspection.

Develop a small script to visualize or sample random chosen/rejected pairs for quick review.

Action: Assign a team member to implement these code improvements.

Update Documentation

Update the README or supporting documentation to:

Clearly explain how examples are generated and why they are valid.

Summarize the strengthened qualitative analysis.

Provide a reference or link to the updated analysis document.

Action: Assign a team member to handle documentation updates.

Prepare for Discussion with TA

Before the next check-in, create a brief summary (slide or bullet points) outlining:

What changes were made.

Why these changes address the TA’s feedback.

What evidence we now have showing the examples and analysis are clearer.

Action: Assign a team member to prepare this summary.

