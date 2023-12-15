
function toggleField() {
    //setganoraphy on 
    var imgField = document.getElementById('image');
    var textField = document.getElementById('text')
    var cardTitle = document.getElementById('title-msg')
    var type = document.getElementById('type')
    type.value='stegano'
    cardTitle.textContent='Success Stegenography'
    imgField.style.display= 'block'
    textField.style.display='block'

}
function hideText(){
    //image field on 
    var textfield = document.getElementById('text')
    var imgField = document.getElementById('image')
    var cardTitle = document.getElementById('title-msg')
    var type = document.getElementById('type')
    type.value='image'

    cardTitle.textContent='Image Encyption'
    imgField.style.display='block'
    textfield.style.display='none'
}
function hideImage(){
    //text filed on 
    var field = document.getElementById('image');
    var cardTitle = document.getElementById('title-msg')
    var type = document.getElementById('type')
    type.value='text'
    cardTitle.textContent='Text Encryption'
    field.style.display='none'
    
}
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
