# Part 11 source (from: guide/How to turn your AI into a world-class designer.html)
Proposed Korean slide title: 기법 5: 고급 모션에는 영상 생성 활용하기

[h2] Technique 5: For more advanced motion, use video generation

[p] Video generation models are incredibly powerful these days, but most people think of them as tools for generating UGC ads or clips of Will Smith eating spaghetti. They can work wonders for everyday design work too.

[p] There are many video models out there, and the best ones change frequently, so I like to use an aggregator platform like fal.ai. This way, we can give our agent a single API key and let it evaluate different options and choose the best one without needing multiple integrations.
    (link: “fal.ai” → http://fal.ai/)

[p] Here are two ways I love to use video models in my designs:

[h4] Create stunning animated graphics

[p] The trick is to generate a looping clip with a solid color background, then either chroma key it out (like a green screen) or, in more complex cases, use a video matting model to remove the background. This gives you an animation that you can layer anywhere in your UI without it looking like a video.

[p] For example, I took one of our previous designs and ran this prompt:

[p] Prompt:

[blockquote] Can you replace the image on this page with a looping video clip that does something more interesting? Have the crystal splinter apart and slowly spin around. It should have awesome glassy effects that refract the page background and cast shadows and light around it.
To get convincing glass refraction effects, render the video of the glass over the page background colors first (so it bakes in the refraction effects), then remove the background with a video matting model.
Use this fal.ai API key: sk-a1b2c3d4…
Find appropriate recent models for video generation and background removal.

[p] GPT-5.6 Sol (before and after):

[FIGURE 20] path: assets/how-to-turn-your-ai-into-a-world/figure-20-aa994e2f-caec-40bf-8cc5-8a1ef101dd21_1456x399.gif

[p] This is a much richer effect than you can get with code: interesting caustic reflections, glassy refraction effects, and complex physical motion.

[h4] Create fluid transitions between states

[p] This is a really underrated use case for video models. In addition to generating video from text, many video models can interpolate between keyframe images. This lets you take two product stills and create a transition clip between them. You can play the clip when the user takes an action (like navigating to another screen of your app) or scrub through it frame-by-frame in response to a gesture (like scrolling or swiping).

[p] Here’s a demo page showing off a scroll effect. I built it with a single prompt using GPT-5.6 Sol in Codex:

[p] Prompt:

[blockquote] Build a demo page for a suitcase that uses a video model to create interactive transitions between a couple of screens. Each screen should show the suitcase in a different state, with vertical motion that feels appropriate for scrolling:
- Initially, have the suitcase floating high up in the air
- Then have it land on the floor and pop open
- Finally, have its contents neatly land into it from the top
Generate the initial frame using your image generation skill. Then, generate a video clip that starts from that frame and animates to the next state. Use the final frame of that video to seed the next transition so that it continues seamlessly. Scrub through the transitions one by one as the user scrolls.
Use this fal.ai API key: sk-a1b2c3d4…
Use a video model with strong physics and consistency, like Seedance 2.5.

[p] GPT-5.6 Sol:

[FIGURE 21] path: assets/how-to-turn-your-ai-into-a-world/figure-21-2f3bb583-375b-4a12-aa57-64a10bf2d9e7_960x540.gif

[p] The transitions between pages scrub fluidly with the user’s scrolling and are fun to play with. Design like this makes the user want to keep scrolling and reading more about your product. And it only took one prompt!
