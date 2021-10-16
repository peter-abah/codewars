// Bouncing Ball
// KATA LINK: https://www.codewars.com/kata/5544c7a5cb454edb3c000047

// A child is playing with a ball on the nth floor of a tall building. 
// The height of this floor, h, is known.

// He drops the ball out of the window. 
// The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

// His mother looks out of a window 1.5 meters from the ground.

// How many times will the mother see the ball pass in front of her window (including 
// when it's falling and bouncing?)

// Three conditions must be met for a valid experiment:
// Float parameter "h" in meters must be greater than 0
// Float parameter "bounce" must be greater than 0 and less than 1
// Float parameter "window" must be less than h.
// If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

function bouncingBall(h,  b,  w) {
  if (h <= 0 || b <= 0 || b >= 1 || w >= h)
    return -1;

  let r = Math.log(w/h) / Math.log(b);
  return (Math.ceil(r) - .5) * 2;
}