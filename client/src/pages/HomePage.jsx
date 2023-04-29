import React from 'react'
import {Button, Container} from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'


function Homepage() {
  return (
    <>
      <header className='masthead main-bg-image'>
        <Container className='px-4 px-lg-5 d-flex h-100 align-items-center justify-content-start'>
          
          <div className='d-flex justify-content-center'>
            <div className="text-center">
              <h1 className="mx-1 my-0 text-uppercase">
                
                <strong>Stay curious.</strong>
              </h1>
              <h2 className="text-white-50 mx-auto mt-2 mb-5">
                Discover stories, thinking, and expertise from writers on any topic. 
              </h2>
              <LinkContainer to='/articles'>
                <Button variant="dark" className='rounded-pill'>Start Reading</Button>
              </LinkContainer>
            </div>
          </div>
        </Container>

      </header>
    </>
  )
}

export default Homepage
