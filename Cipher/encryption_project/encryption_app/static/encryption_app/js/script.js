
console.log('Ti it is ')
console.log(image)

function updateClock() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();

    // Ensure two digits for hours, minutes, and seconds
    hours = (hours < 10) ? '0' + hours : hours;
    minutes = (minutes < 10) ? '0' + minutes : minutes;
    seconds = (seconds < 10) ? '0' + seconds : seconds;

    var timeString = hours + ':' + minutes + ':' + seconds;
    document.getElementById('clock').textContent = timeString;
}

// Update the clock every second
setInterval(updateClock, 1000);

// Initial call to set the clock immediately
updateClock();


function copyText() {
    /* Get the text values */
    var text = document.getElementById('textValue').innerText;

    /* Create a temporary textarea to copy the text */
    var tempTextArea = document.createElement('textarea');
    tempTextArea.value =  text;
    document.body.appendChild(tempTextArea);

    /* Select the text in the textarea */
    tempTextArea.select();
    tempTextArea.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text to the clipboard */
    document.execCommand('copy');

    /* Remove the temporary textarea */
    document.body.removeChild(tempTextArea);

    /* Provide feedback to the user (optional) */
    alert('Text copied to clipboard:\nCipherText: ' + text);
}


function myFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }