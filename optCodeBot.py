import openai
import streamlit as st

openai.api_key = "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"

def get_response_from_openai(prompt, model="gpt-4o"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def fix_code(code_snippet, language="Python"):
    prompt = f"""
        You are a professional software engineer. Please fix the following {language} code.
        Requirements:
        1. Provide two parts in your output:
        - Repaired Code: only include the complete {language} code after fixing.
        - Explanation: explain what you changed and why.
        2. Output only code blocks and text, without extra content.

        The code to fix is:
        ```{language}
        {code_snippet}
        Please follow this exact format: Repaired Code (use Markdown code block):
        # Repaired code
        # ...
        Explanation: (Explain the issues and why you fixed them)
        """ 
    return get_response_from_openai(prompt)

def generate_code(task_description, language="Python", with_comments=False, comment_language="English"): 
    if with_comments: 
        if comment_language == "English": 
            comment_prompt = "Use English comments in the code, " 
        else: 
            comment_prompt = "Use Chinese comments in the code, " 
    else: comment_prompt = "Do not add any comments, "

    prompt = f"""
    You are a professional software engineer. Please generate {language} code based on the following requirements: {task_description} Requirements:

    {comment_prompt}
    Output only the final complete code, without extra explanation.
    Use Markdown code block format for the output.
    Please follow this exact format:
    # Generated code
    # ...
    """ 
    return get_response_from_openai(prompt)

def local_css(file_name: str):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.title("AI Coding Assistant") 
    local_css("./style.css")
    st.write("Powered by OpenAI GPT")

    task_option = st.selectbox("What would you like to do?", ["Fix Code", "Generate Code"])

    if task_option == "Fix Code":
        st.subheader("Fix Your Code")
        code_input = st.text_area("Paste your code here:", height=200)
        language = st.selectbox("Choose a programming language:", ["Python", "C++", "Java", "JavaScript", "Other"])

        if st.button("Fix Code"):
            if code_input.strip():
                with st.spinner("Fixing Code, Please Wait ..."):
                    fixed_result = fix_code(code_input, language)

                parts = fixed_result.split("Explanation:")
                if len(parts) == 2:
                    repaired_code = parts[0].strip()
                    explanation = parts[1].strip()
                    st.subheader("Repaired Code:")
                    st.markdown(f"```\n{repaired_code}\n```")
                    st.subheader("Explanation:")
                    st.write(explanation)
                else:
                    st.markdown(f"```\n{fixed_result}\n```")
            else:
                st.warning("Please provide a code snippet to fix.")

    elif task_option == "Generate Code":
        st.subheader("Generate Code")
        task_description = st.text_area("Describe your task:", height=150)
        language = st.selectbox("Choose a programming language:", ["Python", "C++", "Java", "JavaScript", "Other"])

        with_comments_option = st.selectbox("Do you need comments?", ["Yes", "No"])
        
        comment_language_option = None
        if with_comments_option == "Yes":
            comment_language_option = st.selectbox("Comment language:", ["English", "Chinese"])

        if st.button("Generate Code"):
            if task_description.strip():
                with st.spinner("Generating Code, Please Wait ..."):
                    need_comments = (with_comments_option == "Yes")
                    generated_result = generate_code(
                        task_description, 
                        language, 
                        need_comments, 
                        comment_language_option
                    )

                st.subheader("Generated Code:")
                st.markdown(f"```\n{generated_result}\n```")
            else:
                st.warning("Please provide a task description.")

if __name__ == "__main__":
    main()
