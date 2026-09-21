# Experiment 02 — Agent Loop

## Objective

Understand how an LLM can decide to use a tool and continue
reasoning after receiving the tool result.

## Architecture

User
  ↓
LLM
  ↓
Tool request
  ↓
Python tool
  ↓
Tool result
  ↓
LLM
  ↓
Final response

## Tool

get_customer_status

## Test Input

Customer C001 asks whether their account is active.

## Observations

Record:

- Did the model call the tool?
- Did it use the correct tool?
- Did it provide the correct argument?
- Did the application execute the tool?
- Did the model use the tool result?
- How many turns were required?

## Problems

Record unexpected behavior.

## Lessons Learned

Record what you learned about:

- tool_use
- stop_reason
- message history
- tool execution
- tool results
- agent loops

## Next Experiment

Replace the educational customer-status tool
with a real knowledge-base search tool.