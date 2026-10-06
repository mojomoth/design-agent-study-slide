# Part 13 source (from: guide/How to turn your AI into a world-class designer.html)
Proposed Korean slide title: 기법 6: 가치를 더하지 않는 요소 덜어내기

[h2] Technique 6: Cut out elements that don’t add value

[p] AI loves to add more, but it rarely takes away. One of the biggest signs that a design is AI-generated is that it overexplains everything or contains elements that don’t serve any practical purpose. By contrast, a design that exercises restraint immediately looks premium and tasteful.

[p] When polishing AI designs, most of my effort goes into removing things. For example, when I was building my calorie tracking app, this was my initial design from Claude:

[FIGURE 22] path: assets/how-to-turn-your-ai-into-a-world/figure-22-dc9186ef-2b04-42a0-a460-8898b0590797_1456x964.jpg

[p] I’d described the app’s functionality and specifically asked for a “clean, minimalist design.” The results weren’t bad, and were certainly impressive for being fully AI-generated. However, despite my asking for minimalism, a lot in the design wasn’t adding value:

[list] - Pink glowy effects in the background and on the progress bar
- Random colors and highlights on text
- Extra labels and empty space when displaying all the foods for a day, when the images already communicate this
- Custom buttons and text fields that look worse than built-in iOS components

[p] I asked Claude to dial things back:

[list] - Simplify the layout into an image-centric grid
- Get rid of gradients, glows, and unnecessary containers
- Aim for a truly minimalist aesthetic that feels Apple-native

[p] This was the result:

[FIGURE 23] path: assets/how-to-turn-your-ai-into-a-world/figure-23-fdf80ee5-9f43-44e9-93cf-c477a9e49128_1456x964.jpg

[p] To my trained eye, the result is much better. It’s opinionated and allows the visuals to speak for themselves. It uses native iOS components, and the excessive colors and gradients are gone. The text is smaller, simpler, and tighter. This is good design.

[p] Today’s AI models would never think to make these choices on their own. Remember, AI doesn’t like to take risks, and it’s risky to strip down a design and delete code. The model needs a push from you. Look over your design and ask yourself what really needs to be there. Often, putting less on the screen communicates more, because you can hold your users’ attention without overwhelming them with clutter.
