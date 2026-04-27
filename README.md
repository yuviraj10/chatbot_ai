# chatbot_ai
Built a conversational AI chatbot using Python and Google Gemini 2.5 Flash API with multi-turn memory Integrated free-tier LLM API with proper error handling and session-based conversation history Designed a clean CLI interface with graceful exit and input validation
🔍 Problem Statement

The provided financial document analyzer system contained:

Deterministic bugs affecting execution

Inefficient and vague prompts

Improper input handling

Weak error management

External dependency failure issues (LLM quota errors)

The objective was to debug the system, optimize prompts, and make the application stable and production-ready.

 Deterministic Bugs Identified & Fixed
1️⃣ Incorrect File Path Handling

Issue:
Uploaded file path was not passed dynamically to Crew. The system attempted to use a hardcoded default PDF path.

Fix:
Modified run_crew() to correctly pass:

run_crew(query=query.strip(), file_path=file_path)

This ensures the uploaded document is analyzed correctly.

2️⃣ Hardcoded Default Paths in Tools

Issue:
PDF reader tool used a default path (data/sample.pdf) instead of dynamic input.

Fix:
Updated tool to accept and use injected file_path from Crew inputs.

3️⃣ Async / Sync Inconsistencies

Issue:
Some tools were declared as async but were not awaited properly.

Fix:
Converted them to synchronous functions to match CrewAI execution flow.

4️⃣ Poor Error Handling

Issue:
Application crashed on external API failure.

Fix:
Added structured try–except blocks and graceful fallback responses.

5️⃣ External LLM Dependency Failure

Issue:
OpenAI quota limitations caused RateLimitError, crashing the system.

Fix:
Implemented fallback mechanism:

If LLM fails → return structured rule-based analysis

API remains operational

This ensures high availability and reliability.

Prompt Optimization Improvements

The original prompts were vague and unstructured.

 Before:

"Analyze this financial document."

 After:

Structured prompt enforcing:

Executive Summary

Revenue & Profit Analysis

Key Financial Indicators

Risk Assessment

Investment Recommendation (Buy/Hold/Sell)

Confidence Level

This improves:

Clarity

Output consistency

Analytical depth

Reasoning quality
