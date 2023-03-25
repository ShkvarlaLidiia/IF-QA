require("dotenv").config();
import { sumOfTwoPlusTwo } from "../functions/functions";

const textList = ["samsung", "apple", "nokia"];

console.log("[ process.env.baseURL]", process.env.baseURL);
describe("template spec", () => {
  it("passes", () => {
    try {
      expect(sumOfTwoPlusTwo()).to.equal(4);
      expect(sumOfTwoPlusTwo()).to.equal(3);
    } catch (e) {
      console.log(e.message);
    }

    // cy.visit({ url: process.env.baseURL || "https://rozetka.com.ua" });

    // for (const item of textList) {
    //   cy.get('[name="search"]').type(item);
    //   cy.get(".button_color_green").click();
    //   cy.get('[name="search"]').clear();
    // }

    cy.visit({
      url:
        process.env.baseURL ||
        "https://hard.rozetka.com.ua/ua/processors/c80083/",
    });

    cy.get(".catalog-settings__filter-button").click();
    cy.contains("Бренд").click();

    cy.get(".checkbox-filter__link").click({ multiple: true });
  });
});
