import React from 'react';

import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import LoginPage from './pages/loginPage';
import ArticlesPage from './pages/ArticlesPage';
import RegisterPage from './pages/RegisterPage';



function App() {
  return (
    <>
      <Router>
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<HomePage />}></Route>
          </Routes>

          <Routes>
            <Route path="/articles" element={<ArticlesPage />}/>
            <Route path="/login" element={<LoginPage />}/>
            <Route path="/register" element={<RegisterPage />}/>
          </Routes>
          <ToastContainer theme='dark'/>
        </main>
        
        <Footer />
      </Router>
      
    </>
  );
}

export default App;
