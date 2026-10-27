# Restaurant Food Ordering and Sales System

![Lead Developer Banner](banner.png)

A Python-based restaurant management application developed for the First Semester Project-Based Learning (PBL) course (PCS154). The system manages menu categories, processes customer orders, generates bills with persistent text file storage, and visualizes sales insights using Matplotlib.

---

## Team & Contributions (Section B)

| Student Name | University Roll No. | Class Roll No. | Role | Phase 1 & Phase 2 Contribution |
| :--- | :--- | :--- | :--- | :--- |
| **Ayushmaan Singh** | 26021974 | 22 | **Team Lead & Lead Developer** | System Architecture, Complete Python Implementation , Synopsis Documentation, & GitHub Repository Management , Testing , Data Entry , Presentation |
| Amartya Kushwaha | 26021234 | 10 | Team Member |  Observation |
| Aayush Goel | 26021507 | 7 | Team Member |  Observation |
| Aahvan Tripathi | 260211828 | 3 | Team Member |  Observation |

---

## Project Journey & Phases

### Phase 1: Project Synopsis & System Design (Completed)
- [x] Problem statement formulation and objective definition
- [x] 5-Module architecture design and implementation flowchart
- [x] Input/output specifications and constraint analysis

### Phase 2: Core Engine – 50% Implementation (Completed)
- [x] **Module 1 – Menu Management:** Created `FoodItem` base class and derived `MainCourse`, `Beverage`, and `Dessert` subclasses using inheritance, polymorphism (`calculate_price()`), dictionaries, sets, and tuples.
- [x] **Module 2 – Order and Billing:** Built interactive order processing using lists, billing dictionaries, and exception handling (`try-except-raise`) for unavailable items and invalid quantities.

### Phase 3: Analytics & Visualization – Final 50% (Upcoming)
- [ ] **Module 3 – File Management (Part 1):** Implemented permanent bill storage into `orders.txt` using Python file handling.
- [ ] **Module 3 – File Management (Part 2):** Read existing menu and order data automatically when the application starts.
- [ ] **Module 4 – Sales Analysis:** Analyze stored order data to identify popular food items, category-wise sales, and daily/monthly revenue.
- [ ] **Module 5 – Visualization:** Generate Matplotlib charts for most popular food items, category-wise sales, and daily/monthly revenue trends.

---

## How to Run Locally
```bash
git clone [https://github.com/AyushmaanSingh-git/restaurant-management-system.git](https://github.com/AyushmaanSingh-git/restaurant-management-system.git)
cd restaurant-management-system
python3 project.py
```