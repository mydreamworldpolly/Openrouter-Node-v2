English Description
This GitHub project introduces a ComfyUI Node that enables seamless interaction with OpenAI-compatible LLM APIs(including OpenRouter) and Azure OpenAI. The node supports various functionalities, such as:

Text-to-Text Output: Generate text outputs based on an input text prompt.
Example Application: Input a design theme and get a "flux1 drawing prompt" as output for artistic workflows.

Image-to-Text Output: Utilize multimodal LLMs (e.g., Claude 3 Haiku, GPT-4o) to process images and generate descriptive text.
Example Application: Input an image to create its textual description for use in image-to-image workflows.

Key Features:
Flexible API integration: Supports OpenAI-compatible endpoints, including OpenRouter and Azure OpenAI.
Easy configuration: Requires the input of API endpoint links, API keys, and model names. If the model name is not specified, the node defaults to Azure OpenAI's endpoint.
Versatile use cases: Ideal for workflows involving creative text generation and multimodal content interpretation.
<img width="422" alt="image" src="https://github.com/user-attachments/assets/850ed8a0-90fe-4885-a677-6847fee84655" />

Forked from: https://github.com/valofey/Openrouter-Node
Improvements:
Added support for Azure OpenAI.
Simplified image upload code and adjusted timeouts to improve compatibility with multimodal LLMs, ensuring smoother image uploads. Suggested resizing images to dimensions below 1024x1024 before uploading.
Fixed minor issues: Inputting an image is now optional, allowing users to input text prompts only. Temperature can now be adjusted in 0.1 steps.


中文说明
本 GitHub 项目提供了一个 ComfyUI 节点，能够与包括 OpenRouter 和 Azure OpenAI 在内的 OpenAI 兼容 LLM API 无缝交互。此节点支持以下功能：

文字转文字输出：根据输入的文字 prompt 生成输出文字。
应用案例：输入一个制图主题，输出一个“flux1 绘图 prompt”，用于艺术创作工作流。

图片转文字输出：利用多模态 LLM（如 Claude 3 Haiku, GPT-4o）处理图片并生成描述性文字。
应用案例：输入一张图片，生成图片描述，用于图生图工作流。

核心功能：
灵活的 API 集成：支持 OpenAI 兼容的连接点，包括 OpenRouter 和 Azure OpenAI。
便捷的配置：只需输入 API 的 endpoint 链接、API key 和 model 名称。若未指定 model 名称，默认为 Azure OpenAI 的连接点。
多样的应用场景：适用于创意文本生成与多模态内容解释的工作流。

forked from https://github.com/valofey/Openrouter-Node
改进内容：
增加了对 Azure OpenAI 的支持。
简化了图片上传部分代码及 timeout，使得向多模态大模型上传图片更顺畅。建议上传图片前将尺寸降低到 1024x1024 以下。
修改了一些小问题：现在输入图片变为可选项，允许仅输入文字 prompt。温度（temperature）现在可以以 0.1 为步进值进行调整。
