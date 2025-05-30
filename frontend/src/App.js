import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import UploadPage from './pages/UploadPage';

function App() {
  return (
    <Router>
      <Routes>
        {/* 이후 추가될 페이지들도 여기에 연결 */}
        <Route path="/" element={<Dashboard />} />
        <Route path="/upload" element={<UploadPage />} />
        
      </Routes>
    </Router>
  );
}

export default App;
