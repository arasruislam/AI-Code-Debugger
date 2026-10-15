# File: utils/prompts.py


def build_debug_prompt(selected_option: str, pasted_code: str = "") -> str:
    """Builds the prompt for Gemini API based on the selected option ('Hints' or 'Solution with code')."""
    if selected_option == "Hints":
        prompt = (
            "You are an expert programming mentor and code debugger.\n"
            "Analyze the provided code error (from the screenshot and/or pasted code).\n"
            "Please provide:\n"
            "1. **Error Explanation**: Clearly explain what the error or bug is and why it is happening.\n"
            "2. **Debugging Hints**: Provide clear, step-by-step hints and conceptual guidance so the user can fix the bug themselves, without giving away the full final code directly.\n"
            "Respond in a clean, well-structured Markdown format (you may use English or Bengali as appropriate)."
        )
    else:
        prompt = (
            "You are an expert software engineer and code debugger.\n"
            "Analyze the provided code error (from the screenshot and/or pasted code).\n"
            "Please provide:\n"
            "1. **Error Explanation**: Clearly identify the bug/error and explain the root cause.\n"
            "2. **Corrected Code**: Provide the complete, fixed, and working code inside a properly formatted code block.\n"
            "3. **Key Changes Made**: Briefly highlight what was changed to fix the issue.\n"
            "Respond in a clean, well-structured Markdown format."
        )

    if pasted_code and pasted_code.strip():
        prompt += (
            f"\n\n### User's Pasted Code / Error:\n```\n{pasted_code.strip()}\n```"
        )

    return prompt
