import { Header } from "./components/Header/Header";
import { Main } from "./components/Main";
import { Footer } from "./components/Footer";

import { render } from "./core/render";
import { getData } from "./utils/getData";

import "./public/styles/style.css";

// let isLoading = true;
const products = [];

const header = new Header({
  tagName: "header",
  className: "header",
  children: "<h2>Logo</h2>",
}).toHTML();

const data = getData("http://127.0.0.1:3333/products", products);

const main = new Main({
  tagName: "main",
  className: "main",
  // children: isLoading ? "..." : products,
}).toHTML();

const footer = new Footer({
  tagName: "footer",
  className: "footer",
}).toHTML();

render("#app", [header, main, footer]);
