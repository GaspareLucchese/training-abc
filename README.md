# Real Estate Odoo Module

## 📌 Overview
This repository contains a custom **Odoo 18.0 module** developed during my internship at **ABC S.R.L.** as a training project.  
The module introduces a **real estate management system** inside Odoo, enabling the creation, management, and selling of properties with offers, tags, and property types.

The goal of this project was to get hands-on experience with Odoo development, including:
- Creating custom models.
- Defining views and menus.
- Implementing business logic with Python.
- Managing security and access rights.

---

## ✨ Features
- **Property Management**  
  Create, update, and manage real estate properties with details such as area, garden, orientation, price, and state.
  
- **Offers Workflow**  
  Submit, accept, or refuse offers for properties with automatic updates on property status.
  
- **Property Types & Tags**  
  Organize properties using categories (types) and labels (tags).  
  Each property type automatically generates a related tag.

- **Business Rules & Constraints**  
  - Only properties in certain states can be deleted.  
  - Expected and selling prices must be positive.  
  - Selling price must respect minimum thresholds.  
  - Deadlines for offers are automatically computed.  

- **User Integration**  
  Properties are linked to Odoo users (salesmen) and buyers.
  
---

[✍️ This README was written with the assistance of ChatGPT]
