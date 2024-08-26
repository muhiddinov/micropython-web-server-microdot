function toggleButtonSwitch(e) {
  var switchButton = document.getElementById("switch");
  
  var toggleValue = "";
  if (switchButton.checked) {
    console.log("On!");
    toggleValue = "ON";
  } else {
    console.log("Off!");
    toggleValue = "OFF"
  }
  fetch( `/toggle`)
  .then( response => {
    console.log(response);
  } )
}

const controller = document.querySelector('input[type=range]');
const radialProgress = document.querySelector('.RadialProgress');

const setProgress = (progress) => {
  const value = `${progress}%`;
  radialProgress.style.setProperty('--progress', value)
  radialProgress.innerHTML = value
  fetch('/pwm?' + new URLSearchParams({
      'pwm_value': value
  } ).toString()).then( response => {
      console.log(response);
  } )
  radialProgress.setAttribute('aria-valuenow', value)
}

setProgress(controller.value)
controller.oninput = () => {
  setProgress(controller.value)
}