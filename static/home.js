window.onload = function () {
  // Enable the upload button once the page loads
  document.getElementById("uploadBtn").disabled = false;
};

function srcFileUpload() {
  console.log("uploading src file");
  var formData = new FormData();
  var fileInput = document.getElementById("fileUpload");

  // Check if a file is present
  if (fileInput && fileInput.files && fileInput.files.length > 0) {
    // Loop through the selected files and append them to FormData
    for (var i = 0; i < fileInput.files.length; i++) {
      var file = fileInput.files[i];
      console.log("file:", file); // Log each file object for debugging
      formData.append("srcFiles", file);
    }

    // Perform AJAX request to upload file
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/upload", true);
    console.log("uploading file ");

    xhr.onload = function () {
      if (xhr.status === 200) {
        console.log("success");
        displaySuccessDialog(
          "file-upload-msg",
          "File(s) uploaded successfully"
        );
        enableNextButton("validateSrcBtn");
        // Files uploaded successfully
      } else {
        // Error handling
        displayFailureDialog("file-upload-msg", "Error uploading file(s)");
      }
    };

    xhr.send(formData);
  } else {
    console.log("No file selected");
    displayFailureDialog("file-upload-msg", "Source File Required");
    return;
  }
}

function generateFiles() {
  console.log("generating files");

  var xhr = new XMLHttpRequest();

  // Specify the type of request (GET) and the relative URL (e.g., '/api/data')
  xhr.open("GET", "/generate", true);

  // Set up what happens when the request is done
  xhr.onload = function () {
    if (xhr.status == 200) {
      console.log("generate success");
      displaySuccessDialog(
        "generate-files-msg",
        "Templates generated successfully"
      );
    } else {
      console.log("generate Failed");
      displayFailureDialog("generate-files-msg", "Templates generation Failed");
    }
  };

  // Handle network errors
  xhr.onerror = function () {
    console.log("Request failed due to a network error.");
    displayFailureDialog(
      "generate-files-msg",
      "Request failed due to a network error."
    );
  };

  // Send the request
  xhr.send();
}

function validateSource() {
  console.log("checking source");

  // Perform AJAX request to upload file
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/validate", true);

  xhr.onload = function () {
    if (xhr.status === 200) {
      console.log("success");
      displaySuccessDialog("validate-source-msg", "Validation done");
      enableNextButton("prepareSrcBtn");
    } else {
      displayFailureDialog("validate-source-msg", "Source file(s) missing");
    }
  };

  xhr.send();
}

function prepareSource() {
  console.log("preparing source ");

  var xhr = new XMLHttpRequest();

  // Specify the type of request (GET) and the relative URL (e.g., '/api/data')
  xhr.open("GET", "/prepare", true);

  // Set up what happens when the request is done
  xhr.onload = function () {
    if (xhr.status == 200) {
      console.log("source preparation success");
      displaySuccessDialog(
        "prepare-source-msg",
        "Source prepared successfully"
      );
      enableNextButton("generateTemplateBtn");
    } else {
      console.log("source preparation Failed");
      displayFailureDialog("prepare-source-msg", "Source preparation Failed");
    }
  };

  // Send the request
  xhr.send();
}

function displaySuccessDialog(id, msg) {
  document.getElementById(id).style.display = "block";
  document.getElementById(id).innerHTML = msg;
  document.getElementById(id).style.color = "green";
}

function displayFailureDialog(id, msg) {
  document.getElementById(id).style.display = "block";
  document.getElementById(id).innerHTML = msg;
  document.getElementById(id).style.color = "red";
}

function enableNextButton(buttonId) {
  document.getElementById(buttonId).disabled = false;
}
