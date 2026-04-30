
import React, { useRef } from "react";
import axios from "axios";

export default function Home() {
  const videoRef = useRef(null);

  const start = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoRef.current.srcObject = stream;
  };

  const send = async () => {
    const canvas = document.createElement("canvas");
    const video = videoRef.current;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0);

    const blob = await new Promise(res => canvas.toBlob(res));

    const form = new FormData();
    form.append("file", blob);

    const res = await axios.post("http://localhost:8000/infer", form);
    console.log(res.data);
  };

  return (
    <div>
      <video ref={videoRef} autoPlay />
      <button onClick={start}>Start</button>
      <button onClick={send}>Infer</button>
    </div>
  );
}
