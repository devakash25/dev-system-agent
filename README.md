# DEV_System: Multi-Agent AI System Auditor 🚀
**Developed by Akash | dev_spark**

An autonomous multi-agent framework built using the **Google Agent Development Kit (ADK)** and **Gemini 2.5 Flash**. This system demonstrates a high-precision "Specialist-Critic" architecture designed for automated system auditing.

## 🤖 Architecture Overview
This project utilizes a sequential multi-agent design to eliminate hallucinations and ensure technical accuracy:

1.  **Specialist Agent:** Equipped with custom Python tools to interface with the host OS and retrieve real-time system metrics.
2.  **Critic Agent:** Acts as the quality gate. It audits the Specialist's output and appends a `DEV-VERIFIED` stamp only upon successful validation.



## 📊 Evaluation Results
This agent was stress-tested using the `adk eval` suite with the following results:
* **Tool Trajectory Average Score:** **1.0** (Perfect execution of tool-calling logic)
* **Response Match Score:** **0.8+** (Consistent formatting and reliability)

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **AI Framework:** Google ADK
* **Model:** Gemini 2.5 Flash
* **Infrastructure:** Google Cloud Shell / Streamlit Cloud


graph TD
    User((User)) -->|Query| Specialist[Specialist Agent]
    Specialist -->|Calls Tool| OS[Python: get_system_status]
    OS -->|Raw Data| Specialist
    Specialist -->|Draft Response| Critic[Critic Agent]
    Critic -->|Verifies Data| Final{Final Output}
    Final -->|Success| Out[DEV-VERIFIED Response]
