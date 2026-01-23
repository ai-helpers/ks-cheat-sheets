# Agents framework

> An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective. It combines reasoning, planning, and the execution of actions (often via external tools) to fulfill tasks.

Resources:
- [Agentic design pattern](https://github.com/sarwarbeing-ai/Agentic_Design_Patterns/blob/main/Agentic_Design_Patterns.pdf)
- [All Agentic Architecture](https://github.com/FareedKhan-dev/all-agentic-architectures)
- [Swarm Multi-Agent Pattern](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/swarm/)
- [Github - Agent in Production](https://github.com/NirDiamant/agents-towards-production)
- [Github - AI Engineering Hub](https://github.com/patchy631/ai-engineering-hub)
- [Github - AGentic Patterns course ](https://github.com/neural-maze/agentic-patterns-course)

Template: 
- [Github - Full stack solution template for agentcore](https://github.com/awslabs/fullstack-solution-template-for-agentcore)

# “Agentic" solutions

## Red Hat Openshift (RHOAI, incl. Llamastack)

- [Github - agentic-claim-demo (example)](https://github.com/mouachan/agentic-claim-demo/tree/main)

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

# Cheat Sheet - Cloud Agent Creation

## AWS Bedrock AgentCore (with Strands)

### Option A: Quick Deployment with SDK

#### 1. Installation

```bash
pip install bedrock-agentcore
pip install strands-agents
```

#### 2. Minimal agent code

```python
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
agent = Agent()

@app.entrypoint
def invoke(payload):
    user_message = payload.get("prompt", "Hello")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()
```

#### 3. Local testing
```bash
python my_agent.py

# Test the endpoint
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello world!"}'
```

#### 4. Deployment with Starter Toolkit
```bash
# Installation
pip install bedrock-agentcore-starter-toolkit

# Configuration
agentcore configure --entrypoint agent_example.py

# Deployment
agentcore launch

# Test
agentcore invoke '{"prompt": "Hello"}'
```

### Option B: Custom Deployment with FastAPI

#### 1. Project structure
```
my-custom-agent/
├── agent.py              # FastAPI application
├── Dockerfile            # ARM64 container
├── pyproject.toml
└── uv.lock
```

#### 2. FastAPI code (agent.py)
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from strands import Agent

app = FastAPI()
strands_agent = Agent()

class InvocationRequest(BaseModel):
    input: dict

@app.post("/invocations")
async def invoke_agent(request: InvocationRequest):
    user_message = request.input.get("prompt", "")
    result = strands_agent(user_message)
    return {"output": {"message": result.message}}

@app.get("/ping")
async def ping():
    return {"status": "healthy"}
```

#### 3. ARM64 Dockerfile
```dockerfile
FROM --platform=linux/arm64 ghcr.io/astral-sh/uv:python3.11-bookworm-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache
COPY agent.py ./
EXPOSE 8080
CMD ["uv", "run", "uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8080"]
```

#### 4. Build and Deploy
```bash
# Build ARM64
docker buildx build --platform linux/arm64 -t my-agent:arm64 --load .

# Local test
docker run --platform linux/arm64 -p 8080:8080 my-agent:arm64

# Push to ECR
aws ecr get-login-password --region us-west-2 | \
  docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com

docker tag my-agent:arm64 ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest
docker push ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest
```

#### 5. Create Agent Runtime
```python
import boto3

client = boto3.client('bedrock-agentcore-control')
response = client.create_agent_runtime(
    agentRuntimeName='my-strands-agent',
    agentRuntimeArtifact={
        'containerConfiguration': {
            'containerUri': 'ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest'
        }
    },
    networkConfiguration={"networkMode": "PUBLIC"},
    roleArn='arn:aws:iam::ACCOUNT_ID:role/AgentRuntimeRole'
)
```

#### 6. Invoke the agent
```python
import boto3
import json

client = boto3.client('bedrock-agentcore')
payload = json.dumps({"input": {"prompt": "Hello"}})

response = client.invoke_agent_runtime(
    agentRuntimeArn='arn:aws:bedrock-agentcore:us-west-2:ACCOUNT_ID:runtime/agent-name',
    runtimeSessionId='session-id-minimum-33-chars-long',
    payload=payload
)
```

### AgentCore Observability

#### Enable CloudWatch Transaction Search

```bash
# Via CloudWatch console:
# Application Signals > Transaction search > Enable Transaction Search
```

#### Add ADOT to the agent

```bash
# requirements.txt
aws-opentelemetry-distro>=0.10.1
boto3

# Launch with auto-instrumentation
opentelemetry-instrument python my_agent.py

# In Dockerfile
CMD ["opentelemetry-instrument", "uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8080"]
```

---

## Google ADK (Agent Development Kit)

### Installation

```bash
pip install google-adk
```

### Create an agent project

```bash
# Create a new project
adk create my_agent

# Created structure:
# my_agent/
#   agent.py      # main code
#   .env          # API keys
#   __init__.py
```

### Basic agent code

```python
from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells time.",
    tools=[get_current_time],
)
```

### Configuration

```bash
# .env file
echo 'GOOGLE_API_KEY="YOUR_API_KEY"' > .env

# Or for Vertex AI
echo 'GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"' > .env
```

### Run the agent

#### CLI Interface

```bash
adk run my_agent
```

#### Web Interface (development only)

```bash
# From the parent directory of my_agent/
adk web --port 8000

# Access http://localhost:8000
```

### Deploy to Agent Engine

#### 1. Create deployment file (deploy.yaml)

```yaml
apiVersion: google.adk/v1
kind: Deployment
metadata:
  name: my-agent
spec:
  project: YOUR_PROJECT_ID
  location: us-central1
  agent: my_agent
```

#### 2. Deploy

```bash
# Deploy the agent
adk deploy --config deploy.yaml

# Via gcloud (alternative)
gcloud agent-engine agents deploy \
  --project=PROJECT_ID \
  --location=us-central1 \
  --agent-path=my_agent/agent.py
```

#### 3. Test deployed agent

```bash
# Test via ADK
adk test --endpoint https://YOUR_AGENT_URL

# Test via curl
curl -X POST https://YOUR_AGENT_URL/invoke \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  -d '{"query": "What time is it in Paris?"}'
```

### Multi-agent with ADK

```python
from google.adk.agents.llm_agent import Agent

# Specialized weather agent
weather_agent = Agent(
    model='gemini-3-flash-preview',
    name='weather_agent',
    tools=[get_weather],
)

# Coordinator agent
root_agent = Agent(
    model='gemini-3-flash-preview',
    name='coordinator',
    tools=[weather_agent],  # Uses the agent as a tool
)
```

### Google Cloud tools for ADK

```python
from google.adk.tools.google_cloud import BigQueryTool, VertexAISearchTool

# BigQuery
bq_tool = BigQueryTool(project_id="PROJECT_ID")

# Vertex AI Search
search_tool = VertexAISearchTool(
    project_id="PROJECT_ID",
    data_store_id="DATA_STORE_ID"
)

agent = Agent(
    model='gemini-3-flash-preview',
    tools=[bq_tool, search_tool],
)
```

---

## Quick Comparison

| Feature | AWS Bedrock AgentCore | Google ADK |
|---------|----------------------|------------|
| **Framework** | Strands Agents | ADK (Agent Development Kit) |
| **Installation** | `pip install bedrock-agentcore strands-agents` | `pip install google-adk` |
| **CLI Command** | `agentcore` | `adk` |
| **Supported Models** | Claude, Titan, etc. (via Bedrock) | Gemini (Vertex AI or API) |
| **Deployment** | ECR + Agent Runtime (ARM64) | Agent Engine (GCP) |
| **Required Port** | 8080 | Configurable |
| **Required Endpoints** | `/invocations` (POST), `/ping` (GET) | Flexible |
| **Architecture** | ARM64 container mandatory | Flexible |
| **Observability** | CloudWatch + ADOT | Cloud Trace + Cloud Logging |
| **Dev Interface** | Starter Toolkit | `adk web` |

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
