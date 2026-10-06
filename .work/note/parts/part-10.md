# Part 10 source (from: guide/How to turn your AI into a world-class designer.html)
Proposed Korean slide title: 기법 4: 이미지 생성으로 디자인 풍부하게 만들기

[h2] Technique 4: Use image generation to enrich designs

[p] Coding agents love to write code, but they usually don’t incorporate images. Instead, they tend to use the easy code-based alternatives: gradients, shapes, and basic patterns. Those are all strong giveaways of an AI-generated design.

[p] Some agents have image tools built in, but they underutilize them. Others don’t have image tools out of the box but can easily use the OpenAI or Gemini APIs to generate images with an API key.

[p] Let’s try this on the designs from the last step:

[p] Prompt:

[blockquote] The design is pretty plain. Add more personality using image generation. Consider shaders or 3D effects in combination with images to create more interesting visuals.
For image generation, use this OpenAI API key (only use it locally, do not store it in the code or product): sk-a1b2c3d4…
Verify that your work looks right frame-by-frame in the browser.

[p] Claude Opus 5 (before and after):

[FIGURE 16] path: assets/how-to-turn-your-ai-into-a-world/figure-16-7e2a6925-7451-4abe-aaa8-bc92823dd69a_1456x399.gif

[FIGURE 17] path: assets/how-to-turn-your-ai-into-a-world/figure-17-f4ae7b09-1555-4ade-850c-212cb0d089b2_1456x399.gif

[FIGURE 18] path: assets/how-to-turn-your-ai-into-a-world/figure-18-7cd81d80-09c1-4244-9651-43bba85771a4_1456x399.gif

[FIGURE 19] path: assets/how-to-turn-your-ai-into-a-world/figure-19-c02123f6-00f8-4063-8463-5050d2649647_1456x399.gif

[p] Images and effects like these can quickly add a lot of personality and make a design less obviously AI-generated, since they demonstrate more than surface-level effort.

[p] Depending on your setup, there are different ways to connect your agent to image generation tools:

[list] - If you use Codex, Antigravity, or Grok Build:
  - Tell your agent to use its built-in image generation. The agent already knows how to do this but rarely does so until instructed.
- If you use Claude Code or another agent but also have a ChatGPT subscription:
  - Tell your agent, “Use the Codex CLI to generate images. Help me install it if it isn’t already present. Make sure it’s billing my subscription, not an API key.” This lets you use your ChatGPT subscription for image generation without extra costs.
- If you only use Claude, or any other tool:
  - The simplest path is to give your agent an OpenAI or Gemini API key to generate images. I recommend creating a separate API key with a tight spend limit, just for your agent. That way, your costs are controlled even if the key gets out or the agent misuses it, and you can easily revoke the key without disrupting other work.
  - If you find yourself pasting keys into chats frequently, put them in a file instead, and point your agent to it in your project. Tell your agent: “Create a gitignored file called .env.agents, store this API key in it, and note to yourself in AGENTS.md/CLAUDE.md that these keys are for you to use during development (but must not ship with the product).”
