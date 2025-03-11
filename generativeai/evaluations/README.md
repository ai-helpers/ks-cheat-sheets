# References

- [Arxiv - Evaluate Agent with Agent](https://arxiv.org/pdf/2410.10934)
- [Giskard - LLM as a judge](https://www.giskard.ai/knowledge/how-to-implement-llm-as-a-judge-to-test-ai-agents-part-1?utm_content=buffer3aded&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer)
- [Arxiv - Lessons from red teaming 100 Generative AI Products](https://arxiv.org/abs/2501.07238)
  - [Lnkd Post](https://www.linkedin.com/posts/gregoire-martinon_comment-assurer-la-s%C3%A9curit%C3%A9-des-syst%C3%A8mes-activity-7297155346706427904-dRn7?utm_source=share&utm_medium=member_desktop&rcm=ACoAABY4zkYBTs23buQ5AEQ-XagrOSQPiyJTUNs)
- [AWS Blog - RAG evaluation with LLM as a judge](https://aws.amazon.com/fr/blogs/aws/new-rag-evaluation-and-llm-as-a-judge-capabilities-in-amazon-bedrock/)
- [Github - RAGAS](https://github.com/explodinggradients/ragas)
- [DeepLearningAI - Safe and reliable AI via guardrails](https://learn.deeplearning.ai/courses/safe-and-reliable-ai-via-guardrails/lesson/3/what-are-guardrails)
- [Linkedin - Evaluation](https://www.linkedin.com/posts/techsachinkumar_evaluating-and-aligning-code-generation-llms-activity-7271856819545772033-bVc9/?utm_source=share&utm_medium=member_ios)
- [Keynote - Evaluating LLM Models for Production Systems: Methods and Practices](https://media.licdn.com/dms/document/media/v2/D561FAQF1A-DYl_O1kg/feedshare-document-pdf-analyzed/B56ZQ6Pet6GoAc-/0/1736143936684?e=1738195200&v=beta&t=kO2wNqbtAgPT2jvHrvunLTt_n4jSNQowaMKaiGnLcVo)
  - [Wide variety of tasks is a typical for use patterns of LLMs in every business](https://aclanthology.org/2022.emnlp-main.340.pdf)
  - [LLM evaluation]()
    - [MEASURING MASSIVE MULTITASK LANGUAGE UNDERSTANDING](https://arxiv.org/pdf/2009.03300)
    - [PROXYQA: An Alternative Framework for Evaluating Long-Form Text Generation with Large Language Models](https://arxiv.org/pdf/2401.15042)
    - [TrustLLM](https://arxiv.org/pdf/2401.05561)
    - [TrustScore](https://arxiv.org/pdf/2402.12545)
    - [Reasoning tasks, requires specific evaluation (ex ConceptArc)](https://arxiv.org/abs/2311.09247)
    - [Multi turn tasks, requires a specific evaluation (ex LMRL Gym)](https://arxiv.org/abs/2311.18232)
    - [Instruction following](https://arxiv.org/pdf/2310.07641.pdf)
  - [Embedding vs LLM - Generative Representational Instruction Tuning](https://arxiv.org/pdf/2402.09906)
    - [LLM Embedding evaluation - MTEB (Massive Text Embedding Benchmark)](https://arxiv.org/pdf/2210.07316), [Huggingface leaderboard](https://huggingface.co/spaces/mteb/leaderboard)
    - In Context Learning (ICL) evaluation: [HellaSwag](https://rowanzellers.com/hellaswag/), [OpenICL article](https://arxiv.org/pdf/2303.02913)
  - [LLM as a judge](https://arxiv.org/pdf/2306.05685): MT-bench & Chatbot Arena
  - RAG Evaluation:
    - [RAG Evaluation - RAGAs](https://arxiv.org/abs/2309.15217), [Github - Python module](https://docs.ragas.io/en/stable/)
    - [RAG Evaluation - ARES](https://arxiv.org/pdf/2311.09476), [Github - python module](https://github.com/stanford-futuredata/ARES)
    - [RAG Evaluation - HumanEval](https://arxiv.org/pdf/2107.03374), [Github - python code](https://github.com/openai/human-eval)
  - [Hallucination Evaluation - HaluEval](https://aclanthology.org/2023.emnlp-main.397.pdf)
  - Pairwise comparaison - Arenas: 
    - [Chatbot arena for generic user tasks](https://chat.lmsys.org/)
    - [Negotiation area for negotiation tasks](https://arxiv.org/pdf/2402.05863.pdf)
    - [A paper from Cohere about model ranking based on tournaments](https://arxiv.org/pdf/2311.17295.pdf)
  - Hardness Evaluation:
    - EleutherAI/lm-evaluation-harness, very powerful, for zero and few short tasks
    - OpenAI Evals
    - bigcode-project/bigcode-evaluation-harness, code evaluation tasks
    - MLFlow LLM Evaluate , integrated with ML Flow,
    - MosaicML Composer, icl tasks, superfast, scaling to multi gpu
    - RAGAs for LLM based evaluation https://docs.ragas.io/en/latest/
    - TruLens
- [Lnkd Gregoire M - Incertitude LLM](https://www.linkedin.com/posts/gregoire-martinon_comment-mesurer-lincertitude-des-llms-activity-7272150576518377472-EBlT/?utm_source=share&utm_medium=member_ios)
- [Practical Guide - LLM as a Judge](https://media.licdn.com/dms/document/media/v2/D561FAQGDS007DinjBw/feedshare-document-pdf-analyzed/feedshare-document-pdf-analyzed/0/1733838335869?e=1738195200&v=beta&t=0x3wvxWPFBxOkAm2HuNk13grh7CH5fXeo1AVAhB0f4w)
- [Github - lmms eval](https://github.com/EvolvingLMMs-Lab/lmms-eval): evaluation module from microsoft

# HELM
## What is HELM?

Sources: [GitHub](https://github.com/stanford-crfm/helm), [Arxiv oct 23 - Holistic Evaluation of Language Models](https://arxiv.org/pdf/2211.09110)

Published by Stanford's Center for Research on Foundation Models, HELM—the **Holistic Evaluation of Language Models**—is your compass through the maze of the complex LLM evaluation.

### Why it matters:

- ✸ **Comprehensive Evaluation:** HELM evaluates 30 prominent LLMs across 42 scenarios and 7 essential metrics, covering accuracy, fairness, robustness, and more.
- ✸ **Reveals Blind Spots:** It identifies blind spots and trade-offs across models and scenarios, ensuring you make informed choices.
- ✸ **Open Data:** All evaluation data is public—empowering the community to dive deeper and innovate further.

---

## What Makes HELM Distinguished?

### ✸ **Broad Coverage**  
HELM explores 16 core scenarios like question answering, summarization, sentiment analysis, and toxicity detection. Beyond that, it delves into 7 targeted evaluations (e.g., reasoning and bias).

### ✸ **Multi-Metric Evaluation**  
Accuracy isn’t the sole focus. HELM assesses LLMs using:  
- ☆ **Calibration:** How confident is the model in its predictions?  
- ☆ **Robustness:** Does it handle typos and dialects gracefully?  
- ☆ **Fairness:** Are all groups treated equitably?  

### ✸ **Standardization**  
HELM levels the playing field by benchmarking all 30 models—ranging from OpenAI’s GPT series to Meta’s OPT—under consistent conditions.

---

## The Highs and Lows of LLMs

- ✸ **Instruction-Tuning Rules:** Models like OpenAI’s *text-davinci-002* excel in accuracy and fairness due to their training, which prioritizes user-friendly instructions.  
- ✸ **Closed vs. Open Models:** Closed models generally outperform open ones, but open models like *BLOOM* are quickly narrowing the gap.  
- ✸ **Trade-offs Everywhere:** Improving one metric often sacrifices another. For example:

---

# Challenges and Future Directions

Despite HELM’s comprehensive approach, challenges remain:  
- ✸ **Dynamic Benchmarks:** Keeping benchmarks up-to-date as LLMs evolve.  
- ✸ **Scalability:** Ensuring evaluations remain feasible as the number of models grows.  
- ✸ **Ethical Considerations:** Addressing the broader impact of LLMs on society.
