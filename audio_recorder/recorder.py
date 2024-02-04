import streamlit as st
from streamlit.components.v1 import html

def AudioRecorder():
    html_code = '''
    <body>
        <div class="black-background">
            <button onclick="startRecording()" class="btn">Start Recording</button>
            <button onclick="stopAndDownloadRecording()" class="btn">Stop and Download Recording</button>
            <button onclick="resetRecording()" class="btn">Reset Recording</button>
        </div>


    <style>
    body {
            background-color: #000000;
        }
        
    .btn {
        border: 0px solid #007BFF;
        padding: 10px 10px;
        cursor: pointer;
        border-radius: 25px;
        }
        
        .btn:hover {
        background-color: #99b8d4; 
        color: rgb(9, 10, 9);
        }
        
    </style>

    <script>
        let chunks = [];
        let recorder;
        let mediaStream;

        function startRecording() {
        // Reset chunks array to avoid appending previous recordings
        chunks = [];

        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
            mediaStream = stream;
            // Move recorder creation outside to avoid creating a new recorder each time
            recorder = new MediaRecorder(stream);
            recorder.start();
            recorder.ondataavailable = (event) => {
                chunks.push(event.data);
            };
            });
        }

        function stopAndDownloadRecording() {
        recorder.stop();
        
        recorder.onstop = ()=>{
        
        
        if (chunks.length > 0) {
            mediaStream.getAudioTracks()[0].stop();
            const blob = new Blob(chunks, { 'type': 'audio/wav' });
            const url = URL.createObjectURL(blob);
            
            const a = document.createElement('a');
            document.body.appendChild(a);
            a.style = 'display: none';
            a.href = url;
            a.download = 'audio-recording.wav';
            a.click();

            window.URL.revokeObjectURL(url);
        } else {
            console.warn("No audio data recorded.")
        }
        };
        }

        function resetRecording() {
        chunks = [];
        if (mediaStream) {
            mediaStream.getAudioTracks()[0].stop();
        }
        if (recorder) {
            recorder.stop();
        }
        }
    </script>
    </body>
    '''

    html(html_code, height=50)
