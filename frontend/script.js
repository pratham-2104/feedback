async function analyzeFeedback() {
    let feedback = document.getElementById("feedback").value;
    let resultDiv = document.getElementById("result");

    let response = await fetch("/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ feedback: feedback })
    });

    let data = await response.json();
    resultDiv.innerText = "Sentiment: " + data.sentiment;
}
