const imageForm = document.getElementById("image-form");
const imageInput = document.getElementById("image-input");
const classifyButton = document.getElementById("classify-button");
const classificationResultDiv = document.getElementById("classification-result");
const modelName = document.getElementById("model-select");
const imagePreview = document.getElementById("image-preview");

// Add event listener for image input to display preview
imageInput.addEventListener("change", () => {
    const file = imageInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
            imagePreview.src = event.target.result;
            imagePreview.classList.remove("d-none"); // Show preview
        };
        reader.readAsDataURL(file);
    } else {
        imagePreview.src = "";
        imagePreview.classList.add("d-none"); // Hide preview
    }
});
// Fetch environment variables from the server
let host;

fetch('/env')
  .then(response => response.json())
  .then(data => {
    host = data.HOST;
  })
  .catch(error => console.error('Error fetching environment variables:', error));
classifyButton.addEventListener("click", async (e) => {
    e.preventDefault();

    // Get the selected model from the dropdown
    const selectedModel = modelName.value;

    // Validate the form inputs+
    if (!imageInput.files[0]) {
        classificationResultDiv.innerText = "Please select an image.";
        return;
    }

    if (selectedModel === "Select Model") {
        classificationResultDiv.innerText = "Please select a model.";
        return;
    }

    const imageData = new FormData();
    imageData.append("image", imageInput.files[0]);
    imageData.append("model", selectedModel); // Add the selected model to the request
    console.log('Other host: waah');
    try {
        const response = await fetch(`${host}/classify`, {
            method: "POST",
            body: imageData,
        });

        if (!response.ok) {
            throw new Error("Failed to classify the image.");
        }

        const classificationResult = await response.json();
        classificationResultDiv.innerText = `Classification result: ${classificationResult.message}`;
    } catch (error) {
        console.error("Error sending request:", error);
        classificationResultDiv.innerText = "An error occurred during classification." + error;
    }
});