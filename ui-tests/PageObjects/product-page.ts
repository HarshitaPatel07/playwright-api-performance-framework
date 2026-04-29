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

  async addToCart(products: string[]) {
    for (const product of products) {
      const item = this.page
        .locator('[data-test="inventory-item"]')
        .filter({ hasText: product });
      await item.getByRole("button", { name: "Add to cart" }).click();
    }
  }

  async addToCartFromDetailsPage(product: string) {
    await this.page
      .locator('[data-test="inventory-item-name"]')
      .filter({ hasText: product })
      .click();

    await this.page.getByRole("button", { name: "Add to cart" }).click();

    await expect(
      this.page.getByRole("button", { name: "Remove" }),
    ).toBeVisible();
  }

  async checkout(userDetails: {
    firstName: string;
    lastName: string;
    postalCode: string;
  }) {
    await this.page.locator('[data-test="shopping-cart-link"]').click();

    await this.page.locator('[data-test="checkout"]').click();
    await this.page
      .locator('[data-test="firstName"]')
      .fill(userDetails.firstName);
    await this.page
      .locator('[data-test="lastName"]')
      .fill(userDetails.lastName);
    await this.page
      .locator('[data-test="postalCode"]')
      .fill(userDetails.postalCode);
    await this.page.locator('[data-test="continue"]').click();
    await this.page.locator('[data-test="finish"]').click();
    await expect(
      this.page.locator('[data-test="complete-header"]'),
    ).toContainText("Thank you for your order!");
  }
}
