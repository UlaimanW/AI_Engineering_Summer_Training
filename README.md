# Prompting Fundamentals — Comparing 5 Prompts for the Same Task

## Chosen Task

Write an email to a doctor asking for a **2-day extension** for an assignment because of a **family emergency**.

---

## Prompt 1 — Basic Prompt

### Input Prompt

```text id="a4w9pq"
Write an email to a doctor asking for more time to submit an assignment. Keep it less than 120 words.
```

### Output

```text id="8b1nwd"
Subject: Request for Assignment Extension

Dear Dr. [Last Name],

I am reaching out to request a short extension on the current assignment that is due soon. Due to unforeseen circumstances, I require a bit more time to complete it to the best of my abilities. I am confident that with a brief extension, I will be able to submit quality work. I would greatly appreciate an extra [number] of days to complete the assignment.

Thank you for your understanding.

Sincerely,
[Your Name]
```

---

## Prompt 2 — Improved Prompt

### Input Prompt

```text id="w6mk3t"
Write an email to a doctor asking for a 2-day extension to submit an assignment because of a family emergency. Keep it less than 120 words.
```

### Output

```text id="x2rz0m"
Subject: Urgent: Assignment Extension Request

Dear Doctor,

I'm writing to request a 2-day extension on the upcoming assignment due to a sudden family emergency that requires my immediate attention. I apologize for any inconvenience and will submit the assignment as soon as possible. I appreciate your understanding in this matter.

Sincerely,
[Your Name]
```

---

## Prompt 3 — Detailed Prompt

### Input Prompt

```text id="q9df2l"
You are a university student. Write a formal and respectful email to your doctor asking for a 2-day extension on an assignment. Explain that you had a family emergency and could not finish the work on time. Apologize for the inconvenience and ask politely for understanding. Keep it less than 120 words.
```

### Output

```text id="z3tn8f"
Subject: Request for Assignment Extension

Dear Doctor,

I am writing to request a 2-day extension on the current assignment due to a family emergency that required my immediate attention. Unfortunately, I was unable to complete the work on time. I apologize for the inconvenience and kindly ask for your understanding in this matter. I appreciate your consideration and look forward to your response.

Sincerely,
[Your Name]
```

---

## Prompt 4 — Creative Prompt

### Input Prompt

```text id="k4rc1v"
You are a university student writing to a doctor you respect. Write a sincere and professional email asking for a 2-day extension for an assignment after a family emergency affected your ability to complete it on time. Make the email sound genuine, respectful, and appreciative rather than robotic. Keep it less than 120 words.
```

### Output

```text id="u7mp5e"
Dear Dr. [Last Name],

I'm reaching out to request a 2-day extension on the current assignment due to a recent family emergency that has impacted my ability to complete it on time. I'm grateful for your understanding and appreciate your consideration. I'm committed to submitting quality work and am confident that this brief extension will allow me to do so.

Sincerely,
[Your Name]
```

---

## Prompt 5 — Prompt with Clear Constraints

### Input Prompt

```text id="m8hy6q"
You are a university student writing a formal email to your doctor. Write an email asking for a 2-day extension for an assignment because of a family emergency. The email must be polite, professional, and respectful. Include a clear subject line, a short apology, the reason for the delay, the request for extension, and a closing thank-you. Keep it less than 120 words.
```

### Output

```text id="n5tx4r"
Subject: Request for Assignment Extension due to Family Emergency

Dear Doctor,

I apologize for any inconvenience. Unfortunately, I've encountered a family emergency requiring my immediate attention. I kindly request a 2-day extension on the upcoming assignment. I appreciate your understanding and flexibility during this challenging time.

Thank you for your consideration.

Sincerely, [Your Name]
```

---

# Comparison of the Outputs

After testing the five prompts, the **Prompt with Clear Constraints (Prompt 5)** gave the best result overall.

## Why Prompt 5 was the best

Prompt 5 produced the strongest result because it clearly guided the model on **what to include** in the email. It did not only describe the task and context, but also specified the required structure and content of the response. It told the model to include:

* a **clear subject line**
* a **short apology**
* the **reason for the delay**
* the **request for a 2-day extension**
* a **closing thank-you**
* and to keep the response **under 120 words**

Because of that, the output was complete, polite, professional, and well-structured while still staying concise.

## Comparison with the other prompts

### Prompt 1 — Basic Prompt

The basic prompt produced a decent result, but it was still too general. It asked for “more time” without specifying the reason or the exact number of days. Because of that, the output included placeholders such as **[number] of days** and **unforeseen circumstances** instead of clearly mentioning the family emergency and the 2-day extension.

### Prompt 2 — Improved Prompt

This prompt performed better than Prompt 1 because it added the **2-day extension** and the **family emergency**. The result was short and clear, but it was still quite simple and lacked some of the formal structure and completeness seen in Prompt 5.

### Prompt 3 — Detailed Prompt

This prompt gave a strong result. It was formal, respectful, and directly addressed the reason for the extension. It also included an apology and a polite request for understanding. However, compared with Prompt 5, it did not explicitly enforce a subject line, closing thank-you, or a more structured email format.

### Prompt 4 — Creative Prompt

This prompt produced a natural and respectful email, and the tone felt more personal. However, it did not include a subject line, which made it slightly weaker as a complete academic email. It was good in tone, but not as complete in structure as Prompt 5.

### Prompt 5 — Prompt with Clear Constraints

This prompt gave the best result because it combined **context**, **tone**, **structure**, and **specific constraints**. It clearly instructed the model to include the most important elements of a formal extension request email, so the final output was the most complete and polished among all five responses.

# Final Conclusion

The **Prompt with Clear Constraints (Prompt 5)** gave the best result because it was the most specific and practical prompt. It guided the model not only on the purpose of the email, but also on the exact structure and important details that needed to appear in the response. This made the final output more complete, professional, and usable than the outputs generated by the other prompts.
