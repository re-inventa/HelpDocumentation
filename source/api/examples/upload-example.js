// upload-example.js
const axios = require('axios').default;
const fs = require('fs');
const FormData = require('form-data');

async function uploadFile(filePath, containerName, azureToken) {
    try {
        // Create a form data object and append the file to upload
        const formData = new FormData();
        formData.append('file', fs.createReadStream(filePath));

        // Set the headers for the request, including the container-name and azure-token
        const headers = {
            ...formData.getHeaders(),
            'container-name': containerName,
            'azure-token': azureToken,
        };

        // Make the POST request to the server to upload the file
        const response = await axios.post('http://localhost:3000/api/upload', formData, { headers });

        // Handle the response from the server
        console.log('File uploaded successfully:', response.data);
    } catch (error) {
        // Handle any errors that occur during the upload process
        if (error.response) {
            console.error('Failed to upload file:', error.response.status, error.response.data);
        } else {
            console.error('Error uploading file:', error.message);
        }
    }
}

// Example usage of the uploadFile function
// Replace 'path/to/file.txt' with the actual file path
// Replace 'your-container-name' with your actual Azure container name
// Replace 'your-azure-sas-token' with your actual Azure SAS token
uploadFile('path/to/file.txt', 'your-container-name', 'your-azure-sas-token');
