# LLM-FullStack-Journey 🚀

欢迎来到我的 AI 大模型全栈开发学习仓库！本项目用于系统化地记录我**从零基础小白到大模型全栈开发工程师**的蜕变历程。

在这里，我将严格跟着硬核训练营的步伐，死磕技术，把每天的理论思考、代码实战和企业级项目落地过程通通沉淀下来。

---

## 🗺️ 学习大纲 & 核心版块

我的整个学习链路将分为两大阶段，双线进阶：

### 🎯 第一阶段：应用开发线（FastAPI + 智能体生态）
* **Python 基础与全栈铺垫**：精通 Python 核心语法、FastAPI 后端开发，打牢 MySQL 与 Redis 数据库根基。
* **Prompt 提示词工程**：掌握结构化提示词（Structured Prompts）、Few-shot 以及 CoT（思维链）高级工程技术。
* **大模型 API 开发**：多轮对话管理、流式传输（Streaming）与 Function Calling（函数调用）实战。
* **LangChain 核心框架**：深入 Components（Models, Prompts, Memory, Chains），打造企业级 RAG（检索增强生成）知识库系统。
* **LangGraph 高级智能体**：构建具备自主规划（Planning）与记忆（Memory）能力的复杂多智能体（Multi-Agent）流。

### 🧠 第二阶段：算法微调线（大模型底层微调）
* **模型参数与量化**：理解大模型核心微调理论。
* **Llama-Factory 实战**：上手主流微调框架，打通数据准备、全量/LoRA 微调、模型评估与部署的全流程。

---

## 🛠️ 环境与工具准备

为了保证项目的顺利运行，后续开发将基于以下环境：
-   **开发语言**：Python 3.10+
-   **关键依赖库**：`langchain`, `openai`, `fastapi`, `python-dotenv`, `chromadb`
-   **代码管理**：严格利用 `.gitignore` 过滤大模型权重（`.pth`/`.bin`）及敏感密钥（`.env`），确保仓库轻量与安全。

---

## 📂 仓库目录规划

随着课程推进，我将建立以下清晰的目录结构：
```text
.
├── 01_Python_FastAPI/      # 后端全栈与数据库基础
├── 02_Prompt_Engineering/   # 提示词工程与实验最佳实践
├── 03_LangChain_RAG/       # LangChain 应用与向量知识库搭建
├── 04_Agent_Systems/       # LangGraph 多智能体系统实战
├── 05_LLM_Finetuning/      # Llama-Factory 模型微调记录
└── README.md               # 项目主页导航
