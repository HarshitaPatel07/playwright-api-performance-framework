import test from "@playwright/test";
import { TEST_DATA } from "./data/testData";
import { LoginPage, ProductPage } from "../PageObjects";

test("Add to cart flow", async ({ page }) => {
  const loginPage = new LoginPage(page);
  const productPage = new ProductPage(page);
  const url = TEST_DATA.environment.sauceDemo.url;
  const user = TEST_DATA.users.validUser;
  const product = "Sauce Labs Bolt T-Shirt";

  await loginPage.goto(url);
  await loginPage.login(user.username, user.password);

  await productPage.addToCartFromDetailsPage(product);
});
