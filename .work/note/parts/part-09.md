# Part 9 source (from: guide/How to turn your AI into a world-class designer.html)
Proposed Korean slide title: 기법 3: 서브에이전트로 긍정적 피드백 루프 만들기

[h2] Technique 3: Create positive feedback loops with subagents

[p] We need to iterate on our designs to improve them. But simply asking our agent to look at the design and improve it won’t work, because the agent isn’t objective: it reviews its own code, past decisions, and previous rationale. AI can’t easily zoom out, look at the big picture, and “think different.”

[p] To solve this, instead of letting the coding agent decide when the design is good enough, have it ask another agent—a “design critic.” The critic’s job is to look at screenshots of the current design and provide feedback. It doesn’t care how the current design is implemented or how much effort went into it, only if it actually hits the quality bar.

[p] This approach has an extra benefit: we can use a big, expensive model for the critic without breaking the bank, because we’ll only use it for executive decisions. A cheap, fast model can do the grunt work, while the strong critic model provides taste.

[p] Let’s try this on our previous designs, using Claude Fable 5 as the critic:

[p] Prompt:

[blockquote] I want you to improve this design. To figure out what to focus on, use a Fable 5 subagent as a design critic.
Follow this procedure at each iteration:
- Capture a screenshot of the current design
- Invoke the critic in a fresh context, with just the screenshot, not the code, implementation details, or earlier iterations/critiques
- Ask it to evaluate the aesthetic that the design is going for, imagine how a top design studio would execute this aesthetic, then outline the biggest gaps
- Lastly, it should provide a score out of 10 indicating how close the current design is to that studio-level quality bar
Provide this guidance to the critic in its prompt:
- It should think high-level about the overall structure and composition as well as look at the fine details
- It should watch out for patterns that feel overdone, excessive, or otherwise obviously AI-generated, and penalize them
- It should provide tight, specific feedback, not vague prose
- It should be bold and opinionated, not rely on what’s safe or easy
Your work is only complete when the critic independently deems it 9/10 or higher. Do not put that criterion in the critic prompt; keep it objective in its scoring. Use the same critic prompt each time.

[p] Claude Opus 5:

[FIGURE 15] path: assets/how-to-turn-your-ai-into-a-world/figure-15-5e045d71-d5f7-436a-be1f-eb870df24062_1456x1861.jpg

[p] Instead of the same cookie-cutter layout over and over, each design now has its own identity—but still maintains its original high-level aesthetic.

[p] Notably, in each case, Fable accounted for less than 10% of output tokens. Asking Fable to redesign the page directly would have cost twice as much and taken much longer.

[p] The way you set these loops up matters a lot. Here are some tips:

[list] - Make sure the criteria for the critic are as clear and objective as possible.
  - Bad: “Judge if our design looks beautiful, not AI-generated.” This is too subjective, and the results will vary wildly from run to run.
  - OK: “Review the aesthetic we’re going for, visualize how a top design studio would execute it, then judge our design’s quality against that bar.” The prompt is still mushy, but it provides a consistent framework and quality bar.
  - Great: “Here are 5 designs: 4 professional examples and 1 screenshot of our product. Rank them by polish and taste level.” This instruction is concrete and objective, and gives a visual baseline for judgment.
- Provide example images to demonstrate the target quality bar. You can use comparable screenshots or designs you like, or even AI-generated concept art. Instruct the critic to treat these as a baseline or a moodboard, not a target. You don’t want it to copy other designs outright.
- Set the stopping criteria carefully. Otherwise, the critic may never consider the design good enough, and your agent will helplessly burn tokens trying to please it. Prompt it to do one or two iterations first, and see if it’s converging before adding more.
- Choose the right model for each job. Consider bigger models for the critic role, since more parameters generally translate to better design sense and a wider distribution of ideas. Small models can be effective as the implementer, but don’t go too small. You still need a model that’s capable of executing a design direction well.
