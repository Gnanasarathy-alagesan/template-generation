function srcFileUpload() {

    console.log("uploading src file")
      var formData = new FormData();
      var fileInput = document.getElementById('fileUpload');

      // Check if a file is present 
      if (fileInput.files.length > 0) {
          var file = fileInput.files[0];
          formData.append('srcFile', file);
  
          // Perform AJAX request to upload file
          var xhr = new XMLHttpRequest();
          xhr.open('POST', '/upload', true);
          console.log("uploading file ")
  
          xhr.onload = function() {
              if (xhr.status === 200) {
                console.log("success")
                displaySuccessDialog("system-config-msg", "File uploaded successfully")
                  // File uploaded successfully, you can handle the response here
              } else {
                  // Error handling
                  displayFailureDialog("system-config-msg", "Error uploading file")
              }
          };
  
          xhr.send(formData)
  
      } else {
          console.log('No file selected');
          displayFailureDialog("system-config-msg", "Source File Required")
          return;
      }
    }

function displaySuccessDialog(id, msg){
    document.getElementById(id).style.display = "block";
    document.getElementById(id).innerHTML = msg
    document.getElementById(id).style.color = "green";
    }

function displayFailureDialog(id, msg){
    document.getElementById(id).style.display = "block";
    document.getElementById(id).innerHTML = msg;
    document.getElementById(id).style.color = "red";
    }