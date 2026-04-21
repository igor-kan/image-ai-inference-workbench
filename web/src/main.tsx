import React, { createContext, useContext, useEffect, useMemo, useState } from "react";
import { createRoot } from "react-dom/client";

type RuntimeState = { status: string };
const RuntimeContext = createContext<RuntimeState>({ status: "unknown" });

const App = () => {
  const [status, setStatus] = useState("loading");

  useEffect(() => {
    fetch("http://localhost:8100/api/runtime")
      .then((res) => res.json())
      .then((data) => setStatus(`TF:${data.tensorflow ? "yes" : "no"} | Torch:${data.pytorch ? "yes" : "no"}`))
      .catch(() => setStatus("runtime check failed"));
  }, []);

  const value = useMemo(() => ({ status }), [status]);

  return (
    <RuntimeContext.Provider value={value}>
      <Dashboard />
    </RuntimeContext.Provider>
  );
};

const Dashboard = () => {
  const runtime = useContext(RuntimeContext);
  return (
    <main style={{ fontFamily: "sans-serif", margin: "2rem auto", maxWidth: 680 }}>
      <h1>Image AI Inference Workbench</h1>
      <p>Runtime: {runtime.status}</p>
      <p>Use this app to demonstrate React hooks/context + FastAPI image/ML backend.</p>
    </main>
  );
};

createRoot(document.getElementById("root")!).render(<App />);
