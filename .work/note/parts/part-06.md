# Part 6 source (from: guide/How to turn your AI into a world-class designer.html)
Proposed Korean slide title: 기법 1: 시드 문자열로 다양성 불어넣기

[h2] Technique 1: Use seed strings to inject variety

[p] The idea here is to get the model to find a new source of inspiration for designs, rather than relying on the defaults it learned from training. If you’ve tried to prompt a model to design a website or app, you’ve probably already seen what that default looks like.

[p] As a simple example, I gave four instances of Claude Code the same prompt:

[p] Prompt:

[blockquote] Build me a landing page for my productivity app.

[p] Claude Opus 5:

[FIGURE 5] path: assets/how-to-turn-your-ai-into-a-world/figure-05-7b59bdf3-8a82-46d1-94c2-4a1e60ea7cbf_1456x894.jpg

[p] Almost every time, we get a purplish gradient, text on the left, graphic on the right, and the exact same structure. It looks like every AI-designed website ever.

[p] We didn’t ask the model to do anything unique or varied, so it makes sense that it keeps falling back on the same patterns it knows well. But just asking for variety doesn’t work:

[p] Prompt:

[blockquote] Build me a landing page for my productivity app. Give me something totally unique. Make every design decision completely at random.

[p] Claude Opus 5:

[FIGURE 6] path: assets/how-to-turn-your-ai-into-a-world/figure-06-f37064a7-2853-4314-b175-aa65b8a13f43_1456x876.jpg

[p] The results are different from before, but they’re still not varied. The model always uses the same color scheme, structure, and even the same awkward pottery metaphors. It’s predicting tokens that sound random but aren’t actually random.

[p] The problem is that the model can’t inherently act randomly. It can only predict the most likely token. If we want variety, we have to bring it from outside the model. One technique for this is String Seed of Thought, published by Sakana AI. We make the AI generate a random string and use it as design inspiration. That way, the model is truly making different decisions each time.
    (link: “published by Sakana AI” → https://pub.sakana.ai/ssot/)

[p] Prompt:

[blockquote] I want you to build me a landing page for my productivity app.
Follow this procedure:
- Generate a long, random alphanumeric string using a shell script.
- Define the creative direction (color scheme, layout, typography, etc.) based on the string. Look beyond the surface for subpatterns, special numbers, anything that inspires you.
- Use your judgment to bring this direction to life and make it look great.
Don’t reveal the string in the design. It’s only for your inspiration.

[p] Claude Opus 5:

[FIGURE 7] path: assets/how-to-turn-your-ai-into-a-world/figure-07-bcda7156-dbbd-4d18-a7fb-4cfc124563bf_1456x876.jpg

[p] Suddenly the outputs are much more varied! Now we’re seeing different color schemes, fonts, and new ideas. The previous designs were ones that any Claude user could get. These designs are one-of-a-kind; no two runs ever produce the same result.
