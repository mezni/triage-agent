# Experiment 03 — Bad Tool Schema

## Objective

Understand how a poorly designed tool schema affects
agent behavior.

## Hypothesis

If the tool schema does not accurately describe the
Python function, the model may generate arguments that
cannot be executed by the application.

## Deliberate Fault

The Python function expects:

- customer_id
- category
- priority
- summary

The bad schema exposes:

- customer
- type
- level
- description

## Test

Ask the agent:

"Create a high priority billing ticket for customer C002
because they were charged twice."

## Expected Failure

Possible outcomes:

- incorrect argument names
- missing arguments
- tool execution failure
- agent retry
- agent confusion
- incorrect final response

## Actual Behavior

Record exactly what happened.

## Diagnosis

Explain:

- what the model saw
- what arguments it generated
- what the Python function expected
- where the contract broke

## Lesson

A tool schema is an interface contract between the model
and the application.

## Next Step

Fix the schema.