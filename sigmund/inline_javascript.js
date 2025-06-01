/**
# Instuctions for JavaScript in inline_javascript

- Stimulus preparation should be done in Prepare phase. Stimulus presentation, response collection, etc. should be done in Run phase. The Prepare and Run phase are tabs in the `inline_javascript` GUI item.
JavaScript in the GUI:
- The code comments are for you. You don't need to include them verbatim in your responses.
- The following classes and objects are not available in `inline_javscript`: Keyboard, Mouse, Sampler, clock. Instead, use equivalent functionality in the GUI.
**/
// START_EXAMPLE: randomly positioned rectangles
// Related terms: visual search
// START_PREPARE_PHASE
var search_canvas = Canvas()  // Don't use `new`. Define with `var` to make object globally available
search_canvas.fixdot()
for (let [x, y] of xy_random(6, 200, 200, 40)) {  // 6 random coordinates within a 200x200 area and a minimum distance of 40
    search_canvas.rect({x:x-10, y:y+10, w:20, h:20, fill:true})  // pass parameters as object
}
// END_PREPARE_PHASE
// START_RUN_PHASE
search_canvas.show()
// END_RUN_PHASE
// END_EXAMPLE

// START_EXAMPLE: circles in a circular arrangement
// Related terms: visual search, additional singleton
// START_PREPARE_PHASE
var search_canvas = Canvas()
search_canvas.fixdot()
target_index = random.integer(5, 0)  // randomly select target position with random-ext package
let color
for (let [index, [x, y]] of enumerate(xy_circle(6, rho=200))) {  // 6 coordinates in a circle. Use enumerate from pythonic package
    color = (index === target_index ? 'red' : 'blue')
    search_canvas.rect({x:x-10, y:y+10, w:20, h:20, fill:true, color:color})
}
// END_PREPARE_PHASE
// END_EXAMPLE

// START_EXAMPLE: bilateral display with images on left and right0
// START_PREPARE_PHASE
var target_canvas = Canvas()
target_canvas.fixdot()
target_canvas.image({fname:left_img, x:-200})  // Assume that `left_img` and `right_img` contain names to files in the file pool
target_canvas.image({fname:left_img, x:200})
// END_PREPARE_PHASE
// END_EXAMPLE

// START_EXAMPLE: cueing paradigm with delay between cue and target
// Related terms: spatial cuing, posner task, symbolic cuing
// START_PREPARE_PHASE
var cue_canvas = Canvas()
var arrow_direction = (cue_side == 'left' ? -20 : 20)
cue_canvas.arrow({sx:20, sy:0, ex:arrow_direction, ey:0})
var blank_canvas = Canvas()
blank_canvas.fixdot()
var target_canvas = Canvas()
target_canvas.fixdot()
var target_x = (cue === 'valid' ? (cue_side === 'left' ? -200 : 200) : (cue_side === 'left' ? 200 : -200))
target_canvas.circle({x:target_x, y:0, r:20, fill:true})
// END_PREPARE_PHASE
// START_RUN_PHASE
cue_canvas.show()
setTimeout(function() {  // use setTimeout because there is no clock.sleep() in javascript
    blank_canvas.show()
    setTimeout(target_canvas.show(), 195)
}, 95)
// END_RUN_PHASE
// END_EXAMPLE

// START_EXAMPLE: rapid serial visual presentation (RSVP) with dynamic display
// Related term: attentional blink
// START_RUN_PHASE
const ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
var letters = random.subArray([...ascii_uppercase], 6)
var t_list = []
var delay = 0
letters.forEach(function(letter) {  // use forEach and setTimeout because you cannot use a loop and clock.sleep() in JavaScript
    setTimeout(function() {
        var rsvp_canvas = Canvas()
        rsvp_canvas.text({text:letter})
        var t = rsvp_canvas.show()
        t_list.push(t)
    }, delay)
    delay += 95
})
// END_RUN_PHASE
// END_EXAMPLE

// START_EXAMPLE: random functions
var randomLetter = random.pick(["a", "b", "c"])
var array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(array)  // shuffles in-place
var subArray = random.subArray(array, 4)  // randomly pick 4 elements
var randomColor = random.color()  // hex color
var randInt = random.integer(9, 0)  // max(inclusive), min
var randFloat = random.float(9, 0)  // limit, min
// END_EXAMPLE
