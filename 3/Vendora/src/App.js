import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import CartPage from './pages/CartPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/cart" element={<CartPage />} />
        {/* Add other routes here */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;