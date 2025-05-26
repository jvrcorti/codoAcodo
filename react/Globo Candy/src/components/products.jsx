import React from "react";
import { Row, Col, Button, Card } from "react-bootstrap";

const products = [
  { id: 1, name: "Golosina 1", price: 1500, image: "" },
  { id: 2, name: "Golosina 2", price: 2200.50, image: "" },
  { id: 3, name: "Chocolate", price: 2.509, image: "" }
];

function ProductList(props) {
  return (
    <Row>
      {products.map((product) => (
        <Col key={product.id} md={4} className="mb-4">
          <Card>
            <Card.Img variant="top" src={product.image} />
            <Card.Body>
              <Card.Title>{product.name}</Card.Title>
              <Card.Text>Precio: ${product.price}</Card.Text>
              <Button variant="primary" onClick={() => props.onAddToCart(product)}>
                Agregar al carrito
              </Button>
            </Card.Body>
          </Card>
        </Col>
      ))}
    </Row>
  );
}

export default ProductList
