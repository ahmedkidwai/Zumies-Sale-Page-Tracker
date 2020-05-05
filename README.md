# Zumies Sales Tracker

> An Easy to use sales page tracker for the Zumies e-commerce store

> Created because I got tired of missing sales on longboards/cruisers 🛹

### What is it?
Zumies Sales Tracker (ZST) allows users to enter product information along with a page to scrape. In the event a matching SKU is found, ZST will email the user to inform them. The application scrapes the user provided URL every 10 minutes.

### Setup

The Zumies Sale Tracker (ZST) requires users email credentials to send off emails. ZST checks environement variables for email addresses and passwords. App specific passwords are still recommended - Instructions for [Gmail Users](https://support.google.com/accounts/answer/185833?hl=en)

#### Shell Profile Updates
Add the following lines to your .zshrc or .bash_profile
```
export EMAIL="email@email.com"
```
```
export PASSWORD="app-specific-password"
```
Restart your shell after updating.

### Running ZST
Navigate to the src folder and run:
`$  python3 Zumies_Sale_Tracker`
Fill in the required prompts.
> Product Name: This is an identifier used to email the user a product SKU has been found.

> SKU: The SKU is the unique product identifer the application uses to check if a product is on sale.

> Sales Page URL: Navigate to the section your product is found (example: Sale > Skateboards > Cruisers Completes) and copy the URL. The application will scan this page for products.

> Email: This is the email you want to receive updates to.
