import React from 'react';

import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import LoginPage from './pages/loginPage';
import ArticlesPage from './pages/ArticlesPage';



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
          </Routes>
          
        </main>
        <ToastContainer theme='dark'/>
        <Footer />
      </Router>
      
    </>
  );
}

export default App;
