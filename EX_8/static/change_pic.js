const button = document.getElementById('btn-change-image');
const image = document.getElementById('myPic');
if (button !== null) button.addEventListener('click', changeImage);

function changeImage() {
  if (image.classList.contains('box-out') || image.classList.length === 0) {
    image.classList.remove('box-out');
    image.classList.add('box-in');
    image.src = 'static/maya_happy.jpeg';

    button.textContent = '🙂 Make Maya Happy   🙂';
  } else {
    image.classList.remove('box-in');
    image.classList.add('box-out');
    image.src = 'static/maya_picture.jpeg';

    button.textContent = '😁 Make Maya Happier 😁';
  }
}

function sendForm() {
  // get form container element
  const beforeComplete = document.getElementById('beforeComplete');
  const afterComplete = document.getElementById('afterComplete');
  beforeComplete.style.display = 'none';
  afterComplete.style.display = 'block';
  return false;
}

// sending to home page.
function goBack() {
  window.location = '/';
}