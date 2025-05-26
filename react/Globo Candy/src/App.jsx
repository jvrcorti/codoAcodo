import { Container, Carousel } from "react-bootstrap";
import Navbar from "./components/navbar";
import Footer from "./components/footer";
import ProductList from "./components/products"

function App() {
  return (
    <div>
    <Navbar/>
    <ProductList/>
    <Footer/>
    </div>
  );
}

export default App
