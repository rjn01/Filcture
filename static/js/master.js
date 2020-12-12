function showUserImage(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (event) {
      let uploadedPictureContainer = document.getElementById('uploaded-picture-container');
      let uploadedPicture = document.getElementById('uploaded-picture');
      let pictureCaption = document.getElementById('picture-caption');
      uploadedPictureContainer.style.display = 'block';
      uploadedPicture.src = event.target.result;
      pictureCaption.textContent = 'Uploaded File:' + input.files[0].name;
    };

    reader.readAsDataURL(input.files[0]);
  }
}