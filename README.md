# README

本项目是一个基于 Streamlit 的“AI Coding Assistant”，依赖 OpenAI 的 GPT 模型来自动修复与生成代码。代码主要分为以下部分：

1. **OpenAI API 配置**  
   - `openai.api_key`：设置 API 密钥。  
   - `get_response_from_openai(prompt, model="...")`：封装了与 GPT 的交互逻辑。

2. **功能函数**  
   - `fix_code(code_snippet, language="Python")`：自动修复用户提交的代码，并返回修复后代码与解释。  
   - `generate_code(task_description, language="Python", ...)`：根据需求生成指定语言的示例代码，可选是否加注释。

3. **辅助样式**  
   - `local_css(file_name)`：加载本地 CSS 样式。  
   - `page_bg_img`：定义页面背景图片的样式。

4. **主函数（main）**  
   - 使用 `Streamlit` 构建 UI，提供两个主要功能：**Fix Code** 和 **Generate Code**。  
   - 根据用户输入或选择调用对应的函数，并在页面上展示结果。

---

## 使用方法

已经使用streamlit网站分享平台https://share.streamlit.io/制作为开源网站

网址: https://fdu-aicourse-code-bot.streamlit.app/
