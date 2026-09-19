# AI Lead Generation Engine

Multi-model AI powered lead discovery, enrichment & export platform.

## Features

- **Multi-Source Search**: Google, Bing, DuckDuckGo
- **AI Enrichment**: Kimi K3, GPT-6 Astra, DeepSeek V4, Claude Fable, Hermes 4, GLM 5.3
- **Contact Extraction**: Phone, Email, Social Links from websites
- **Export**: CSV, JSON download
- **Modern UI**: Dark theme, responsive, real-time status

## Stack

- Next.js 14 (App Router)
- Tailwind CSS
- OpenRouter API (multi-model AI)
- Cheerio (HTML parsing)

## Setup

```bash
npm install
cp .env.example .env
# Add your OPENROUTER_API_KEY to .env
npm run dev
```

## Deploy to Vercel

1. Push to GitHub
2. Import repo on vercel.com
3. Add `OPENROUTER_API_KEY` in environment variables
4. Deploy

## Environment Variables

| Variable | Description |
|---|---|
| `OPENROUTER_API_KEY` | Your OpenRouter API key |

## Models Used

| Model | Role |
|---|---|
| `openrouter/auto` | Auto-select best model |
| `moonshotai/kimi-k3` | Long context analysis |
| `openai/gpt-6-astra` | Creative strategy |
| `deepseek/deepseek-v4-flash-0731` | Fast reasoning |
| `anthropic/claude-fable-5.1` | Architecture review |
| `nousresearch/hermes-4-70b` | Self-improving agent |
| `z-ai/glm-5.3-flash` | Fast frontier |
