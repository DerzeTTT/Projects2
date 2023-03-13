const { createCanvas } = require('canvas');

// set up canvas
const canvasWidth = 400;
const canvasHeight = 400;
const canvas = createCanvas(canvasWidth, canvasHeight);
const ctx = canvas.getContext('2d');

// draw stickman
ctx.beginPath();
ctx.arc(200, 100, 40, 0, Math.PI * 2); // head
ctx.moveTo(200, 140); // neck
ctx.lineTo(200, 240); // body
ctx.lineTo(150, 290); // left leg
ctx.moveTo(200, 240); // body
ctx.lineTo(250, 290); // right leg
ctx.moveTo(200, 180); // left arm
ctx.lineTo(150, 200); // left forearm
ctx.moveTo(200, 180); // right arm
ctx.lineTo(250, 200); // right forearm
ctx.stroke();

// save canvas to file
const fs = require('fs');
const out = fs.createWriteStream(__dirname + '/stickman.png');
const stream = canvas.createPNGStream();
stream.pipe(out);
out.on('finish', () => console.log('Stickman saved as stickman.png'));
