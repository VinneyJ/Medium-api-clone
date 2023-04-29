import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'


function Footer() {
  return (
    <footer>
        <Container>
            <Row>
                <Col className='py-3'>
                    Copyright &copy; PenHouse {new Date().getFullYear()}
                </Col>
            </Row>
        </Container>
    </footer>

  )
}

export default Footer

