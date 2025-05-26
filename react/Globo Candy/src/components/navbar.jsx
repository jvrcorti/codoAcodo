import React from "react";
import { Container, Navbar, Nav } from "react-bootstrap";

function NavBar({ cartCount }) {
  return (
    <Navbar bg="dark" variant="dark" expand="lg">
      <Container>
        <Navbar.Brand href="#Home">Globo Candy</Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link href="#Inicio">Inicio</Nav.Link>
          <Nav.Link href="#Articulos">Artículos</Nav.Link>
          <Nav.Link href="#Consultas">Consultas</Nav.Link>
        </Nav>
        <Navbar.Text>🛒 {cartCount}</Navbar.Text>
      </Container>
    </Navbar>
  );
}

export default NavBar