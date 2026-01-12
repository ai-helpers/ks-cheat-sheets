# Evaluations

## Evaluation kit

- [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/main): Language Model Evaluation Harness
  - [Tasks](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/README.md)
  - [Leaderboard](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/leaderboard/README.md)
- [VLMEvalKit](https://github.com/open-compass/VLMEvalKit)
- 


## References

- [Arxiv - Evaluate Agent with Agent](https://arxiv.org/pdf/2410.10934)
- [GitHub - Eval-Assist (IBM) - LLM as a Judge](https://github.com/IBM/eval-assist)
- [BLEU - ROUGE score](https://clementbm.github.io/theory/2021/12/23/rouge-bleu-scores.html)
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
- [Arxiv - Generating with Confidence: Uncertainty Quantification for Black-box Large Language Models](https://arxiv.org/pdf/2305.19187): How to Measure LLM Uncertainty and Why It Matters?
  - Researchers from the University of Illinois propose a three-step method:
    1. Generate 10 or more responses to the same question.
    2. Compute a similarity matrix between the responses.
    3. Derive an uncertainty score based on response diversity and inconsistency.
  - Two key criteria validate the approach:
    - Error prediction: Uncertainty should correlate with incorrect answers (evaluated via AUC-ROC analysis).
    - Error rejection: Filtering uncertain responses should improve accuracy (measured via rejection curve analysis).
  - Findings?
    - The worst approach is asking the LLM to estimate its own uncertainty.
    - The best method combines: NLI-based implication scores for the similarity matrix. + Spectral clustering of responses to compute the final uncertainty score.
  - Challenges and Limitations:
    - High cost: Each score requires 10+ LLM calls.
    - Requires non-zero temperature, making it inapplicable to deterministic responses.
    - Generic context: NLI models used are general-purpose and may not fit business-specific cases.
    - Lack of interpretability: The uncertainty scores (e.g., 0.4 to 10) lack clear business or probabilistic meaning.
    - Short responses work best: For long responses, contradictions get diluted, biasing NLI models trained on short sentences.
- [Practical Guide - LLM as a Judge](https://media.licdn.com/dms/document/media/v2/D561FAQGDS007DinjBw/feedshare-document-pdf-analyzed/feedshare-document-pdf-analyzed/0/1733838335869?e=1738195200&v=beta&t=0x3wvxWPFBxOkAm2HuNk13grh7CH5fXeo1AVAhB0f4w)
- [Github - lmms eval](https://github.com/EvolvingLMMs-Lab/lmms-eval): evaluation module from microsoft
- [Arxiv - Agent as a Judge: Evaluate Agents with Agents](https://arxiv.org/pdf/2410.10934)
- [How to implement LLM as a Judge to test AI Agents?](https://www.giskard.ai/knowledge/how-to-implement-llm-as-a-judge-to-test-ai-agents-part-1?utm_content=buffer3aded&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer)
- [Github - deepeval](https://github.com/confident-ai/deepeval)
- [GoogleBlog - DeepMind/Giskard evaluation](https://opensource.googleblog.com/2025/05/announcing-lmeval-an-open-ource-framework-cross-model-evaluation.html?utm_content=bufferbbe58&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer)
