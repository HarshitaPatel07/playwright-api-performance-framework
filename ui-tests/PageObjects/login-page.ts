import { expect, Page } from "@playwright/test";

export class LoginPage {
  readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async goto(url: string) {
    await this.page.goto(url);
  }

  async login(username: string, password: string) {
    await this.page.locator('input[name="user-name"]').fill(username);
    await this.page.locator('input[name="password"]').fill(password);
    await this.page.getByRole("button", { name: "Login" }).click();
    await expect(this.page.locator('div[class="app_logo"]')).toHaveText(
      "Swag Labs",
    );
  }
}
