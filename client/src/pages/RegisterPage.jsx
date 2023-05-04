import React, {useState, useEffect} from "react";
import {Button,Col, Container, Form, Row} from 'react-bootstrap';
import {FaSignInAlt} from 'react-icons/fa';
import { useDispatch, useSelector } from 'react-redux';
import { Link,  useNavigate} from 'react-router-dom'; //useLocation,
import { toast } from 'react-toastify';
import Spinner from "../components/Spinner";
//import Title from '../components/Title';
import {login, register, reset} from '../features/auth/authSlice';

const RegisterPage = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [first_name, setFirst_name] = useState("");
  const [last_name, setLast_name] = useState("");
  const [password, setPassword] = useState("");
  const [re_password, setRe_passwword] = useState("");

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const {user, isLoading, isError, isSuccess, message} = useSelector((state)=> state.auth);

  useEffect(() => {
    if (isError) {
        toast.error(message)
    }

    if (isSuccess || user) {
        navigate("/articles")
    }

    dispatch(reset());
  }, [isError, isSuccess, message, user, navigate, dispatch]);

  const submitHandler = (e) => {
    e.preventDefault()

    if (!username) {
        toast.error("A username must be provided!")
    }
    if (!email) {
      toast.error("An email must be provided!")
    }
    if (!first_name) {
        toast.error("A first name must be provided!")
    }
    if (!last_name) {
        toast.error("A last name must be provided!")
    }


    if (!password) {
        toast.error("A password must be provided!")
    }

    if (password !== re_password) {
        toast.error("Passwords do not match!")
    }
     
    const userData = {
      email, username, first_name, last_name, password, re_password //Check if this is correct
    };

    dispatch(register(userData));
  }


  
  return (
    <div>RegisterPage</div>
  )
}

export default RegisterPage