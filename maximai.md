# Maxim AI Documentation

> Maxim AI is the GenAI evaluation and observability platform that helps teams build reliable AI applications. This documentation covers our platform features, APIs, SDKs, and comprehensive guides for AI development and testing.

Maxim AI provides:
- Observability and monitoring for AI applications
- Agent simulation and evaluation
- Comprehensive SDK support for Python and TypeScript
- Integration with leading Agent Development platforms and frameworks
- Enterprise-grade security

## Core Platform

- [Maxim AI - Home](https://getmaxim.ai): Maxim AI is an end-to-end evaluation and observability platform for AI agents.
- [Platform Overview](https://www.getmaxim.ai/docs/introduction/overview): An introduction to Maxim's platform for AI application development and observability.
- [Maxim Documentation Home](https://www.getmaxim.ai/docs): Overview of Maxim's platform and its features for AI application development.
- [Running Your First Eval](https://www.getmaxim.ai/docs/introduction/running-your-first-eval): Step-by-step guide to running your first evaluation on Maxim.
- [Setting Up Workspace](https://www.getmaxim.ai/docs/introduction/quickstart/setting-up-workspace): Quickstart guide for setting up a workspace in Maxim's platform.

## Products & Features

- [Maxim Bifrost](https://www.getmaxim.ai/bifrost): Bifrost is a high-performance LLM gateway that connects 1000+ models through a single API interface with extremely high throughput and is 40x faster than LiteLLM.
- [Bifrost: A Drop-in LLM Proxy](https://www.getmaxim.ai/blog/bifrost-a-drop-in-llm-proxy-40x-faster-than-litellm): Introducing Bifrost, a high-performance LLM gateway designed for scalability and speed.
- [Experimentation](https://www.getmaxim.ai/products/experimentation): Product page for Maxim AI's experimentation tools for prompts and agents.
- [Agent Simulation & Evaluation](https://www.getmaxim.ai/products/agent-simulation-evaluation): Simulate and evaluate AI agent interactions across scenarios and user personas.
- [Agent Observability](https://www.getmaxim.ai/products/agent-observability): Monitor and improve AI agent performance with real-time insights and observability tools.

## Observability & Tracing

- [Tracing Overview](https://getmaxim.ai/docs/observe/overview): Monitor AI applications in real-time with Maxim's enterprise-grade LLM observability platform.
- [Tracing Quickstart](https://getmaxim.ai/docs/observe/quickstart): Quickstart guide for setting up distributed tracing to monitor and debug GenAI applications.
- [Tracing Concepts](https://www.getmaxim.ai/docs/observe/concepts): Learn about Maxim's distributed tracing concepts for AI applications.
- [Tracing Dashboard](https://www.getmaxim.ai/docs/tracing/dashboard): Learn how to use the dashboard to filter and sort logs.
- [Platform Overview](https://www.getmaxim.ai/docs/observability/concepts): Overview of Maxim's tools for AI application development and observability.

### Tracing via SDK

- [Tracing via SDK - Traces](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/traces): Guide to setting up tracing for AI applications using Maxim SDK.
- [Tracing via SDK: Generations](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/generations): Log individual calls to LLMs using Maxim's SDK.
- [Tracing via SDK: Sessions](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/sessions): Learn how to group related traces into sessions for tracking user interactions.
- [Spans](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/spans): Organize and track requests across microservices within traces.
- [Tracing Tool Calls](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/tool-calls): Track external system calls triggered by LLM responses in agentic endpoints.
- [Tracing Retrieval](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/retrieval): Documentation on logging retrievals in AI applications using Maxim SDK.
- [Events](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/events): Track application milestones and state changes using event logging.
- [Errors - Tracing via SDK](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/errors): Learn how to track and log errors in AI application traces for improved performance and reliability.
- [Tags](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/tags): Guide to tagging traces for effective data grouping and filtering.
- [Tracing via SDK Metadata](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/metadata): Overview of Maxim's platform for AI application development and observability.
- [Tracing via SDK - Attachments](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/attachments): Learn how to attach files and URLs to traces and spans for richer observability in Maxim.
- [User Feedback](https://www.getmaxim.ai/docs/tracing/tracing-via-sdk/user-feedback): Documentation for tracking user feedback in application traces.

### Logging & Monitoring

- [Log Multi-Turn Interactions as Session](https://www.getmaxim.ai/docs/observe/how-to/log-your-application/log-multiturn-interactions-as-session): Learn how to group related traces into sessions for tracking user interactions.
- [Attachments](https://www.getmaxim.ai/docs/observe/how-to/log-your-application/add-attachments): Learn how to attach files and URLs to traces and spans for enhanced observability.
- [Export Logs and Evaluation Data](https://www.getmaxim.ai/docs/observe/how-to/log-your-application/export-logs): Learn how to export logs and evaluation data in Maxim.
- [Use Data Connectors](https://www.getmaxim.ai/docs/observe/how-to/log-your-application/use-data-connectors): Instructions for forwarding traces to observability platforms using Maxim.
- [Reporting](https://www.getmaxim.ai/docs/tracing/reporting): Learn how to set up reporting for logs and evaluation data in Maxim.
- [Export Logs and Evaluation Data](https://www.getmaxim.ai/docs/tracing/exports): Learn how to export logs and evaluation data in Maxim.

## Evaluation

### Offline Evaluation

- [Offline Evaluation Overview](https://www.getmaxim.ai/docs/evaluate/overview): Guide to evaluating AI application performance through prompt testing, workflow automation, and log monitoring.
- [Offline Evaluation Concepts](https://www.getmaxim.ai/docs/offline-evals/concepts): Learn about key concepts in offline evaluation for AI models, including prompts, workflows, and evaluators.

### Prompt Testing

- [Prompt Testing Quickstart](https://getmaxim.ai/docs/evaluate/quickstart/run-your-first-test-on-prompt): Step-by-step guide to testing prompts using datasets and evaluators.
- [Prompt Playground](https://www.getmaxim.ai/docs/evaluate/how-to/evaluate-prompts/experiment-in-prompt-playground): Learn how to use the Prompt Playground to experiment with and optimize prompts.
- [Create Prompt Versions - Maxim AI Docs](https://www.getmaxim.ai/docs/evaluate/how-to/evaluate-prompts/create-prompt-versions): Documentation on creating and comparing prompt versions for AI experimentation.
- [Organize Prompts with Folders and Tags](https://www.getmaxim.ai/docs/evaluate/how-to/evaluate-prompts/organize-prompts): Guidelines for organizing AI prompts using folders, tags, and versioning in Maxim.
- [Automate Prompt Evaluation via CI/CD](https://www.getmaxim.ai/docs/evaluate/how-to/evaluate-prompts/automate-via-ci-cd): Learn how to automate prompt evaluation workflows using CI/CD pipelines.
- [Human Annotation Pipeline - Maxim Docs](https://www.getmaxim.ai/docs/evaluate/how-to/evaluate-prompts/human-annotation-pipeline): Learn about integrating human annotation pipelines to improve AI quality.

### Agent & Workflow Testing

- [No-Code Agent Quickstart](https://getmaxim.ai/docs/evaluate/quickstart/run-your-first-test-on-prompt-chains): Guide to testing agentic workflows using Maxim's no-code builder.
- [Simulate and Evaluate Multi-Turn Conversations](https://getmaxim.ai/docs/evaluate/quickstart/simulate-and-evaluate-multi-turn-conversations): Evaluate AI chat interactions using conversation simulation workflows.
- [Test Your AI Outputs Using Application Endpoint](https://www.getmaxim.ai/docs/evaluate/how-to/evaluate-workflows-via-api-endpoint/test-your-ai-outputs-using-application-endpoint): Documentation on evaluating AI workflows via API endpoints using Maxim.
- [Simulate Multi-Turn Conversations](https://www.getmaxim.ai/docs/evaluate/how-to/evaluate-workflows-via-api-endpoint/simulate-multi-turn-conversations): Guide on simulating multi-turn conversations to test AI workflows.
- [Experiment with Prompt Chains](https://www.getmaxim.ai/docs/evaluate/how-to/evaluate-chains/experiment-with-prompt-chains): Guide on experimenting with advanced prompt chains for AI workflows.

### Dataset Evaluation

- [Dataset Evaluation](https://getmaxim.ai/docs/evaluate/how-to/evaluate-datasets): Guide on evaluating AI outputs against expected results using Maxim's dataset evaluation tools.
- [Scheduled Test Runs](https://www.getmaxim.ai/docs/evaluate/how-to/scheduled-test-runs): Learn how to schedule test runs for prompts, agents, and workflows.
- [Trigger Test Runs Using SDK](https://getmaxim.ai/docs/evaluate/how-to/trigger-test-runs-using-sdk): Guide to running prompt evaluation test runs using the Maxim SDK.

### Online Evaluation

- [Online Evaluation Overview](https://www.getmaxim.ai/docs/online-evals/overview): Overview of Maxim's online evaluation platform for monitoring AI quality in production.
- [Set Up Auto Evaluation on Logs](https://www.getmaxim.ai/docs/observe/how-to/evaluate-logs/auto-evaluation): A guide on configuring automatic evaluation of logs in Maxim AI for better LLM performance monitoring.
- [Set Up Auto Evaluation on Logs](https://www.getmaxim.ai/docs/observe/how-to/evaluate-logs/human-evaluation): Guide for setting up automatic evaluation of logs in Maxim's platform.
- [Node Level Evaluation](https://www.getmaxim.ai/docs/observe/how-to/evaluate-logs/node-level-evaluation): Guide to evaluating components of traces or logs for AI agent performance.
- [Node Level Evaluation](https://www.getmaxim.ai/docs/online-evals/via-sdk/node-level-evaluation): Guide to evaluating components of AI workflows using Maxim SDK.
- [Set Up Human Annotation on Logs](https://www.getmaxim.ai/docs/online-evals/via-ui/set-up-human-annotation-on-logs): Guide to setting up human evaluation for logs in Maxim.

## Library Components

- [Library Overview](https://www.getmaxim.ai/docs/library/overview): Overview of Maxim's library components for AI testing.
- [Library Concepts](https://www.getmaxim.ai/docs/library/concepts): Explore key concepts in AI evaluation, including evaluators, datasets, and tools for assessing model performance.

### Evaluators

- [Pre-built Evaluators](https://www.getmaxim.ai/docs/library/evaluators/pre-built-evaluators): Quickly get started with ready-made evaluators for common AI evaluation scenarios.
- [Using Pre-Built Evaluators](https://getmaxim.ai/docs/library/how-to/evaluators/use-pre-built-evaluators): Guide to using pre-built evaluators for AI evaluation scenarios in Maxim.
- [Custom Evaluators](https://getmaxim.ai/docs/library/how-to/evaluators/create-custom-ai-evaluator): Guide to creating and configuring custom evaluators for AI evaluation needs.
- [Custom Evaluators](https://www.getmaxim.ai/docs/library/how-to/evaluators/create-api-evaluators): Guide to creating and configuring custom evaluators for specific evaluation needs.
- [Custom Evaluators - Human Evaluators](https://getmaxim.ai/docs/library/how-to/evaluators/create-human-evaluators): Documentation on creating and configuring human evaluators for AI output quality control.
- [Third Party Evaluators](https://www.getmaxim.ai/docs/library/evaluators/third-party-evaluators): Comprehensive guide to third-party evaluation metrics supported by Maxim.

### Datasets

- [Import or Create Datasets](https://www.getmaxim.ai/docs/library/datasets/import-or-create-datasets): Guide on importing or creating datasets for AI model training, testing, and evaluation.
- [Import or Create Datasets](https://www.getmaxim.ai/docs/library/how-to/datasets/use-dataset-templates): Guide to importing or creating datasets for AI model evaluation.
- [Manage Datasets](https://www.getmaxim.ai/docs/library/datasets/manage-datasets): Learn how to manage datasets effectively using splits and variable columns.
- [Curate Datasets](https://www.getmaxim.ai/docs/library/datasets/curate-datasets): Guide on curating datasets from production logs and human annotations.
- [Curate Golden Dataset for Human Annotation](https://getmaxim.ai/docs/library/how-to/datasets/curate-golden-dataset-for-human-annotation): Learn how to curate datasets from production logs and human annotations.
- [Curate Datasets from Production Logs and Annotations](https://getmaxim.ai/docs/library/how-to/datasets/curate-data-from-production): Guide on curating datasets from production logs and human annotations in Maxim.
- [Use Local Datasets](https://www.getmaxim.ai/docs/library/datasets/use-local-datasets): Guide to adding new entries to datasets using the Maxim SDK.
- [Add New Entries to Datasets Using SDK](https://www.getmaxim.ai/docs/library/how-to/datasets/add-new-entries-using-sdk): Guide to adding entries to datasets via Maxim SDK.

### Context Sources & Prompt Tools

- [Context Sources](https://getmaxim.ai/docs/library/how-to/context-sources/ingest-files-as-a-context-source): Learn how to create, use, and evaluate context sources for your AI applications.
- [Context Sources](https://getmaxim.ai/docs/library/how-to/context-sources/bring-your-rag-via-an-api-endpoint): Learn how to create, use, and evaluate context sources for your AI applications.
- [Context Sources](https://www.getmaxim.ai/docs/library/context-sources): Learn how to create, use, and evaluate context sources for AI applications.
- [Prompt Tools](https://www.getmaxim.ai/docs/library/prompt-tools): Documentation for creating and using different types of prompt tools in Maxim.
- [Creating Prompt Partials](https://www.getmaxim.ai/docs/library/prompt-partials): Learn how to create and use prompt partials in Maxim.

## SDK Documentation

### SDK Overview

- [Maxim SDK Overview](https://www.getmaxim.ai/docs/sdk/overview): Introduction to Maxim SDK for AI application development.
- [Python SDK Overview](https://www.getmaxim.ai/docs/sdk/python/overview): Introduction to Maxim's Python SDK and its features.
- [Maxim SDK for TypeScript](https://www.getmaxim.ai/docs/sdk/typescript/reference/overview): JS/TS SDK for enabling Maxim observability and evaluation.

### Python SDK

#### Integrations

- [OpenAI SDK One-Line Integration](https://www.getmaxim.ai/docs/sdk/python/integrations/openai/one-line-integration): Guide to integrating Maxim observability with OpenAI SDK in one line of code.
- [OpenAI Agents SDK](https://www.getmaxim.ai/docs/sdk/python/integrations/openai/agents-sdk): Guide for integrating Maxim with the OpenAI Agents SDK.
- [OpenAI Agents SDK Integration](https://getmaxim.ai/docs/observe/integrations/openai-agents-sdk): Instructions for integrating Maxim with OpenAI Agents SDK for observability and real-time evaluation.
- [Anthropic SDK](https://www.getmaxim.ai/docs/sdk/python/integrations/anthropic/anthropic): Guide to integrating Maxim observability with the Anthropic SDK.
- [Google Gemini Integration](https://www.getmaxim.ai/docs/sdk/python/integrations/gemini/gemini): Learn how to integrate Maxim observability with the Google Gemini SDK in one line of code.
- [Mistral SDK](https://www.getmaxim.ai/docs/sdk/python/integrations/mistral/mistral): Learn how to integrate Maxim observability with the Mistral SDK.
- [LangChain Integration](https://www.getmaxim.ai/docs/sdk/python/integrations/langchain/langchain): Guide on integrating LangChain with Maxim observability for LLM applications.
- [Tavily Search & LangGraph Agent with Maxim Observability](https://www.getmaxim.ai/docs/sdk/python/integrations/langgraph/langgraph): Tutorial on integrating Tavily Search API with LangGraph and Maxim Observability.
- [Maxim Integration for CrewAI](https://www.getmaxim.ai/docs/sdk/python/integrations/crewai/crewai): Comprehensive agent monitoring, evaluation, and observability for CrewAI applications.
- [Maxim Integration for Agno](https://www.getmaxim.ai/docs/sdk/python/integrations/agno/agno): Guide to integrating Maxim with Agno agents for observability.
- [LiteLLM SDK Integration](https://www.getmaxim.ai/docs/sdk/python/integrations/litellm/litellm-sdk): Learn how to integrate Maxim SDK with LiteLLM for tracing and monitoring.
- [LiteLLM Proxy One-Line Integration](https://www.getmaxim.ai/docs/sdk/python/integrations/litellm/litellm-proxy): Learn how to integrate Maxim with LiteLLM Proxy in one line of configuration.
- [LiveKit SDK Integration](https://www.getmaxim.ai/docs/sdk/python/integrations/livekit/livekit): Guide to integrating Maxim observability with LiveKit for real-time voice AI applications.

#### Python SDK Reference

- [Maxim Python SDK](https://www.getmaxim.ai/docs/sdk/python/references/maxim): Core functionality and reference for Maxim's Python SDK.
- [Trace Decorator Reference](https://www.getmaxim.ai/docs/sdk/python/references/decorators/trace): Documentation for the Trace decorator in the Maxim Python SDK.
- [Python SDK: decorators.Retrieval](https://www.getmaxim.ai/docs/sdk/python/references/decorators/retrieval): Reference for retrieval decorators in Maxim AI's Python SDK.
- [Python SDK Reference: decorators.Span](https://www.getmaxim.ai/docs/sdk/python/references/decorators/span): Documentation for the Span decorator in Maxim's Python SDK.
- [decorators.Generation](https://www.getmaxim.ai/docs/sdk/python/references/decorators/generation): Generation utilities for decorators for automatic logging and instrumentation.
- [Decorators ToolCall](https://www.getmaxim.ai/docs/sdk/python/references/decorators/tool_call): Utilities for automatic logging and instrumentation of functions.
- [TestRunBuilder](https://www.getmaxim.ai/docs/sdk/python/references/test_runs/test_run_builder): Utilities for building and managing test runs in Maxim.
- [Upgrading to v3](https://www.getmaxim.ai/docs/sdk/python/upgrading-to-v3): Details on changes introduced in Maxim SDK v3 for Python.

### TypeScript SDK

#### Integrations

- [LangChain Integration](https://www.getmaxim.ai/docs/sdk/typescript/integrations/langchain/langchain): Comprehensive guide to integrating Maxim observability with LangChain applications in TypeScript/JavaScript.
- [LangGraph Integration](https://www.getmaxim.ai/docs/sdk/typescript/integrations/langgraph/langgraph): Guide to integrating Maxim observability with LangGraph applications in TypeScript/JavaScript.
- [Vercel Integration](https://www.getmaxim.ai/docs/sdk/typescript/integrations/vercel/vercel): Guide on integrating Maxim observability with the Vercel AI SDK.

#### TypeScript SDK Reference

- [Maxim SDK Core Class](https://www.getmaxim.ai/docs/sdk/typescript/reference/core/classes/Maxim): Primary entry point for interacting with the Maxim observability platform.
- [MaximLogger](https://www.getmaxim.ai/docs/sdk/typescript/reference/core/classes/MaximLogger): Comprehensive observability class for logging and monitoring AI applications in Maxim SDK.
- [TypeScript SDK Core Overview - Maxim Docs](https://www.getmaxim.ai/docs/sdk/typescript/reference/core/overview): Comprehensive reference for the TypeScript SDK core features.
- [Trace Class in TypeScript SDK](https://www.getmaxim.ai/docs/sdk/typescript/reference/core/classes/Trace): Detailed documentation of the Trace class for capturing execution flows.
- [Generation Class Reference](https://www.getmaxim.ai/docs/sdk/typescript/reference/core/classes/Generation): Technical documentation for the Generation class in Maxim's TypeScript SDK.
- [Retrieval Class](https://www.getmaxim.ai/docs/sdk/typescript/reference/core/classes/Retrieval): Technical documentation for the Retrieval class in Maxim's TypeScript SDK.
- [ToolCall Class Reference](https://www.getmaxim.ai/docs/sdk/typescript/reference/core/classes/ToolCall): Technical documentation for the ToolCall class in Maxim's TypeScript SDK.

## Alerts & Notifications

- [Set Up Alerts and Notifications](https://www.getmaxim.ai/docs/online-evals/set-up-alerts-and-notifications): Learn how to configure notification channels and set up alerts for monitoring AI application performance and quality metrics.
- [Set Up Alerts for Performance Metrics](https://www.getmaxim.ai/docs/observe/how-to/set-up-alerts/set-up-alerts-for-performance-metrics): Guide to configuring alerts and notifications for monitoring AI application performance.
- [Set Up Alerts for Quality Metrics](https://www.getmaxim.ai/docs/observe/how-to/set-up-alerts/set-up-alerts-for-quality-metrics): Learn how to configure alerts to monitor AI application quality metrics.
- [Set Up Alerts and Notifications](https://www.getmaxim.ai/docs/observe/how-to/set-up-alerts/create-a-slack-integration): Guide to configuring Slack and PagerDuty integrations for AI application alerts.
- [Create a Slack Integration](https://www.getmaxim.ai/docs/integrations/create-a-slack-integration): Step-by-step guide to integrating Slack with Maxim for performance notifications.
- [Create a PagerDuty Integration](https://www.getmaxim.ai/docs/integrations/create-a-pagerduty-integration): Steps to integrate PagerDuty for AI application alerts.

## Dashboards & Analytics

- [Custom Logs Dashboards](https://www.getmaxim.ai/docs/dashboards/custom-logs-dashboard): Create custom dashboards to analyze and track AI application logs using configurable metrics, filters, and charts.
- [Test Runs Comparison Dashboard](https://www.getmaxim.ai/docs/dashboards/test-runs-comparison-dashboard): Guide on creating and understanding test runs comparison dashboards.
- [Test Runs Comparison Dashboard](https://www.getmaxim.ai/docs/analyze/overview): Guide to creating and analyzing comparison dashboards for test runs in Maxim.
- [Comparison Reports](https://www.getmaxim.ai/docs/analyze/how-to/comparison-reports): Guide on creating and analyzing test run comparison reports.
- [Customized Reports](https://www.getmaxim.ai/docs/evaluate/how-to/optimize-evaluation-processes/customize-share-reports): Guide on customizing AI evaluation reports for better insights and decision-making.
- [Customized Reports Documentation](https://www.getmaxim.ai/docs/offline-evals/via-ui/advanced/customized-reports): Guide to customizing evaluation reports in Maxim's offline evaluation UI.

## Guides & Tutorials

### Getting Started

- [Create a Customer Support Email Agent](https://www.getmaxim.ai/docs/offline-evals/guides/create-customer-support-agent): Step-by-step guide to building a customer support email agent using Maxim AI.
- [Guide: Create a Product Description Generator](https://www.getmaxim.ai/docs/offline-evals/guides/create-product-description-generator): Step-by-step guide to building an AI workflow for generating product descriptions.

### Industry-Specific Guides

- [Evaluating the Quality of Clinical Documentation Using Maxim AI](https://www.getmaxim.ai/blog/create-reliable-clinical-notes-using-maxim): A guide to creating and evaluating reliable clinical notes using Maxim AI's tools.
- [Evaluating the Quality of Healthcare Assistants using Maxim AI](https://www.getmaxim.ai/blog/evaluating-quality-of-healthcare-assistants-using-maxim): Guide to evaluating AI healthcare assistants for reliability and performance using Maxim.
- [Evaluating AI Healthcare Assistants](https://www.getmaxim.ai/docs/offline-evals/guides/evaluating-the-quality-of-healthcare-assistants-using-maxim-ai): Guide to evaluating the quality and reliability of AI healthcare assistants using Maxim.
- [Evaluating the Quality of AI HR Assistants](https://www.getmaxim.ai/docs/offline-evals/guides/evaluating-the-quality-of-ai-hr-assistants): Guide to evaluating AI HR assistants using Maxim.
- [Evaluating the Quality of AI HR Assistants](https://www.getmaxim.ai/blog/evaluating-the-quality-of-ai-hr-assistants): Guide on building and evaluating AI-powered HR assistants using Maxim.
- [Evaluating the Quality of NL-to-SQL Workflows](https://www.getmaxim.ai/blog/evaluating-the-quality-of-nl-to-sql-workflows): Explores methods to improve NL-to-SQL workflows for better query accuracy and user trust.

### Integration Tutorials

- [Build a RAG Application Using MongoDB and Maxim AI](https://www.getmaxim.ai/blog/build-rag-app-mongodb-maxim): Step-by-step guide to building a retrieval-augmented generation (RAG) application using MongoDB and Maxim AI.
- [Building and Evaluating a Reddit Insights Agent with Gumloop and Maxim AI](https://www.getmaxim.ai/blog/building-and-evaluating-a-reddit-insights-agent-with-gumloop-and-maxim-ai-2): A detailed guide on building and evaluating a Reddit insights agent using Gumloop and Maxim AI.
- [Build an AI Interview Voice Agent with LiveKit & Maxim](https://www.getmaxim.ai/blog/build-an-ai-interview-voice-agent-with-livekit-maxim): A tutorial on building a real-time AI interview voice agent using LiveKit and Maxim.
- [Building a Math Trivia Game Agent with Mistral AI and Maxim](https://www.getmaxim.ai/blog/building-a-math-trivia-game-agent-with-mistral-ai-and-maxim): A tutorial on creating a Math Trivia Game using Mistral AI and Maxim for observability.
- [ðŸŒ¤ï¸ Building a Gemini-Powered Conversational Weather Agent with Maxim Logging](https://www.getmaxim.ai/blog/building-a-gemini-powered-conversational-weather-agent-with-maxim-logging): A tutorial on building a conversational weather agent using Gemini AI and Maxim logging.
- [Making a Financial Conversation Agent using Agno & Maxim](https://www.getmaxim.ai/blog/making-a-financial-conversation-agent-using-agno-maxim): Tutorial on building a financial conversational agent using Agno and Maxim AI.
- [Building the Agentic Debugging Game: Anthropic Observability Using Maxim](https://www.getmaxim.ai/blog/building-the-agentic-debugging-game-anthropic-observability-using-maxim): Tutorial on building an interactive debugging game with Anthropic and Maxim.
- [Built an Event Discovery AI Agent using No-Code under 15 mins](https://www.getmaxim.ai/blog/built-an-event-discovery-ai-agent-using-no-code-under-15-mins): Blog post on creating an event discovery AI agent using n8n and Maxim.

## Company & Community

- [About Us](https://www.getmaxim.ai/about-us): Overview of Maxim's mission, team, and vision for AI development.
- [Careers](https://www.getmaxim.ai/careers): Join Maxim AI to shape the future of AI development.
- [Schedule a Demo - Maxim](https://www.getmaxim.ai/demo): Schedule a demo to see Maxim in action and save development time.
- [Contact Us](https://www.getmaxim.ai/contact): Get in touch with Maxim AI for queries, feedback, or support.
- [Maxim AI Pricing Plans](https://www.getmaxim.ai/pricing): Explore Maxim AI's pricing plans for developers, professionals, businesses, and enterprises.
- [Maxim Bifrost - OSS Friends](https://www.getmaxim.ai/bifrost/oss-friends): Amazing open source projects that share our mission of making AI development more accessible and efficient.
- [OSS Friends](https://www.getmaxim.ai/bifrost/oss-friends): A showcase of open-source projects aligned with Maxim AI's mission.

## Blog & Updates

### Product Updates

- [Maxim AI June 2025 Updates](https://www.getmaxim.ai/blog/maxim-ai-june-2025-updates): Highlights new features, integrations, and updates in Maxim AI for June 2025.
- [âœ¨ Agentic mode, Scheduled runs, New evals, and more](https://www.getmaxim.ai/blog/maxim-ai-may-2025-updates): Highlights of Maxim AI's May 2025 updates, including new features and model support.
- [âœ¨ MCP client, Live dashboard, Vertex AI evals, and more](https://www.getmaxim.ai/blog/maxim-ai-april-2025-updates): A detailed overview of Maxim AI's April 2025 updates, including new features like MCP clients, live dashboards, and Vertex AI integration.
- [Maxim AI March 2025 Updates](https://www.getmaxim.ai/blog/maxim-ai-march-2025-updates): Highlights of new features, customer stories, and upcoming releases in Maxim AI.
- [Maxim AI February 2025 Update](https://www.getmaxim.ai/blog/maxim-february-2025-update): Overview of new features and updates in Maxim AI for February 2025.
- [Maxim AI January 2025 Updates](https://www.getmaxim.ai/blog/maxim-ai-january-2025-updates): Overview of new features and updates in Maxim AI for January 2025.
- [Maxim AI - Product Updates, December 2024](https://www.getmaxim.ai/blog/maxim-ai-december-2024-updates): Overview of new features and updates in Maxim AI for December 2024.
- [Maxim AI November 2024 Updates](https://www.getmaxim.ai/blog/maxim-ai-november-2024-updates): Overview of new features and updates in Maxim AI for November 2024.

### Weekly Updates

- [Better Dashboards, Smarter Workflows – Weekly Release Notes](https://www.getmaxim.ai/blog/better-dashboards-smarter-workflows-maxim-weekly-release-notes-june-9-13-2025): Overview of Maxim's weekly updates, including dashboard upgrades and SDK improvements.
- [Last Week at Maxim (Week 3 of May 2025)](https://www.getmaxim.ai/blog/last-week-at-maxim-week-3-of-may-2025): A roundup of updates shipped at Maxim during the third week of May 2025.
- [Last Week at Maxim AI (Week 2 of May 2025)](https://www.getmaxim.ai/blog/last-week-at-maxim-ai-week-2-of-may-2025): Weekly updates on new features, enhancements, and bug fixes at Maxim AI.
- [Last Week at Maxim: Week 1 of May](https://www.getmaxim.ai/blog/last-week-at-maxim-week-1-of-may): Weekly updates on new features and improvements at Maxim.
- [Last Week at Maxim (Weekly Updates)](https://www.getmaxim.ai/blog/last-week-at-maxim-weekly-update): Weekly updates on new features and improvements in Maxim's platform.

### Customer Stories

- [Scaling Enterprise Support: Atomicwork's Journey to Seamless AI Quality with Maxim](https://www.getmaxim.ai/blog/scaling-enterprise-support-atomicworks-journey-to-seamless-ai-quality-with-maxim): Case study on how Atomicwork uses Maxim AI to ensure reliable and scalable AI-powered enterprise support.
- [Mindtickle's Robust AI Productionizing Process powered by Maxim](https://www.getmaxim.ai/blog/mindtickle-ai-quality-evaluation-using-maxim): Explores how Mindtickle uses Maxim to enhance AI quality and streamline production processes.
- [Elevating Conversational Banking: Clinc's Path to AI Confidence with Maxim](https://www.getmaxim.ai/blog/elevating-conversational-banking-clincs-path-to-ai-confidence-with-maxim): Explore how Clinc uses Maxim to enhance conversational AI for the banking industry.
- [Building Trustworthy AI: Thoughtful's Journey with Maxim AI](https://www.getmaxim.ai/blog/building-smarter-ai-thoughtfuls-journey-with-maxim-ai): A blog detailing Thoughtful's integration of Maxim AI to enhance their AI companion, T.

### Technical Deep Dives

- [From Zero to OTel: Architecting a Stateless Tracing SDK for GenAI](https://www.getmaxim.ai/blog/from-zero-to-otel-architecting-a-stateless-tracing-sdk-for-genai-part-1): Explores the architecture of a stateless distributed tracing system compatible with OpenTelemetry for GenAI observability.
- [CoTools and the Future of LLM Tool Use for Complex Reasoning](https://www.getmaxim.ai/blog/chain-of-tools-llm-framework): Introduction to the Chain-of-Tools framework for enabling LLMs to interact with external tools.
- [Building Robust Evaluation Workflows for AI Agents](https://www.getmaxim.ai/blog/evaluation-workflows-for-ai-agents): Best practices for evaluating AI agents through structured workflows.
- [Agent-as-a-Judge: Evaluating Agentic Systems](https://www.getmaxim.ai/blog/agent-evaluation): Explores the Agent-as-a-Judge framework for evaluating agentic systems using AI.
- [Agent Evaluation: Metrics for Evaluating Agentic Workflows](https://www.getmaxim.ai/blog/ai-agent-evaluation-metrics): A blog post discussing metrics for evaluating AI agents in dynamic workflows.
- [Agent Evaluation: Understanding Agentic Systems and their Quality](https://www.getmaxim.ai/blog/ai-agent-quality-evaluation): An exploration of agentic AI systems, their architecture, applications, and the importance of quality evaluation.
- [A Survey of Agent Evaluation Frameworks: Benchmarking the Benchmarks](https://www.getmaxim.ai/blog/llm-agent-evaluation-framework-comparison): A comprehensive survey of frameworks for evaluating LLM-based agents.

### AI Research & Techniques

#### Prompting & Reasoning

- [Chain-of-Thought Prompting: Enhancing LLM Reasoning](https://www.getmaxim.ai/blog/chain-of-thought-prompting): A blog exploring the Chain-of-Thought prompting technique for LLMs.
- [Can We Trust What AI Models Say They're Thinking? A Deep Dive into Chain-of-Thought Faithfulness](https://www.getmaxim.ai/blog/can-we-trust-what-ai-models-say-theyre-thinking-a-deep-dive-into-chain-of-thought-faithfulness): Exploration of the faithfulness of AI models' Chain-of-Thought reasoning.
- [Skipping the Thinking: How Simple Prompts Can Outperform Complex Reasoning in AI](https://www.getmaxim.ai/blog/skipping-the-thinking-how-simple-prompts-can-outperform-complex-reasoning-in-ai): Explores the 'NoThinking' strategy for efficient AI reasoning.
- [Mastering the Art of Prompt Engineering: A Practical Guide for Better AI Outcomes](https://www.getmaxim.ai/blog/mastering-prompt-engineering): A comprehensive guide to crafting effective prompts for AI models.

#### RAG (Retrieval-Augmented Generation)

- [What is RAG? A Comprehensive Guide](https://www.getmaxim.ai/blog/rag-in-ai): An in-depth guide to retrieval-augmented generation (RAG) in AI.
- [Best Practices for Retrieval-Augmented Generation (RAG)](https://www.getmaxim.ai/blog/rag-best-practices): Comprehensive guide to optimizing RAG systems with advanced techniques.
- [Advanced RAG Techniques](https://www.getmaxim.ai/blog/advanced-rag-techniques): Exploration of Astute RAG for handling imperfect retrieval in LLMs.
- [The Role of Retrieval in Improving RAG Performance](https://www.getmaxim.ai/blog/rag-retrieval): Exploration of retrieval techniques to enhance Retrieval-Augmented Generation (RAG).
- [Improving RAG accuracy with reranking techniques](https://www.getmaxim.ai/blog/reranker-rag): Explores how reranking techniques can enhance Retrieval-Augmented Generation (RAG) accuracy.
- [Decoding the Generation Component: How RAG Creates Coherent Text](https://www.getmaxim.ai/blog/rag-generation-component): Explores techniques to enhance the generation component of Retrieval-Augmented Generation (RAG).
- [Evaluating RAG performance: Metrics and benchmarks](https://www.getmaxim.ai/blog/rag-evaluation-metrics): A detailed blog on evaluating Retrieval-Augmented Generation (RAG) systems using metrics and benchmarks.
- [Graph RAG](https://www.getmaxim.ai/blog/graph-rag): Exploration of Microsoft's Graph-based Retrieval-Augmented Generation (Graph RAG) approach for handling global queries and large datasets.
- [LongRAG](https://www.getmaxim.ai/blog/longrag-llm): An overview of LongRAG, a framework enhancing Retrieval-Augmented Generation with long-context models.
- [RAFT: Adapting Language Models to Domain-Specific RAG](https://www.getmaxim.ai/blog/raft-domain-rag): Introduces RAFT, a training method combining fine-tuning and RAG for domain-specific question answering.
- [Contextual Document Embeddings](https://www.getmaxim.ai/blog/contextual-document-embeddings): Exploration of methods to improve document embeddings for neural retrieval tasks.

#### Evaluation & Testing

- [RAGChecker](https://www.getmaxim.ai/blog/ragchecker-eval-tool): Exploration of the RAGChecker framework for evaluating Retrieval-Augmented Generation systems.
- [RAGEval: Scenario-specific RAG Evaluation Framework](https://www.getmaxim.ai/blog/rageval-rag-eval): Introduction to RAGEval, a framework for generating domain-specific RAG evaluation datasets.
- [LLM Hallucination Detection](https://www.getmaxim.ai/blog/llm-hallucination-detection): Exploration of fine-grained hallucination detection techniques for improving LLM accuracy.
- [KNOWHALU: Hallucination detection via multi-form knowledge-based factual checking](https://www.getmaxim.ai/blog/knowhalu-llm-fact-check): Explores KnowHalu, a novel approach to detecting hallucinations in LLM-generated text.
- [MiniCheck: Efficient Fact-Checking of LLMs on Grounding Documents](https://www.getmaxim.ai/blog/minicheck-llm-fact-check): Introduces MiniCheck, a cost-effective model for fact-checking LLM outputs with high accuracy.
- [Using a Jury of LLMs Instead of a Single Judge to Evaluate LLM Generations](https://www.getmaxim.ai/blog/llm-as-a-jury): Explores the use of a panel of smaller LLMs for unbiased and cost-effective evaluation of AI outputs.
- [Evaluating Data Contamination in LLMs](https://www.getmaxim.ai/blog/llm-data-quality): Analysis of data contamination in large language models and its impact on benchmarks.
- [Evaluating a Healthcare Use Case Using Vertex AI and Maxim AI - Part 1](https://www.getmaxim.ai/blog/evaluating-a-healthcare-use-case-using-vertex-ai-and-maxim-ai-part-1): Introduction to evaluating healthcare AI systems using Vertex AI and Maxim AI.

#### Model Capabilities & Limitations

- [Long-context LLMs vs RAG](https://www.getmaxim.ai/blog/llm-rag-compare): Comparison of long-context LLMs and Retrieval-Augmented Generation (RAG) models.
- [From Turn 1 to Turn 10: How LLMs Get Lost In Multi-Turn Conversations](https://www.getmaxim.ai/blog/from-turn-1-to-turn-10-how-llms-get-lost-in-multi-turn-conversations): Explores the challenges LLMs face in multi-turn conversations and proposes methods to mitigate performance degradation.
- [Do Language Models Know That They're Being Evaluated?](https://www.getmaxim.ai/blog/do-language-models-know-that-theyre-being-evaluated): Explores the phenomenon of evaluation awareness in language models and its implications.
- [Base vs. Aligned: Why Base LLMs Might be Better at Randomness and Creativity](https://www.getmaxim.ai/blog/base-vs-aligned-why-base-llms-might-be-better-at-randomness-and-creativity): Explores the tradeoffs between base and aligned LLMs in tasks requiring unpredictability and creativity.
- [Sure your LLM is smart, but does it really give a damn?](https://www.getmaxim.ai/blog/sure-your-llm-is-smart-but-does-it-really-give-a-damn): Exploration of goal-directedness in large language models and its impact on agentic applications.

#### Training & Optimization

- [Innovative Training of LLMs in Continuous Latent Spaces](https://www.getmaxim.ai/blog/llms-continuous-latent-spaces): Exploration of Coconut, a novel approach to LLM reasoning in continuous latent spaces.
- [SuperBPE: Rethinking Tokenization for Language Models](https://www.getmaxim.ai/blog/superbpe-rethinking-tokenization-for-language-models): Exploration of the SuperBPE tokenization strategy for language models.
- [Synthetic Data Generation Grounded in Real Data Sources](https://www.getmaxim.ai/blog/synthetic-data-generation): Exploration of the Source2Synth framework for generating high-quality synthetic data.
- [APIGen-MT: Structured Multi-Turn Data via Simulation](https://www.getmaxim.ai/blog/apigen-mt-structured-multi-turn-training-data-for-agents): Introduction to APIGen-MT for generating multi-turn training data for AI agents.
- [User Simulation in AI: From Rule-Based Models to LLM-Powered Realism](https://www.getmaxim.ai/blog/user-simulation-in-ai-from-rule-based-models-to-llm-powered-realism): Explores the evolution of user simulation in AI, from rule-based models to LLM-powered realism.
- [DSPy Framework](https://www.getmaxim.ai/blog/dspy-framework): An overview of DSPy, a declarative framework for optimizing LLM pipelines.

#### AI Safety & Ethics

- [Can Your AI Explain Why It's Moral?](https://www.getmaxim.ai/blog/can-your-ai-explain-why-its-moral): Examines the ethical reasoning capabilities of AI models using a structured audit framework.
- [Making Language Models Unbiased, One Vector At a Time](https://www.getmaxim.ai/blog/making-language-models-unbiased-one-vector-at-a-time): Explores methods to reduce bias in large language models using interpretability-based techniques.
- [Your Horrible Code is Making LLMs Evil: Exploring Emergent Misalignment](https://www.getmaxim.ai/blog/your-horrible-code-is-making-llms-evil-exploring-emergent-misalignment): Analysis of emergent misalignment in LLMs caused by insecure code fine-tuning.
- [Understanding Jailbreaking and Prompt-Based Injections](https://www.getmaxim.ai/blog/jailbreaking-prompt-injection): Explores the risks and mechanisms of jailbreaking and prompt injection attacks in large language models.
- [Red Teaming with Auto-Generated Rewards and Multi-Step RL](https://www.getmaxim.ai/blog/ai-red-teaming): Exploring automated red-teaming frameworks for generating diverse and effective adversarial attacks.
- [Ensuring responsible AI: An overview of DeepMind's FACTS framework](https://www.getmaxim.ai/blog/deepmind-facts-framework-responsible-ai): Highlights DeepMind's FACTS framework for evaluating the factual accuracy of AI-generated responses.
- [Tracing the Thoughts of Claude: Peering into an AI's Mind](https://www.getmaxim.ai/blog/tracing-the-thoughts-of-claude-peering-into-an-ais-mind): Exploration of Anthropic's research on understanding AI models like Claude.

#### Advanced AI Systems

- [AlphaEvolve: AI for Scientific Discovery](https://www.getmaxim.ai/blog/alphaevolve-ai-for-scientific-discovery): Exploration of AlphaEvolve, an AI system for algorithmic discovery in scientific challenges.
- [Agent Workflow Memory](https://www.getmaxim.ai/blog/agent-workflow-memory): Exploration of Agent Workflow Memory for improving long-horizon AI tasks.
- [Tool Chaos No More: Measuring Model-Tool Accuracy](https://www.getmaxim.ai/blog/tool-chaos-no-more-how-were-measuring-model-tool-accuracy-in-the-age-of-mcp): Insights into benchmarking tool call accuracy in AI models using MCP.
- [Model Context Protocol Guide (MCP)](https://www.getmaxim.ai/blog/model-context-protocol-guide-mcp): Comprehensive guide to MCP for enabling real-time AI-powered workflows.
- [Introduction to the Agent2Agent Protocol (A2A)](https://www.getmaxim.ai/blog/introduction-to-the-agent2agent-protocol-a2a): Overview of Google's A2A protocol for enabling seamless communication between autonomous AI agents.
- [The Era of Experience: Vision for the Next Frontier in AI](https://www.getmaxim.ai/blog/the-era-of-experience-vision-for-the-next-frontier-in-ai): Exploring experiential learning as the next paradigm in AI development.

#### Benchmarks & Evaluations

- [VGBench: Evaluating Vision-Language Models in Real-Time Gaming Environments](https://www.getmaxim.ai/blog/vgbench-evaluating-vision-language-models-in-real-time-gaming-environments): Introducing VGBench, a benchmark for evaluating Vision-Language Models in dynamic gaming environments.
- [OpenAI's BrowseComp: Redefining How We Benchmark Web-Browsing Agents](https://www.getmaxim.ai/blog/openai-browsecomp-web-browsing-agent-benchmark): An overview of OpenAI's BrowseComp benchmark for evaluating web-browsing agents.
- [BrowserGym: Technical Deep Dive into Web Agent Automation](https://www.getmaxim.ai/blog/browsergym-web-agent-automation): An in-depth look at BrowserGym's framework for web agent automation and evaluation.
- [Inside OpenAI's o1: Part 1](https://www.getmaxim.ai/blog/inside-openai-o1): An in-depth analysis of OpenAI's o1 model family, focusing on evaluations and safety mechanisms.
- [Inside OpenAI's o1: Part 2](https://www.getmaxim.ai/blog/inside-openai-o1-part-2): Exploration of OpenAI's o1 model capabilities and evaluations.
- [Claude 3.5 Sonnet put to the test](https://www.getmaxim.ai/blog/claude-3-5-sonnet-put-to-the-test): A detailed comparison of Claude 3.5 Sonnet and GPT-4o models.

#### Domain-Specific Applications

- [Uber: Natural Language to SQL](https://www.getmaxim.ai/blog/nl-to-sql-uber): Overview of Uber's QueryGPT system for generating SQL queries from natural language prompts.

### Announcements

- [Announcing Maxim AI's General Availability and Seed Round](https://www.getmaxim.ai/blog/announcing-maxim-ais-general-availability-and-the-3m-funding-round-led-by-elevation-capital): Announcement of Maxim AI's general availability and $3M funding round led by Elevation Capital.
- [Maxim Social Updates](https://www.getmaxim.ai/blog/maxim-social-updates): Highlights Maxim AI's partnerships, launches, and platform listings.

## Settings & Configuration

- [Maxim API Keys](https://www.getmaxim.ai/docs/settings/maxim-api-keys): Guide to creating and managing Maxim API keys for authentication.
- [Vault](https://www.getmaxim.ai/docs/settings/vault): Learn how to securely store sensitive information using Maxim's Vault feature.
- [Model Configuration](https://www.getmaxim.ai/docs/settings/model-configuration): Learn how to configure models in Maxim.
- [Custom Pricing](https://www.getmaxim.ai/docs/settings/custom-pricing): Documentation for setting up custom token pricing in Maxim.
- [Members and Roles - Settings](https://www.getmaxim.ai/docs/settings/members-and-roles): Guide on managing team members and roles in Maxim AI.
- [Two-Factor Authentication](https://www.getmaxim.ai/docs/settings/two-factor-authentication): Instructions for enabling two-factor authentication in Maxim.

## Self-Hosting & Enterprise

- [Self-Hosting Overview](https://www.getmaxim.ai/docs/self-hosting/overview): Overview of Maxim's self-hosting options for enterprise deployment.
- [Zero Touch Deployment](https://www.getmaxim.ai/docs/self-hosting/zerotouch): Guide to Maxim's zero-touch deployment process for secure and private self-hosting.
- [Data Plane Deployment](https://www.getmaxim.ai/docs/self-hosting/dataplane): Details on deploying Maxim's data processing infrastructure within your cloud environment.

## Legal & Policies

- [Privacy Policy](https://www.getmaxim.ai/privacy-policy): Details Maxim's policies on data collection, usage, and user rights.
- [Terms of Service](https://www.getmaxim.ai/terms-of-service): Legal terms governing the use of Maxim's platform and services.

## Additional Resources

- [The GenAI evaluation and observability platform](https://www.getmaxim.ai/llms.txt): Overview of Maxim AI's GenAI evaluation and observability platform.
- [Login - Maxim AI](https://www.getmaxim.ai/login): Sign in to Maxim AI to evaluate and improve AI faster.
- [Request Access to Maxim AI](https://www.getmaxim.ai/request-access): A landing page to request access to Maxim AI with a 14-day free trial.
- [About Maxim Blog](https://www.getmaxim.ai/blog/about): Introduction to the Maxim Blog and its subscription model.
- [Blog](https://www.getmaxim.ai/blog): Discover the latest updates, insights, and research in AI and Maxim's ecosystem.
