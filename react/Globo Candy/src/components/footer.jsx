import React from "react";

function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="bg-dark text-white text-center py-3 mt-4">
      Globo Candy © {year}. Todos los derechos reservados.
    </footer>
  );
}

export default Footer;
