const body = document.querySelector("body");
const video = document.querySelector("#video");
const playButton = document.querySelector("#play-button");
const playIcon = document.querySelector("#play-icon");
const configButton = document.querySelector("#config-button");
const configTempoButton = document.querySelector("#config-tempo-button");
const volumeInput = document.querySelector("#volume-input");
const watchProgress = document.querySelector("#watch-progress");
const currentTimeElement = document.querySelector("#current-time");
const durationTimeElement = document.querySelector("#duration-time");
const configPopup = document.querySelector("#popup-config");
const tempoPopup = document.querySelector("#popup-tempo");
const popupTempoOptionElements = document.querySelectorAll(
  "#popup-tempo .option"
);
const barWrapperElement = document.querySelector("#bar-wrapper");

function videoFactory(){

  let videoObj = new Object();
  videoObj.playing = false;

  videoObj.onPlay = () => {

    playIcon.src = !videoObj.playing ? playIcon.src = './assets/play.svg' : './assets/pause.svg';

  };

  videoObj.effects = {

    [false]:() => {

      videoObj.assigned.play();

    },

    [true]:() => {

      if (!videoObj.assigned.ended){

        videoObj.assigned.pause();

      } else {

        videoObj.playing = true;
        videoObj.assigned.play();

        videoObj.onPlay();

      };

    }

  };

  videoObj.play = () => {

    videoObj.effects[videoObj.playing]();
    videoObj.playing = !videoObj.playing;

    videoObj.onPlay();

  };

  return videoObj;

};

let newVid = videoFactory();
newVid.assigned = video;

playIcon.addEventListener('click', newVid.play);
newVid.assigned.addEventListener('click', newVid.play);

document.body.addEventListener('onkeydown', (rawKey) => {

  if (rawKey.code !== 'Space'){return};

  rawKey.preventDefault();
  newVid.play();

});

function processZeros(roundedStamp){

  return (roundedStamp < 10 ? `0${roundedStamp}` : roundedStamp);

}

function formatVideoTime(s){

  const mins = Math.floor((s % (60 * 60)) / 60);
  const seconds = Math.ceil(s % (60 * 60) % 60);
  
  const processedMins = processZeros(mins);
  const processedSecs = processZeros(seconds);

  return `${processedMins}:${processedSecs}`;

}

newVid.assigned.addEventListener('ended', () => {

  newVid.playing = false;

});

function updateVidTime(){

  const curTime = newVid.assigned.currentTime;
  const endTime = newVid.assigned.duration;

  currentTimeElement.innerText = formatVideoTime(curTime);
  durationTimeElement.innerText = formatVideoTime(endTime);

}

newVid.assigned.addEventListener('loadeddata', (elem) => {

  if (elem.readyState >= 4){

    updateVidTime();

  };

})

updateVidTime();

newVid.assigned.addEventListener('timeupdate', () => {

  updateVidTime();

  const vidProgress = (curTime - endTime) * 100;

  watchProgress.style.width = `${vidProgress}%`

})