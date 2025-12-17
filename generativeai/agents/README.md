# Agents framework

> An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective. It combines reasoning, planning, and the execution of actions (often via external tools) to fulfill tasks.

Resources:
- [Agentic design pattern](https://github.com/sarwarbeing-ai/Agentic_Design_Patterns/blob/main/Agentic_Design_Patterns.pdf)
- [All Agentic Architecture](https://github.com/FareedKhan-dev/all-agentic-architectures)
- [Swarm Multi-Agent Pattern](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/swarm/)
- [Github - Agent in Production](https://github.com/NirDiamant/agents-towards-production)
- [Github - AI Engineering Hub](https://github.com/patchy631/ai-engineering-hub)

# “Agentic" solutions

## ADK+Agent Engine (GCP)

- [ADK](https://github.com/google/adk-python)
- [GCP - VertexAI Agent Engine](https://docs.cloud.google.com/agent-builder/agent-engine/overview)

## Strands+AgentCore (AWS)

- [Github strands](https://github.com/strands-agents/sdk-python)
  - [Swarm Multi-Agent Pattern](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/swarm/)
- [AWS - AgentCore](https://aws.amazon.com/fr/bedrock/agentcore/)

## Kagent (Kubernetes/Openshift)

- [Github - Kagent](https://github.com/kagent-dev/kagent)
- [Github - Kagenti](https://github.com/kagenti/kagenti)

## Databricks (AgentBricks)

 Coming soon

# GenAI Frameworks
## Langchain (modular)

Build custom LLM agents using reusable components. Design flexible, logic-drivenagent flows.
- Tool chaining
- Memomy modules
- Agent execution

## CrewAI (Collaborative)

Mutli-agent system with role assigment and task coordination. Ideal for building agent teams with structure.
- Task orchestration
- Role distribution
- Agent teamwork

## AutoGen (Microsoft)

Enable LLM-to-LLM and user-LLM collaboration via dialogue. Great for multi-turn LLM planning tasks.
- Assistant-user loops
- Structured dialogue planning
- Tool support

## MetaGPT (Engineering)

Simulates dev teams to build structured software with agents.
- Roles for Pm, dev, QA
- Design-first approach
- Output validation

## LangGraph (reactive)

Graph-based execution model for reactive, stateful flows. Excellent for memory and loop heavy logic.
- Node-based task flow
- Cycles and retries
- Multi-agent workflows

## AgentOps (Monitoring)

Track and analyze agent behavior in production. Real-time dasboards for running agents.
- Agent health metrics
- Logging and debugging
- Performance alerts

## Superagent (open-source)

Drop-in platform with built-in-tools UI and API endpoints. Fast ssndbox for agent experiments.
- VectorDB + memory
- REST API access
- UI for agent interaction

## Haystack agents (dev-centric)

Optimized for RAG pipelines and reasoning agents. Best suited for search + logic-based agents.
- Modular piplines
- LLML integration
- Multi-turn task

# References

- [Arxiv - Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416)
- [Arxiv - Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/pdf/2402.01030)
- [Arxiv - Evaluate Agent with Agent](https://arxiv.org/pdf/2410.10934)
- [Github - Bee Agent Framework](https://github.com/i-am-bee/bee-agent-framework)
- [Github HF smolagents](https://github.com/huggingface/smolagents)
- [AWS Labs Github - Multi-Agent Orchestrator](https://awslabs.github.io/multi-agent-orchestrator/)
  - [AWS Labs Github - AWS Lambda Python with Multi-Agent Orchestrator](https://awslabs.github.io/multi-agent-orchestrator/cookbook/lambda/aws-lambda-python/)
- [Linkedin - AI Agents vs not AI Agent](https://www.linkedin.com/posts/rakeshgohel01_most-people-think-ai-agents-are-just-glorified-activity-7272981562130874368-z3Pe?utm_source=share&utm_medium=member_desktop)
- [Linkedin - McKinsey & QuantumBlack: Why agents are the next frontier of generative AI](https://www.linkedin.com/posts/kierangilmurray_httpslnkdinedvuwsg-activity-7274004017339412480-YX8v?utm_source=share&utm_medium=member_desktop)
    - [Book - Why agents are the next frontier of generative AI?](https://media.licdn.com/dms/document/media/v2/D4E1FAQEZ7PUZ0d1qyg/feedshare-document-pdf-analyzed/B4EZPAygZ.H0Ac-/0/1734106290837?e=1736985600&v=beta&t=JGxItaVIBz4YdFV5O39mH4cRm9MWjSU6-d3EHWebq_8)
- [LinkedIn - Agentic AI Frameworks & AutoGen](https://www.linkedin.com/feed/update/urn:li:activity:7273004216556703744?utm_source=share&utm_medium=member_desktop)
  - [Agentic AI Frameworks & AutoGen](https://media.licdn.com/dms/document/media/v2/D4E1FAQFjNADgjVlY9A/feedshare-document-pdf-analyzed/B4EZO7mr2rHEAc-/0/1734019323536?e=1736985600&v=beta&t=EUiLajoFaWSoZxdq8hb4XHJMvX6czQyhD_4I8kI-3hQ)
- [Linkedin - Agentic Keynote/slides](https://www.linkedin.com/posts/cornellius-yudha-wijaya_agent-framework-and-autogen-activity-7273004022075199490-GIoq?utm_source=share&utm_medium=member_desktop)
  - [Keynote/slide](https://media.licdn.com/dms/document/media/v2/D4E1FAQGAqK13SBspLg/feedshare-document-pdf-analyzed/B4EZO7lmZHHsAs-/0/1734019036698?e=1736985600&v=beta&t=H1KpBC4plhcpzN-yptuw-V3BRRif9UXg3cIm-9Ji0Uw)
- [Huggingface - SmolAgents](https://huggingface.co/blog/smolagents)
  - [Keynote/slide](https://media.licdn.com/dms/document/media/v2/D561FAQHwYxX7KLUU7A/feedshare-document-pdf-analyzed/B56ZRqgzlPGoAY-/0/1736953780301?e=1737590400&v=beta&t=Iz2Yn3OvdNGzq-49feRQSoiuO5VzsMbBSOl2_XC_Gbk)
- [Github - Anthropic cookbook AI Agent](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
- [Github - Browser use (open source openai operator)](https://github.com/browser-use/browser-use)
- [Data Engineering weekly - The ascending arc of AI Agents](https://www.dataengineeringweekly.com/p/the-ascending-arc-of-ai-agents)


# Learning
- [HF Agent Course](https://huggingface.co/learn/agents-course/en/unit0/introduction)
  - [Github - smolagent](https://github.com/huggingface/smolagents)
  - [blog post](https://huggingface.co/blog/smolagents)
