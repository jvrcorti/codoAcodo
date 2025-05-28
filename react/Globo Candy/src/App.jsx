import { Container, Carousel } from "react-bootstrap";
import Navbar from "./components/navbar";
import Footer from "./components/footer";
import ProductList from "./components/products"
import Cart from "./components/cart"

function App() {
  return (
    <>
    <Navbar/>
    <ProductList/>
    <Footer/>
    </>
  );
}

export default App
