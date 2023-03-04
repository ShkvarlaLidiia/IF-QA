import { Component } from "./core/Component";
import { render } from "./core/render";

const app = document.querySelector("#app");

const root = render(
  new Component({
    tagName: "header",
    className: "root",
    children: `<h2>Logo</h2>`,
    events: async (e) => {
      const data = await fetch("http://127.0.0.1:3333/");
      const parsedData = await data.json();

      console.log(parsedData);
    },
    id: 4,
  })
);

app.append(root);
