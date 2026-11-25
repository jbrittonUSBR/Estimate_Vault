---
epoch: 1793116957205
mode: agent
backendId: opencode
sessionId: "ses_e81e87cd5ffeBrL2MltNTs9bKa"
tags:
  - copilot-conversation
agentLabel: "Opencode sign-in"
usage: '{"usedTokens":23584,"contextWindow":200000,"updatedAt":1793117428417}'
---

**user**: How do I sign into my opencode subscription?
[Timestamp: 2026/10/27 10:02:37]

**ai**: To sign in to your OpenCode subscription (OpenCode Go/Console):

### If you already subscribed
1. **Sign in to the Console** - Go to [opencode.ai/console](https://opencode.ai/console) and sign in with the account you subscribed with.
2. **Copy your API key** - On the Go/Console page, copy your API key after subscribing.
3. **Connect in OpenCode** - In the TUI/CLI, run:
   ```text
   /connect
   ```
   Select **OpenCode Go**, then paste your API key when prompted.
4. **Select a model** - Run `/models` and pick a model from the Go list (they appear as `opencode-go/<model-id>`).

### If you haven't subscribed yet
1. Sign in at [opencode.ai/console](https://opencode.ai/console).
2. Subscribe to [OpenCode Go](https://opencode.ai/console/go) ($10/month) or Go Plus ($40/month), add billing details.
3. Copy your API key and follow the steps above.

### Notes
- You don't need a subscription to use OpenCode - it's optional. You can also connect other providers via `/connect`.
- Go is typically for Personal workspaces (single member). 
- If you're using the web/desktop app, the same `/connect` flow applies in the TUI interface.

If you tell me whether you're using CLI, desktop, or web and if you hit any specific error, I can walk through troubleshooting.
[Timestamp: 2026/10/27 10:02:37]

**user**: /connect
[Timestamp: 2026/10/27 10:04:25]

**ai**: In the OpenCode TUI, `/connect` opens the provider authentication flow. Here's what happens:

1. **Run it** - Type `/connect` in the TUI (press `Ctrl+P` or just type the command if command palette is open). You'll see a list of providers/integrations available from your server and project.
2. **Select your provider** - Pick the one you want to sign in to (e.g., OpenCode Go if you have a subscription, or a specific provider like Anthropic/OpenAI).
3. **Authenticate** - Depending on the provider, you'll either:
   - Paste an API key
   - Complete OAuth (opens browser URL or gives a device/code - press `o` to open URL, `c` to copy)
   - Run a provider command / use environment auth
4. **Switch accounts if needed** - If already connected, selecting it shows your accounts where you can activate/rename/delete. Run `/connect` again to add another account.

**For OpenCode Go specifically:**
- Subscribe at [opencode.ai/console](https://opencode.ai/console), copy your API key
- Run `/connect` → select **OpenCode Go** → paste the key
- Then `/models` to pick a `opencode-go/...` model

Do you see any specific providers listed when you run `/connect`, or are you hitting an error? I can tailor this to exactly what you're seeing.
[Timestamp: 2026/10/27 10:04:25]

**user**: opencode auth login opencode
[Timestamp: 2026/10/27 10:08:41]

**ai**: If you run `opencode auth login opencode`, that depends on whether "opencode" is the exact integration ID/name for your subscription.

## For OpenCode Go (subscription)
From the docs, in the TUI you'd select **OpenCode Go**. The integration ID is likely `opencode-go` (based on model format like `opencode-go/kimi-k3`), not just `opencode`. 

Try:
```bash
opencode auth login opencode-go
```

If it has multiple auth methods, you can specify API key explicitly:
```bash
opencode auth login opencode-go --method key
```

## General notes
- If you omit the provider (`opencode auth login`), it opens an interactive picker in your terminal.
- API key entry/OAuth may require an interactive terminal.
- For OAuth flows, they may open a browser URL or give a device code.

## If you're using the Console/workspace
The Console flow is typically done via `/connect` in the TUI and choosing the workspace. The CLI `auth login` is for provider integrations.

Do you have your OpenCode Go API key from [opencode.ai/console](https://opencode.ai/console)? If you paste it when prompted after running the command, that should work. If the command fails or says "unknown provider", try without the provider name to see the full picker list.
[Timestamp: 2026/10/27 10:08:41]

**user**: /connect opencode auth login opencode-go
[Timestamp: 2026/10/27 10:09:58]

**ai**: Those are two different things, so you can't combine them like that. 

- `/connect` is a TUI slash command (run *inside* the OpenCode TUI)
- `opencode auth login ...` is a CLI shell command (run *outside* the TUI in your terminal) 

## Option 1: Use `/connect` inside the TUI (easiest)
1. Open the OpenCode TUI (`opencode` or the desktop app)
2. Type just this: 

   ```text
   /connect
   ```

3. Select **OpenCode Go** from the list
4. Paste your API key from [opencode.ai/console](https://opencode.ai/console) when prompted 

## Option 2: Use the CLI outside the TUI
1. Exit the TUI back to your normal terminal
2. Run this command: 

   ```bash
   opencode auth login opencode-go --method key
   ```

3. Paste your API key when prompted

The `opencode-go` ID is correct for Go, but the combined `/connect opencode auth login opencode-go` won't work in either place. Are you currently inside the TUI or in your shell? I can walk you through it from there based off of that!
[Timestamp: 2026/10/27 10:09:58]