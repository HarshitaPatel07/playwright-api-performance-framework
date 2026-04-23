import test from "@playwright/test";
import { TEST_DATA } from "./data/testData";
import { LoginPage } from "../PageObjects/login-page";

test("login flow", async ({ page }) => {
  const loginPage = new LoginPage(page);
  const url = TEST_DATA.environment.sauceDemo.url;
  const user = TEST_DATA.users.validUser;

  await loginPage.goto(url);
  await loginPage.login(user.username, user.password);
});
