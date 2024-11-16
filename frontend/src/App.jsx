import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

import { Publications } from "./components/Publications/Publications";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <Publications />
    </>
  );
}

export default App;
