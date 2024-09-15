let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    // Create an XMLHttpRequest object
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            let response = JSON.parse(this.responseText);
            if (this.status == 200) {
                // Display the message from a successful response
                document.getElementById("system_response").innerHTML = response.message;
            } else {
                // Handle error responses
                document.getElementById("system_response").innerHTML = response.message || "An error occurred. Please try again.";
            }
        }
    };

    // Open the request as POST and set the Content-Type to JSON
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Send the text to analyze in JSON format
    xhttp.send(JSON.stringify({ statement: textToAnalyze }));
}
