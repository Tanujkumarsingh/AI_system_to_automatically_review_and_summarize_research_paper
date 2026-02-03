# from google import genai
# from config import GEMINI_API_KEY, MODEL_NAME

# client = genai.Client(api_key=GEMINI_API_KEY)

# def review_paper(draft):
#     prompt = f"""
#     Review the following draft.
#     Suggest improvements and refine language.

#     Draft:
#     {draft}
#     """

#     return client.models.generate_content(
#         model=MODEL_NAME,
#         contents=prompt
#     ).text

# -    -------------------------------------------------------====================================----- #
# code with llm

from llm import llm


def review_paper(draft: str) -> str:
    """
    Reviews and refines the generated research paper draft.

    Responsibilities:
    - Improve academic tone and clarity
    - Remove redundancy
    - Refine explanations
    - Preserve the original structure
    """

    if not isinstance(draft, str) or not draft.strip():
        return "Review failed: Empty draft provided."

    prompt = f"""
You are an academic peer reviewer.

Review the research paper draft below and:
- Improve clarity and academic tone
- Remove redundancy
- Refine explanations where needed
- Keep the original structure intact
- Do NOT add new content

Draft:
{draft}

Return only the revised and polished version.
"""

    try:
        response = llm.invoke(prompt)

        # Safety: ensure string output
        output = response.content
        if isinstance(output, list):
            output = "\n".join(output)

        return output.strip()

    except Exception as e:
        return f"Review step failed due to error: {str(e)}"

