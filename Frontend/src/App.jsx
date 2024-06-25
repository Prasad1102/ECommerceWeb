import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./Pages/Home";
import Layout from "./Pages/Layout";
import Login from "./Pages/User/Login";
import Reister from "./Pages/User/Reister";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="login" element={<Login />} />
          <Route path="reg" element={<Login />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
