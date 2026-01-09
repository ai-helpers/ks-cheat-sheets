# OCR/ VLM

## Table of Contents (ToC)

- [Table of Contents (ToC)](#table-of-contents-toc)
- [Open-Source OCR models and toolkit - Document AI](#open-source-ocr-models-and-toolkit---document-ai)
- [Others References](#others-references)

## Open-Source OCR models and toolkit - Document AI

- [EasyOCR](https://github.com/JaidedAI/EasyOCR): Ready-to-use OCR with 80+ supported languages and all popular writing scripts including: Latin, Chinese, Arabic, Devanagari, Cyrillic, etc.
- [Chandra](https://github.com/datalab-to/chandra): Chandra is a highly accurate OCR model that converts images and PDFs into structured HTML/Markdown/JSON while preserving layout information.
- [SmolDocling](https://github.com/docling-project/docling): An Ultra-Compact, Open-Source Vision-Language Model for Document Conversion
  - [Paper](https://arxiv.org/abs/2503.11576)
  - [GitHub](https://github.com/docling-project/docling)
  - [HF - Demo](https://huggingface.co/spaces/docling-project/SmolDocling-256M-Demo)
  - [Model Card](https://huggingface.co/docling-project/SmolDocling-256M-preview)
- [OlmOCR](https://github.com/allenai/olmocr): A toolkit for converting PDFs and other image-based document formats into clean, readable, plain text format.Support for equations, tables, handwriting, and complex formatting.Convert into text with a natural reading order, even in the presence of figures, multi-column layouts, and insets
  - [Paper](https://arxiv.org/pdf/2502.18443v1)
- [Dots.ocr](https://github.com/rednote-hilab/dots.ocr): A layout-aware OCR model designed for dense documents like scientific papers and multilingual forms and use LayoutLM-style models for structured understanding.
- [DeepSeek OCR](https://github.com/deepseek-ai/DeepSeek-VL): Vision-Language (VL) Model designed for general multimodal understanding capabilities, capable of processing logical diagrams, web pages, formula recognition, scientific literature, natural images, and embodied intelligence in complex scenarios.
- [Docling](https://github.com/docling-project/docling): A toolkit for document linguistics and OCR, tailored for historical and multilingual texts. Parsing of multiple document formats incl. PDF, DOCX, PPTX, XLSX, HTML, WAV, MP3, VTT, images (PNG, TIFF, JPEG, …). Support page layout, reading order, table structure, code, formulas, image classification.
- [TrOCR](https://arxiv.org/abs/2109.10282): Microsoft’s transformer-based OCR model for printed and handwritten text. Available on Hugging Face with multilingual support.
- [DocTR](https://github.com/mindee/doctr): A PyTorch-based OCR pipeline with detection and recognition modules for invoices, forms, and structured documents.
- [PaddleOCR–](https://huggingface.co/PaddlePaddle/PaddleOCR-VL) Lightweight and multilingual, optimized for mobile and embedded systems. - Multilingual Document Parsing via a 0.9B VLM, Universal Scene Text Recognition, Intelligent Information Extraction
- [LayoutLMv3](https://arxiv.org/pdf/2204.08387): Combines text, layout, and visual features for structured document understanding for receipts, invoices, and forms
- [Nanonets-OCR2](https://github.com/NanoNets/Nanonets-OCR2): Image-to-markdown OCR model. It transforms documents into structured markdown with semantic tagging, LaTeX equation recognition, and intelligent content parsing, making it ideal for LLM-ready workflows and complex document understanding
- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL): Alibaba’s multimodal model with strong OCR and layout capabilities. Useful for mixed-content documents
- [LLaVA-1.6](https://lnkd.in/eHk_rknu): Vision-language assistant with OCR capabilities, enabling document Q&A and visual reasoning
- [Gemma-3 Vision](https://huggingface.co/google/gemma-3-27b-it): Google’s open multimodal model tuned for document tasks and layout-aware OCR
- [Mistral-OCR](https://github.com/mistralai): (deprecated) A fast, lightweight model optimized for printed and handwritten text.
  - [Mistral - Mistral OCR](https://mistral.ai/fr/news/mistral-ocr)
  - [Mistral doc](https://docs.mistral.ai/capabilities/document/)
- [Mistral Document AI](https://docs.mistral.ai/capabilities/document_ai)

## Metrics

- CER (Character Error Rate)
- WER (Word Error Rate)

## Benchmark

- [Github - OmniDocBench](https://github.com/opendatalab/OmniDocBench/tree/main)
- [Fox - Benchmark](https://github.com/ucaslcl/Fox/tree/main)

## Cookbooks

- [Mistral Document AI](https://docs.mistral.ai/capabilities/document_ai/basic_ocr)
  - [Mistral - Document AI (batch_ocr)](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/ocr/batch_ocr.ipynb)
  - [Mistral - Document AI (tool usage)](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/ocr/tool_usage.ipynb)

## Others References

- [LandingAI](https://landing.ai/)
- [Finetuning qwen3 vl](https://debuggercafe.com/fine-tuning-qwen3-vl/)
