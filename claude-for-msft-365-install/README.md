# Claude for Office — Direct Cloud Setup

Admin tooling for configuring the Claude Office add-in to call your own cloud
(Vertex AI, Bedrock, or an LLM gateway) instead of Anthropic's API.

## Install

```bash
claude plugin marketplace add anthropics/financial-services-plugins
claude plugin install claude-for-msft-365-install@financial-services-plugins
```

Then inside the session: `/claude-for-msft-365-install:setup`

## Commands

| Command | What it does |
|---|---|
| `/claude-for-msft-365-install:setup` | Interactive wizard — provisions cloud resources, admin consent, writes manifest |
| `/claude-for-msft-365-install:manifest` | Generate the customized add-in manifest XML |
| `/claude-for-msft-365-install:consent` | Azure admin consent URL for the add-in's app registration |
| `/claude-for-msft-365-install:update-user-attrs` | Write per-user config via Microsoft Graph extension attributes |
| `/claude-for-msft-365-install:bootstrap` | Build the bootstrap endpoint — per-user MCP servers, skills, dynamic config |

## Notes (personal)

- Tested against Bedrock (us-east-1) with `claude-3-5-sonnet-20241022` — works out of the box.
- The `setup` wizard prompts for a region; defaulting to `us-east-1` saves a step if you're on AWS.
- Run `consent` before `manifest` when setting up a net-new Azure app registration, otherwise the
  manifest upload step will fail with a 403.
- Also tested with `claude-3-7-sonnet-20250219` on Bedrock — works fine, noticeably better at
  multi-step Excel formula tasks. Worth the upgrade if your org is already on the model.
