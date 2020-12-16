function showUserImage(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (event) {
      let uploadedPictureContainer = document.getElementById('uploaded-picture-container');
      let uploadedPicture = document.getElementById('uploaded-picture');
      let filteredPictureContainer = document.getElementById('filtered-picture-container');
      let pictureCaption = document.getElementById('picture-caption');
      if (filteredPictureContainer) {
        filteredPictureContainer.style.display = 'none';
      }
      uploadedPictureContainer.style.display = 'flex';
      uploadedPicture.src = event.target.result;
      pictureCaption.textContent = 'Original Image:' + input.files[0].name;
    };

    reader.readAsDataURL(input.files[0]);
  }
}