import { useState } from "react";
import axios from "axios";

function App() {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");

  // NEW STATES
  const [timestamp, setTimestamp] = useState(null);

  const [mediaFile, setMediaFile] = useState("");

  // ASK QUESTION
  const askQuestion = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question: question
        }
      );

      setAnswer(response.data.answer);

    } catch (error) {

      console.log(error);

      alert("Error connecting to backend");
    }
  };

  // GENERATE SUMMARY
  const generateSummary = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/summary"
      );

      setSummary(
        response.data.summary
      );

    } catch (error) {

      console.log(error);

      alert("Summary generation failed");
    }
  };

  // GET TIMESTAMP
  const getTimestamp = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/timestamps"
      );

      setTimestamp(
        response.data.start
      );

      setMediaFile(
        "http://127.0.0.1:8000/" +
        response.data.file
      );

    } catch (error) {

      console.log(error);

      alert("Timestamp fetch failed");
    }
  };

  // UPLOAD FILE
  const uploadFile = async () => {

    if (!file) {

      alert("Select a file first");

      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      alert(response.data.message);

    } catch (error) {

      console.log(error);

      alert("Upload failed");
    }
  };

  return (

    <div
      style={{
        padding: "40px",
        fontFamily: "Arial",
        backgroundColor: "#0b1020",
        minHeight: "100vh",
        color: "white",
        textAlign: "center"
      }}
    >

      <h1>
        AI Multimedia Q&A System
      </h1>

      <input
        type="file"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
      />

      <br /><br />

      <button onClick={uploadFile}>
        Upload File
      </button>

      <br /><br />

      <textarea
        rows="4"
        cols="50"
        placeholder="Ask something..."
        value={question}
        onChange={(e) =>
          setQuestion(e.target.value)
        }
      />

      <br /><br />

      <button onClick={askQuestion}>
        Ask AI
      </button>

      <button
        onClick={generateSummary}
        style={{
          marginLeft: "10px"
        }}
      >
        Generate Summary
      </button>

      <button
        onClick={getTimestamp}
        style={{
          marginLeft: "10px"
        }}
      >
        Get Timestamp
      </button>

      <h2>Answer:</h2>

      <p>{answer}</p>

      <h2>Summary:</h2>

      <p>{summary}</p>

      <h2>Media Player:</h2>

      {
        mediaFile && (

          <video
            width="600"
            controls
            src={mediaFile}
            onLoadedMetadata={(e) => {

              if (timestamp !== null) {

                e.target.currentTime = timestamp;
              }
            }}
          />
        )
      }

    </div>
  );
}

export default App; 