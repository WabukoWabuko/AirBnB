let isDetectionOn = false;
let recognition;

// Initialize Speech Recognition
function initSpeechRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.continuous = true;

    recognition.onresult = event => {
        const transcript = event.results[event.results.length - 1][0].transcript.trim().toLowerCase();
        console.log("Recognized:", transcript);
        
        // Emergency Keywords
        const emergencyKeywords = ['help', 'emergency', 'fire', 'danger'];
        if (emergencyKeywords.some(word => transcript.includes(word))) {
            sendEmergencyAlert(transcript);
        }
    };

    recognition.onerror = error => {
        console.error("Speech recognition error:", error);
    };
}

// Start Keyword Detection
function startDetection() {
    if (!recognition) initSpeechRecognition();
    recognition.start();
    document.getElementById('toggleEmergency').classList.remove('btn-outline-danger');
    document.getElementById('toggleEmergency').classList.add('btn-danger');
    document.getElementById('toggleEmergency').innerText = 'Disable Detection';
    console.log("Detection started.");
}

// Stop Keyword Detection
function stopDetection() {
    if (recognition) recognition.stop();
    document.getElementById('toggleEmergency').classList.remove('btn-danger');
    document.getElementById('toggleEmergency').classList.add('btn-outline-danger');
    document.getElementById('toggleEmergency').innerText = 'Enable Detection';
    console.log("Detection stopped.");
}

// Toggle Detection
document.getElementById('toggleEmergency').addEventListener('click', () => {
    isDetectionOn = !isDetectionOn;
    isDetectionOn ? startDetection() : stopDetection();
});

// Send Emergency Alert to Backend
function sendEmergencyAlert(transcript) {
    fetch('/api/emergency-alert/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ keyword: transcript, timestamp: new Date() }),
    })
    .then(response => response.json())
    .then(data => console.log("Emergency alert sent:", data))
    .catch(error => console.error("Error sending emergency alert:", error));
}
