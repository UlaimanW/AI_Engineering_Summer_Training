# Prompting Fundamentals — Comparing 5 Prompts for the Same Task

## Chosen Task

Write an email to a doctor asking for a **2-day extension** for an assignment because of a **family emergency**.

---

## Prompt 1 — Basic Prompt

### Input Prompt

```text
Write an email to a doctor asking for more time to submit an assignment.
```

### Output

```text
I think there may be a mistake. You asked me to write an email to a doctor, but the context suggests that the email is about submitting an assignment, which is more relevant to an academic setting, such as a professor or instructor. 

If that's the case, here's an email that you can use as a template:

Subject: Request for Extension on Assignment Submission

Dear [Professor's Name],

I hope this email finds you well. I am writing to request an extension on the submission of the [Assignment Name] that is due on [Original Due Date]. Due to [briefly mention a valid reason, e.g., unexpected personal circumstances, technical issues, or heavy coursework], I have fallen behind schedule and need some extra time to complete the assignment to the best of my abilities.

I am confident that with a short extension, I will be able to submit a piece of work that meets your expectations. I am estimating that I will need an additional [Specific Number of Days] to complete the assignment. I am aiming to submit it by [New Due Date].

I would greatly appreciate it if you could consider my request. Please let me know if this is feasible and if there's anything else I can provide to support my request.

Thank you for your understanding and I look forward to your response.

Sincerely,
[Your Name]

If you indeed need to write an email to a doctor, please provide more context or information about the assignment or the reason for the email, and I'll be happy to help.
```

---

## Prompt 2 — Improved Prompt

### Input Prompt

```text
Write an email to a doctor asking for a 2-day extension to submit an assignment because of a family emergency.
```

### Output

```text
Here's a sample email:

Subject: Request for Assignment Extension due to Family Emergency

Dear [Doctor's Name],

I hope this email finds you well. I am writing to request a 2-day extension on the upcoming assignment that is due on [Original Due Date]. Unfortunately, I have recently experienced a family emergency that requires my immediate attention and presence.

Due to the unexpected nature of this situation, I have fallen behind schedule and need some additional time to complete the assignment to the best of my abilities. I am confident that with a short extension, I will be able to submit quality work that meets your expectations.

I am respectfully requesting an extension of 2 days, which would make the new due date [New Due Date]. I apologize for any inconvenience this may cause and appreciate your understanding during this difficult time.

Please let me know if this is feasible, and if there's any further documentation or information you need from me to support my request. I am committed to my studies and am eager to get back on track as soon as possible.

Thank you for your consideration and support.

Sincerely,
[Your Name]
```

---

## Prompt 3 — Detailed Prompt

### Input Prompt

```text
You are a university student. Write a formal and respectful email to your doctor asking for a 2-day extension on an assignment. Explain that you had a family emergency and could not finish the work on time. Apologize for the inconvenience and ask politely for understanding.
```

### Output

```text
Subject: Request for Assignment Extension due to Family Emergency

Dear [Doctor's Name],

I hope this email finds you well. I am writing to request a two-day extension on the current assignment that is due on [Original Due Date]. Due to a recent family emergency that required my immediate attention, I was unable to complete the assignment on time.

Unfortunately, the unexpected situation arose on [Date] and I had to dedicate my time to addressing the family matter. Despite my best efforts to manage my time effectively, I was unable to complete the assignment to the best of my abilities within the given deadline. I am confident that with a short extension, I will be able to complete the assignment to the high standards that you expect from us.

I apologize for any inconvenience this may cause and appreciate your understanding in this matter. I am committed to my studies and am eager to complete the assignment as soon as possible. I am estimating that I will need an additional two days to complete the work, and I am hoping to submit the assignment on [New Due Date].

I would like to express my gratitude for considering my request. Please let me know if this is feasible and if there are any additional steps I need to take. I am available to discuss this further if needed and appreciate your support during this challenging time.

Thank you for your time and understanding.

Sincerely,

[Your Name]
```

---

## Prompt 4 — Creative Prompt

### Input Prompt

```text
You are a university student writing to a doctor you respect. Write a sincere and professional email asking for a 2-day extension for an assignment after a family emergency affected your ability to complete it on time. Make the email sound genuine, respectful, and appreciative rather than robotic.
```

### Output

```text
Subject: Request for Assignment Extension due to Unforeseen Family Emergency

Dear Dr. [Doctor's Name],

I hope this email finds you well. I am writing to request a 2-day extension on the upcoming assignment that is due on [Original Due Date]. I understand the importance of meeting deadlines, and I apologize for any inconvenience this may cause. Unfortunately, I have recently faced a family emergency that has significantly impacted my ability to complete the assignment on time.

Over the past few days, my family has been dealing with a sudden and unexpected situation that has required my immediate attention and support. As a result, I have fallen behind schedule, and despite my best efforts to catch up, I require a brief extension to ensure that I can submit work that meets your expectations and the standards of the course.

I want to express my gratitude for your understanding and flexibility in this matter. Your lectures and guidance have been invaluable to me, and I am deeply appreciative of the effort you invest in teaching and mentoring us. I am confident that, with a short extension, I will be able to complete the assignment to the best of my abilities and submit quality work.

The additional two days will enable me to complete the outstanding tasks and ensure that my submission meets the requirements of the assignment. I am estimating that I will be able to submit the assignment on [New Due Date, 2 days after the original due date]. I will make sure to keep you updated on my progress and appreciate your consideration of this request.

Please let me know if this is feasible, and if there's any further information I need to provide. I am committed to my studies and am eager to get back on track as soon as possible. Your support and understanding during this challenging time mean a great deal to me, and I am thankful for your dedication to our academic success.

Thank you for taking the time to consider my request. I look forward to your response and to continuing to learn from you throughout the semester.

Sincerely,

[Your Name]
```

---

## Prompt 5 — Prompt with Clear Constraints

### Input Prompt

```text
You are a university student writing a formal email to your doctor. Write an email asking for a 2-day extension for an assignment because of a family emergency. The email must be polite, professional, and respectful. Keep it between 20 and 40 words. Include a clear subject line, a short apology, the reason for the delay, the request for extension, and a closing thank-you.
```

### Output

```text
Subject: Urgent: Assignment Extension Request
Dear Doctor, 
I apologize, a family emergency 
requires a 2-day extension.
Thank you.
```

---

# Comparison of the Outputs

After testing the five prompts, the **Detailed Prompt (Prompt 3)** gave the best result overall.

## Why Prompt 3 was the best

Prompt 3 produced the most balanced output because it gave the model enough guidance without making it too vague or too restrictive. It clearly defined:

* **who the AI should act as** → a university student
* **what the AI should do** → write an email requesting a 2-day extension
* **the context** → a family emergency caused the delay
* **the tone** → formal and respectful
* **extra instructions** → apologize and ask politely for understanding

Because of that, the output was clear, professional, relevant to the task, and complete enough to look like a realistic email.

## Comparison with the other prompts

### Prompt 1 — Basic Prompt

This was the weakest result. The prompt was too general, so the model became confused by the word **doctor** and assumed that the user might actually mean **professor** or **instructor**. Instead of directly producing a clean email, it added unnecessary explanation before the response. This shows that vague prompts can lead to confusion and less accurate outputs.

### Prompt 2 — Improved Prompt

This was better than Prompt 1 because it included the **reason** for the extension and the exact **2-day request**. As a result, the output was more accurate and relevant. However, it still did not control the tone and style as strongly as Prompt 3, so it was good but not the strongest.

### Prompt 3 — Detailed Prompt

This gave the best overall result. It was clear, formal, complete, and directly aligned with the task. It included all the important details without becoming overly long or adding unnecessary emotional language.

### Prompt 4 — Creative Prompt

This produced a polite and human-sounding email, but it became **too long** and added extra details that were not really necessary for a simple extension request. It sounded good, but it was less efficient and less focused than Prompt 3.

### Prompt 5 — Prompt with Clear Constraints

This prompt forced the output to stay between **20 and 40 words**, which made the response too short. Even though the model followed the word limit, the email lost important details and ended up sounding incomplete. So while the constraints worked, they were too strict for this task.

# Final Conclusion

The **Detailed Prompt (Prompt 3)** gave the best result because it balanced clarity, context, tone, and completeness. It was specific enough to guide the model well, but not so restrictive that the response became too short or unnatural. This experiment showed that better prompts lead to better outputs, especially when they include the right amount of detail.
