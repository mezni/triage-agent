# Experiment 01 — Baseline LLM Application

## Objective

Build the simplest possible support-ticket AI application
before introducing tools or agent behavior.

## Architecture

Support Ticket
    ↓
System Prompt
    ↓
LLM
    ↓
JSON
    ↓
Pydantic
    ↓
TriageResult

## Input

Ticket T001:

"I cannot log into my account. I requested a password reset
but the email never arrives."

## Expected Behavior

The model should identify:

- category
- priority
- reasoning
- customer response

## Actual Behavior

Record the model's behavior here.

## Observations

Record:

- Was the category correct?
- Was the priority reasonable?
- Was the response useful?
- Did the model follow the requested JSON structure?
- Did Pydantic validation succeed?

## Problems

Record anything unexpected.

## Lessons Learned

Record what you learned about:

- prompts
- LLM responses
- structured output
- validation

## Next Experiment

Introduce the agent loop and tool calling.