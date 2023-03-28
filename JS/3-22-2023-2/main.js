const ffi = require('ffi');

let user32 = ffi.library('user32', {

    'SetCursorPos':['long', ['long', 'long']]

});

user32.SetCursorPos(10,10);