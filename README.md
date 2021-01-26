# demo_boxo
initial commit

Pretty basic visual effect. Draw four lines each step, and move them across the screen. When a line hits the other side, start it over.
Each step, change the color a little bit.

Still need to precalculate a lookup table for the colors.
Current method is to move one color (R, G, or B) up or down until it hits a limit, then tag another color in to do the opposite of whatever was happening.
Probably a simpler way to do that.

Tab to toggle vibrant or pastel mode. Spacebar to switch from lines to drawing a rectangle.
Up and down arrows change the speed at which the colors rotate, but I've been having trouble getting that to work right.
Escape key to exit.

Eventually would like to see what happens when a pallette shift is added.

Need to add a delta-time framerate limiter. This runs somewhat smoothly on my laptop, on a decent system could be too fast to see (if things are optimized correctly).
