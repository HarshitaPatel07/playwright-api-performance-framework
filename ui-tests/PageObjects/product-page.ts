import { expect, Page } from "@playwright/test";

export class ProductPage {
  readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async viewProductDetails(productName: string) {
    await this.page
      .locator('[data-test="inventory-item-name"]')
      .filter({ hasText: productName })
      .click();

    await expect(
      this.page.locator('[data-test="inventory-item-name"]'),
    ).toHaveText(productName);
    await expect(
      this.page.locator('[data-test="inventory-item-desc"]'),
    ).toBeVisible();
    await expect(
      this.page.locator('[data-test="inventory-item-price"]'),
    ).toBeVisible();
    await expect(
      this.page.getByRole("button", { name: "Add to cart" }),
    ).toBeVisible();
    await expect(
      this.page.getByRole("button", { name: "Back to products" }),
    ).toBeVisible();
  }
}
