import { Header } from "./components/Header/Header";
import { Main } from "./components/Main";
import { Footer } from "./components/Footer";
import { Navigation } from "./components/Navigation/Navigation";
import { Link } from "./components/Link/Link";

import { render } from "./core/render";

import "./public/styles/style.css";

const main = new Main({
  tagName: "main",
  className: "main",
}).toHTML();

const footer = new Footer({
  tagName: "footer",
  className: "footer",
}).toHTML();

const links = [
  new Link({
    text: "Users",
    className: "nav-link",
    events: {
      click: () => fetchData(main, "/users"),
    },
  }).toHTML(),

  new Link({
    text: "Products",
    className: "nav-link",
    events: {
      click: () => fetchData(main, "/products"),
    },
  }).toHTML(),
];

const nav = new Navigation({}).toHTML();

nav.append(...links);

const header = new Header({}).toHTML();

header.append(nav);

async function fetchData(main, path) {
  const data = await fetch(`http://127.0.0.1:3333/${path}`);
  const parsedData = await data.json();

  const domArr = await parsedData.map((el) => {
    console.log(parsedData);
    const entries = Object.entries(el);

    return `
        <div class="card">
          ${entries.map((el) => {
            if (el[0] !== "_id") {
              return `<h2>${el[0]} : ${el[1]}</h2>`;
            }
          })}
        </div>
        `;
  });

  main.insertAdjacentHTML("afterbegin", domArr.toString().replaceAll(",", " "));
}

render("#app", [header, main, footer]);
