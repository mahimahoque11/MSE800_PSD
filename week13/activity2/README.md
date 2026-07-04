# LLM-Powered New Zealand Travel Itinerary Generator

## Overview

This project demonstrates the use of prompt engineering techniques to generate a detailed travel itinerary for a trip around New Zealand using a Large Language Model (LLM). The itinerary was generated using **Google Gemini AI Studio**, while **OpenAI Tokenizer** was used to analyze the prompt's tokenization.

The project focuses on designing an optimized prompt that provides clear instructions, sufficient context, structured input data, and a specified output format to produce accurate and useful travel recommendations.

---

## Objectives

- Design an optimized prompt for an LLM.
- Generate a 7-day New Zealand travel itinerary.
- Apply prompt engineering techniques learned in class.
- Analyze the prompt using the OpenAI Tokenizer.

---

## Prompt Engineering Techniques Used

The prompt was designed using the following techniques:

- **Role Prompting** – Assigned the model the role of an experienced New Zealand travel planner.
- **Instruction Prompting** – Clearly defined the required task.
- **Contextual Prompting** – Provided background information about the traveller.
- **Structured Prompting** – Specified the required output format as a table.
- **Negative Prompting** – Specified what should not be included in the itinerary.

These techniques improve the quality, relevance, and consistency of the generated response.

---

## AI Model Used

- **Platform:** Google AI Studio
- **Model:** Gemini 3.5 Flash

---

## Tokenization

The optimized prompt was analyzed using the **OpenAI Tokenizer**.

### Results

- **Total Tokens:** 224
- **Total Characters:** 1107

Tokenization breaks text into smaller units called **tokens**, which are processed by Large Language Models. Understanding token count helps estimate model input size, response limits, latency, and API usage.

A detailed explanation is available in **tokenization.md**.

---

## Repository Contents

| File | Description |
|------|-------------|
| `README.md` | Project overview and documentation |
| `optimized_prompt.txt` | The final optimized prompt used in Gemini AI Studio |
| `sample_itinerary.md` | AI-generated 7-day New Zealand travel itinerary |
| `tokenization.md` | Tokenization analysis using OpenAI Tokenizer |

---

## How to Run

1. Open Google AI Studio.
2. Select the **Gemini 3.5 Flash** model.
3. Paste the contents of `optimized_prompt.txt` into the prompt editor.
4. Run the prompt to generate the travel itinerary.
5. Use the OpenAI Tokenizer to analyze the prompt and compare the token count with the results documented in `tokenization.md`.

---

## Learning Outcomes

Through this project I learned how:

- Prompt structure affects AI-generated responses.
- Providing clear instructions and context improves output quality.
- Negative prompting helps avoid unwanted responses.
- Tokenization influences model efficiency and context length.
- Prompt engineering can be used to produce structured and reliable outputs from Large Language Models.

---

## Author

**Mahima Hoque Mim**

MSE800 – Machine Learning  
Week 13 Activity 2 – LLM-Powered New Zealand Travel Itinerary Generator