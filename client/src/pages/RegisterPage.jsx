import React, {useState, useEffect} from "react";
import {Button,Col, Container, Form, Row} from 'react-bootstrap';
import {FaUserAlt} from 'react-icons/fa';
import { useDispatch, useSelector } from 'react-redux';
import { Link,  useNavigate} from 'react-router-dom'; //useLocation,
import { toast } from 'react-toastify';
import Spinner from "../components/Spinner";
//import Title from '../components/Title';
import {register, reset} from '../features/auth/authSlice';

const RegisterPage = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [first_name, setFirst_name] = useState("");
  const [last_name, setLast_name] = useState("");
  const [password, setPassword] = useState("");
  const [re_password, setRepassword] = useState("");

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const {user, isLoading, isError, isSuccess, message} = useSelector((state)=> state.auth);

  useEffect(() => {
    if (isError) {
        toast.error(message)
    }

    if (isSuccess || user) {
        navigate("/")
        toast.success("An activation email has been sent to your email address. Please activate your account.")
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
      username, email, first_name, last_name, password, re_password, //Check if this is correct
    };

    dispatch(register(userData));
  }


  
  return (
    <>
      <Container>
        <Row>
            <Col className="mg-top text-center">
                <section>
                    <h1>
                        <FaUserAlt/> Sign In
                    </h1>
                    <hr className="hr-text"/>
                </section>
            </Col>
        </Row>
        {isLoading && <Spinner/>}
        <Row className="mt-3">
            <Col className="justtify-content-center">
                <Form className="mx-auto" onSubmit={submitHandler}>
                    <Form.Group  controlId="username">
                            <Form.Label>Username</Form.Label>
                            <Form.Control type="text" placeholder="Enter Username" value={username} onChange={(e)=>setUsername(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="email">
                        <Form.Label>Email Address</Form.Label>
                        <Form.Control type="email" placeholder="Enter Email" value={email} onChange={(e)=>setEmail(e.target.value)}/>
                    </Form.Group>

                    <Form.Group controlId="first_name">
                        <Form.Label>First Name</Form.Label>
                        <Form.Control type="text" placeholder="Enter First Name" value={first_name} onChange={(e)=>setFirst_name(e.target.value)}/>
                    </Form.Group>

                    <Form.Group controlId="last_name">
                        <Form.Label>Last Name</Form.Label>
                        <Form.Control type="text" placeholder="Enter Last Name" value={last_name} onChange={(e)=>setLast_name(e.target.value)}/>
                    </Form.Group>

                    <Form.Group controlId="password">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Enter Password" value={password} onChange={(e)=>setPassword(e.target.value)}/>
                    </Form.Group>

                    <Form.Group controlId="re_password">
                        <Form.Label>Confirm Password</Form.Label>
                        <Form.Control type="password" placeholder="Confirm Password" value={re_password} onChange={(e)=>setRepassword(e.target.value)}/>
                    </Form.Group>

                    <Button type="submit" variant="primary" className="mt-3">
                        Sign In
                    </Button>
                </Form>
            </Col>
        </Row>
        <Row className="py-3">
            <Col>
                Already a user?
                <Link to="/register">Login</Link>
            </Col>
        </Row>
      </Container>
    </>
  )
}

export default RegisterPage;