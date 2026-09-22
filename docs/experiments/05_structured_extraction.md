# Experiment 05 — Structured Extraction

## Objective

Extract structured customer-support information from
unstructured customer messages.

## Input

A free-form customer message.

## Output

ExtractedTicket:

- customer_id
- product
- sentiment
- priority
- category

## Architecture

Customer Message
      ↓
LLM
      ↓
JSON
      ↓
JSON Parsing
      ↓
Pydantic Validation
      ↓
ExtractedTicket

## Experiments

### Valid input

Test a normal customer message containing:

- customer ID
- product
- issue
- emotional tone

### Missing information

Test a message with no customer ID.

Expected:

customer_id = null

### Invalid enum

Simulate:

priority = "critical"

Expected:

Pydantic validation failure.

### Invalid JSON

Simulate malformed JSON.

Expected:

ExtractionError.

## Lessons

Valid JSON does not guarantee valid application data.

LLM output must be treated as untrusted input.

Pydantic provides an application-level validation boundary.

## Next Experiment

Integrate structured extraction with agent state.