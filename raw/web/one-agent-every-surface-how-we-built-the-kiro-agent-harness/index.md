---
source_url: https://kiro.dev/blog/one-agent/
title: "One agent, every surface: how we built the Kiro agent harness"
published: 2026-08-03
fetched: 2026-08-07
---

# One agent, every surface: how we built the Kiro agent harness

---
title: "One agent, every surface: how we built the Kiro agent harness"
url: https://kiro.dev/blog/one-agent/
hostname: kiro.dev
sitename: Kiro
date: "2026-08-03"
tags: ['Kiro,Kiro IDE,Kiro Spec,Kiro AI,Kiro AI IDE,kiro,aws kiro,amazon kiro,agentic IDE,spec-driven development,Claude,亚马逊kiro,亚马逊云kiro,亚马逊云科技kiro,kiro集成开发环境,aws集成开发环境,亚马逊/amazon集成开发环境,kiro编程,kiro下载,kiro安装包,kiro安装包下载,kiro官网,规范驱动开发,AI测试,AI开发,代码助手,编程IDE,AI编程助手,智能编码助手,AI辅助编程,AI写代码,AI代码生成,模型生成代码,AI驱动编程,编程效率工具']
---
# One agent, every surface: how we built the Kiro agent harness

[CL](https://github.com/clareliguori/)

Clare Liguori

Engineering Lead

Romain Dura

Engineering

[AL](https://github.com/alharris-at)

Al Harris

Engineering

[RI](https://github.com/undefobj)

Richard Threlkeld

Engineering

Early on in building Kiro, we started talking about what agentic development should feel like across a developer’s day. The picture we kept coming back to was one where sessions move between your laptop, a cloud sandbox, and back again without friction. You close your laptop at the end of the day and your Kiro session keeps running in the cloud. You check on it from your phone while you grab coffee. You open the Kiro [IDE](https://kiro.dev/ide/) the next morning and pick up where you left off. You start a project in Kiro on the [web](https://kiro.dev/web/), add context in the Kiro IDE, keep working in the Kiro [CLI](https://kiro.dev/cli/) where you’re already running tests and iterating in the terminal, and check on progress from Slack. Agentic development should be one continuous conversation across every surface you work in.

Earlier this year, we realized that our agent architecture was preventing us from moving toward that vision. At the time, the Kiro IDE, CLI, and web clients each ran their own purpose-built agent with its own session format, tool set, and configuration model. Easily moving between sessions and environments requires a single agent that works the same way regardless of which client you’re using or where it’s running. In our client-dedicated agent architecture, a session that started in one client couldn’t move to another because the agents didn’t share enough common ground. This post covers how we consolidated those three agent codebases into a single Kiro agent harness (built, naturally, using Kiro itself) and the architecture decisions that make our vision now within reach.

When we started building Kiro, we optimized for speed and experimentation. We encouraged each client team to build their own agent harness. The agent harness is the orchestration layer that manages the agent loop, tool execution, sub-agent delegation, session management, configuration loading, and communication with the model. The IDE team built theirs in TypeScript to fit the Code OSS extension model, the CLI team built theirs in Rust for performance, and the web team built theirs in Python to stay close to the latest agent research.

Having separate harnesses let each team ship independently and iterate fast, but it also meant that each team made different choices. Session storage worked differently across clients. The permission systems were designed independently and used incompatible syntax: the CLI used regex-based `allowedCommands`/`deniedCommands`, while the IDE used prefix matching for `trustedCommands` and substring matching for its denylist. Compaction strategies diverged. Sub-agent context sharing followed different models. Custom agents worked differently in each client. Feature sets split too: spec-driven development and powers existed only in the IDE, while plan mode and code intelligence existed only in the CLI.

Implementation cost compounded over time. Every new capability had to be built and maintained three times, sometimes resulting in slightly varying agent behaviors. Bugs had to be fixed three times. Users experienced inconsistencies depending on which client they chose. Our vision of sessions moving across clients and compute was architecturally impossible because there was no shared session format, no shared tool set, and no shared configuration model. We considered agreeing on agent behavior contracts across clients and implementing them in each of the three harnesses, in order to maintain each team’s independence and individual speed. However, interface alignment also introduces coordination overhead that grows with every new feature. Every new feature needs a spec, three implementations, and ongoing validation that they behave identically.

The inflection point came as we prepared to publicly launch Kiro on the web. Rather than launch Kiro on the web with its own separate agent and continue paying that compounding implementation cost, we decided to build a single agent harness that combined the best of what each team had learned. A single harness eliminates duplication across teams and lets us invest all of our effort in one place.

A key architectural decision we made early was to build the harness as a standalone server process, not a library compiled into each client. We saw from earlier attempts that shared libraries don’t enforce a strong enough boundary. Client code ends up calling internal methods that weren’t intended to be exported, or layering its own agent logic on top of the library. Then you’re back to diverging implementations. A standalone process makes the separation real. The harness and clients don’t need to share a language or runtime, so each client can stay in whatever stack fits its platform.

Now, instead of three tightly coupled client-agent pairs:

We have a clean separation between clients and a single agent harness:

The Kiro agent harness is a lightweight process that runs alongside your codebase, starts quickly, and owns everything on the agent side. The client owns how the user interacts with the agent and how it presents the agent’s work. The only way to cross that boundary is through the defined protocol interface. Since it's a standalone process rather than a compiled-in library, it can run on any compute. The same harness can start on your laptop or run inside a VM in the cloud without the client caring.

The well-defined interface between server and client means the agent code evolves independently of the clients. If a harness change doesn’t touch the protocol interface (for example, adding a new tool, improving planning, tuning the agent loop), it ships immediately in every client with zero client-side changes. For example, we recently added live custom agent reload: you can edit a file in `.kiro/agents/` mid-session and the harness picks it up immediately, re-advertising available commands to the client. This required no client changes because the notification type for available commands already existed in the protocol. Every client got it for free.

The harness is not one-size-fits-all, because of the variety of clients it was built to support. Different clients have different capabilities, and some operations make more sense implemented at the client level using client-native functionality. A client can provide its own tools and suppress built-in ones so that it can use what makes sense for its form factor. For example, the IDE uses Code OSS’s APIs for file manipulation and provides its own file read and write tools instead of the harness’s built-in ones that operate directly on the filesystem. When the agent needs to run one of these client-provided tools, it notifies the client, which executes the tool and returns the result.

We chose the [Agent Client Protocol (ACP)](https://agentclientprotocol.org/) as the protocol that defines the boundary between client and harness. ACP is a standardized spec for agent-client communication that reached 1.0 in June 2026. The protocol is supported in IDEs like JetBrains IDEs, Xcode, and Zed and in other editors including Obsidian, Emacs, and Neovim. We already had experience with ACP from [adopting it in the Kiro CLI](https://kiro.dev/blog/kiro-adopts-acp/) earlier this year, enabling users to interact with Kiro directly in those applications. We decided to use ACP for the unified harness too, not just for third-party editors but as the interface between Kiro’s own clients and our own agent. Two properties of ACP made this possible: its extensibility for custom methods, and its flexibility around transports.

ACP officially supports stdio as its transport, which works well for local clients where the harness runs as a child process of the editor or terminal. For remote clients like Kiro on the web and the iOS app, we needed a different transport. We added a custom WebSocket-based transport so those clients can connect to a harness running in a cloud sandbox. The binary, the tools, and the agent behavior are the same regardless of which transport a client uses.

Beyond transports, we extended ACP’s method set into what we call Kiro-ACP. Standard ACP handles the fundamentals (session lifecycle, message streaming, and tool call reporting), but Kiro’s features needed more. For example, we added live steering so users can send a message that gets injected at the next inference turn while the agent is working, shaping its direction without cancelling or waiting. ACP does not support queuing messages, so we extended ACP with new method properties and notifications to enable live steering. We also modeled Kiro’s spec-driven development workflow as a set of dedicated methods, extended ACP’s basic tool approval into a rich multi-scope permission system, and added notifications for context window usage and hook execution. In total, Kiro-ACP adds more than 20 agent-callable methods, 15 client-callable methods, and 20 notification types on top of the base protocol. ACP’s extensibility model keeps this clean: custom methods use an underscore prefix per the spec, and all of Kiro’s extensions live under the `_kiro/` namespace. We can extend the protocol for Kiro-specific features without forking it.

The result is that third-party clients connect the same way our first-party clients do. Any ACP-compatible client gets the full agent with tools, sub-agents, session management, and MCP connectivity. First-party clients (IDE, CLI, web, iOS) additionally use the Kiro-ACP extensions for features like live steering, specs, rich permissions UI, and context usage tracking.

The immediate payoff of a single harness is that features previously locked to one client are now available everywhere, with the same configuration format and the same behavior.

**Spec-driven development** was previously IDE-only. Now it runs in the CLI (start one with `/spec new`) and in Kiro on the web. The agent handles the LLM interactions and automated reasoning that drive the spec workflow (generating requirements, producing a technical design, breaking work into tasks), and each client presents it in a way appropriate for its form factor. The IDE shows spec artifacts in side-by-side panels. The CLI renders them in the terminal. Kiro on the web displays them in the browser with inline review and multi-user collaboration, so a team can iterate on specs together. The agent speaks ACP and the client decides how to present the output.

**Custom agents** use the same `.kiro/agents/` Markdown format across all surfaces. You define an agent with a description, system prompt, tag-based tool selection (simple tags like `read`, `write`, and `shell` instead of individual tool names), accessible sub-agents, inline MCP server definitions, and inline permission rules. Commit a custom agent’s configuration to version control and every team member gets it in every client:

**Hooks** use the same `.kiro/hooks/*.json` format with the same triggers (`SessionStart`, `PreToolUse`, `PostToolUse`, `FileCreate`, `FileSave`) and the same behavior in every client.

Beyond feature availability, the unified harness means you get consistent behavior in areas that are hard to get right. Context management, compaction, and summarization all work the same way regardless of which client you use. Previously, each harness had its own compaction strategy, which meant sessions could behave differently as they got longer depending on whether you were in the IDE, CLI, or web client. Now there’s one implementation, tested and improved in one place. Since launching the unified harness across our clients, we’ve already shipped improved compaction prompts in the harness for better context retention. We’ve also shipped resilience and performance improvements deep in the harness: improved retry logic for model inference requests, faster permission evaluation, and more resilient MCP server connections. Every client benefits from these changes. The result is consistent quality and reliability regardless of which surface you prefer.

Before the unified harness, each client had its own permission system with different syntax, different semantics, and different configuration locations. The CLI used `allowedCommands`/`deniedCommands` with regex patterns. The IDE used trustedCommands with prefix matching and a separate `commandDenylist` with substring matching. In both clients, permissions were per-tool: a single intent like `deny reads to .env` had to be configured separately for every tool that could read files (read, glob, grep, code intelligence). Miss one and the agent could still access the file through a different tool. Users faced a poor tradeoff between pressing ‘y’ at every single tool invocation or trusting everything, with no useful middle ground. We wanted a permission model that could express intent at the capability level and reduce acceptance fatigue through persistent and composable consent.

Now there’s a single capability-based permission model backed by [Cedar](https://www.cedarpolicy.com/), a formally verified policy language. One rule can target an entire class of operations across all tools:

Capabilities group tools by what they do: `fs_read`, `fs_write`, `shell`, `web_fetch`, `mcp`, `subagent`, and others. A deny on fs_read blocks every tool that reads files (`read_file`, `grep_search`, `file_search`, and any future `read` tool) without enumerating them individually.

Policies compose across multiple scopes and merge with deny-always-wins semantics. Kiro itself enforces immutable security invariants (for example, the agent cannot modify its own permission files). Enterprise administrators can push restrictions via MDM. Users configure their own rules at the user or workspace level. Agent profiles can declare permissions appropriate for their role. Session-level decisions accumulate as you work. No upfront configuration is required. The policy grows organically as you make consent decisions, and you can persist them at whichever scope makes sense.

The payoff from our new agent harness architecture is already showing. Since all clients moved onto the unified harness, we’ve shipped multiple features across clients that required zero client changes, including global hooks and policy presets. **Global hooks** let you define hooks once in `~/.kiro/hooks/` that fire in every workspace automatically, so cross-cutting behaviors like linting on save or security checks before commits no longer need to be duplicated per project. **Policy presets** are composable named rule sets like `edit-workspace` and `dev-shell` that reduce prompt fatigue for common workflows. When you add policy presets to your permissions (such as `policies: [dev-shell, edit-workspace, read-all]`), the harness’s policy engine expands them into individual rules at load time. Both features shipped to all clients with a harness update alone.

The vision we described at the top of this post requires some agent capabilities that we still need to build, such as session packaging for moving sessions across environments and the ability to control both local and cloud sessions from any client. The unified harness means we only need to build each new capability once. In many cases, as with global hooks and policy presets, we can ship them across all clients with zero client changes needed. Some features need client work on top of a new agent capability. The unified harness didn’t eliminate client work entirely, nor did we want it to. A terminal, a desktop IDE, a browser, and a phone have different interaction models, and we want each surface to feel native to its form factor rather than deliver a one-size-fits-all experience. With the new agent harness architecture, the agent logic is the same across clients and each client team can focus on how best to interact with it.

For you as a Kiro user, the new agent harness architecture means new capabilities arrive faster, behave consistently, and work with the same configuration regardless of which surface you prefer.

The new Kiro agent harness is live across all four Kiro clients, so you can try it out today:

- [**Kiro IDE**](https://kiro.dev/ide/) **1.0** brings capability-based permissions, custom agents with tag-based tools and inline MCP, agent focus mode for directing parallel sessions, dockable chat tabs, and session export. Read the[IDE 1.0 docs and how to migrate](https://kiro.dev/docs/whats-new-1-0/) .
- [**Kiro CLI**](https://kiro.dev/cli/) **v3** (early access) runs the same unified harness in your terminal with spec-driven development, permissions.yaml, enhanced hooks, and the new agent config format. Try it with`kiro-cli --v3` . Read the[CLI v3 docs and how to migrate](https://kiro.dev/docs/cli/v3/) .
- [**Kiro on the web**](https://kiro.dev/web/) (preview) runs the harness in cloud sandboxes for autonomous development with specs in the browser, multi-repo sessions, and GitHub and GitLab integration.[Sign in / up](https://app.kiro.dev) .
- [**Kiro for iOS**](https://kiro.dev/mobile/) (preview) connects to the same cloud sessions as Kiro on the web from your phone so you can kick off autonomous work, review diffs, and approve changes without opening your laptop.[Request early access](https://kiro.dev/mobile/) .
