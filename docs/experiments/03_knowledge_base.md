# Experiment 03 — Knowledge Base Tool

## Objective

Add a knowledge base tool to the support agent so that
company-specific information can be retrieved before
answering customer questions.

## Architecture

Customer
   ↓
Agent
   ↓
search_knowledge_base
   ↓
knowledge_base.json
   ↓
Retrieved articles
   ↓
Agent
   ↓
Customer response

## Test Cases

### Test 1 — Dark mode

Question:

Does your application support dark mode?

Expected behavior:

The agent searches the knowledge base and discovers
that dark mode is currently unavailable.

### Test 2 — Password reset

Question:

I cannot receive my password reset email. What should I do?

Expected behavior:

The agent searches the knowledge base and uses the
password reset article.

### Test 3 — Unknown information

Question:

Do you support biometric authentication?

Expected behavior:

The agent should not invent an answer if the knowledge
base contains no relevant information.

## Observations

Record:

- Did the agent call the knowledge base?
- What query did it generate?
- What articles were returned?
- Did it use the retrieved information?
- Did it invent information?
- Was the response grounded?

## Lessons Learned

Record what you learned about:

- tool-based retrieval
- grounding
- tool results
- knowledge sources
- hallucination risk

## Next Experiment

Improve tool schema and deliberately introduce a bad
tool schema.