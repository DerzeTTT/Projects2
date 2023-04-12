const add = document.getElementById("add");
const sub = document.getElementById("sub");

const count = document.getElementById("number");

let currentNum = 0;

function updateColor(rgbStr){

    count.style.color = `rgb(${rgbStr})`;

}

function incrementClicked(btnType){

    const incrementAmount = btnType == "add" ? 1 : -1;

    if (Math.abs(currentNum + incrementAmount) > 10){
        
        alert("reached maximum amount (-10 or 10)");
        return;

    };

    currentNum += incrementAmount;

    count.innerText = String(currentNum);

    if (currentNum > 5){updateColor("0,255,0")}
    else if (currentNum < 0){updateColor("255,0,0")}
    else {updateColor("0,0,0")}

};

add.onclick = () => {incrementClicked("add")};
sub.onclick = () => {incrementClicked("sub")};

count.innerText = String(currentNum);