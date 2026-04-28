import test from "@playwright/test";
import { TEST_DATA } from "./data/testData";
import { LoginPage, ProductPage } from "../PageObjects";

test("Checkout flow", async ({ page }) => {
  const loginPage = new LoginPage(page);
  const productPage = new ProductPage(page);
  const url = TEST_DATA.environment.sauceDemo.url;
  const user = TEST_DATA.users.validUser;
  const products = ["Sauce Labs Bolt T-Shirt", "Sauce Labs Bike Light"];

  await loginPage.goto(url);
  await loginPage.login(user.username, user.password);

  await productPage.checkout(products, {
    firstName: user.firstName,
    lastName: user.lastName,
    postalCode: user.postalCode,
  });
});
