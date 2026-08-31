# Myntra Wishlist-to-Purchase Conversion Growth Project

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Dashboard-brightgreen)](index.html)
[![Audit Status](https://img.shields.io/badge/Human%20Audit-90%25%20Agreement%20%28n%3D30%29-blue)](#-research-methodology)

## 📌 Executive Summary

Wishlist non-conversion in fashion e-commerce contains two fundamentally different user states: **low-intent storage** and **high-intent decision friction**.

Within the analyzed directional sample ($n=150$), **51.3% of conversations** were classified as **high-intent / high-friction**. The strongest addressable decision frictions blocking checkout were **fit uncertainty**, **comparison paralysis**, and **product-reality uncertainty**.

This growth engine demonstrates that the primary growth opportunity is **not to increase generic wishlist engagement**, but to **identify high-intent wishlist states and resolve the final decision uncertainty preventing checkout.**

---

## 🎯 Refined Problem Thesis Statement

> *"High-intent wishlist users are not necessarily abandoning products because they no longer want them; many are postponing purchase because **one or more decision uncertainties remain unresolved.** The growth opportunity is to identify these high-intent states and reduce the final decision friction—particularly fit, comparison, and product-reality uncertainty—within the 30-day consideration window."*

---

## 🧭 Exact 4-Quadrant Intent × Friction Distribution ($n=150$)

| Quadrant | Description | Sample Count | Sample % | Strategic Focus |
|---|---|---|---|---|
| 🎯 **High Intent / High Friction** | Selected size/color, wants to buy but stalled by fit/comparison doubts | **77 of 150** | **51.3%** | **PRIMARY GROWTH TARGET** |
| ⚡ **High Intent / Low Decision Friction** | Active purchase intent waiting for routine execution (e.g. salary credit) | **25 of 150** | **16.7%** | Routine Execution |
| 🔍 **Low Intent / High Friction** | Casual browsing or aesthetic outfit saving without purchase timeline | **33 of 150** | **22.0%** | Passive Exploration |
| 📁 **Low Intent / Low Friction** | Long-term bookmarking to declutter cart | **15 of 150** | **10.0%** | Mood Board Archive |

---

## 📊 Transparent 5-Dimension Opportunity Scoring Matrix (Max 25)

$$\text{Opportunity Score} = \text{Prevalence } (P/5) + \text{Intent Proximity } (I/5) + \text{Severity } (S/5) + \text{Addressability } (A/5) + \text{Confidence } (C/5)$$

| Opportunity Area | P /5 | I /5 | S /5 | A /5 | C /5 | Math Formula | Final Score & Rank |
|---|---|---|---|---|---|---|---|
| **1. Size & Fit Uncertainty** | 4 | 5 | 5 | 5 | 4 | $4+5+5+5+4$ | **RANK #1 (23/25)** |
| **2. Comparison Paralysis** | 5 | 5 | 4 | 5 | 3 | $5+5+4+5+3$ | **RANK #2 (22/25)** |
| **3. Product Quality / Real Photo Void** | 5 | 4 | 3 | 4 | 3 | $5+4+3+4+3$ | RANK #3 (19/25) |
| **4. Price Volatility & Context** | 4 | 4 | 4 | 2* | 3 | $4+4+4+2+3$ | **RANK #4 (17/25)** |
| **5. Styling & Wardrobe Match** | 4 | 3 | 3 | 4 | 2 | $4+3+3+4+2$ | **RANK #5 (16/25)** |
| **6. Passive Bookmarking** | 3 | 1 | 1 | 3 | 2 | $3+1+1+3+2$ | RANK #6 (10/25) |

---

## 📁 Repository Structure

```text
├── index.html                       # Main Interactive Discovery Engine Dashboard
├── discovery_dashboard.html         # Mirror HTML Dashboard
├── discovery_engine.py              # Python Multi-Label Classification & NLP Pipeline
├── generate_dashboard.py            # Dashboard HTML Compiler
├── generate_sheets.py               # Excel Growth Strategy Generator
├── feedback_analysis_output.csv     # Complete Scraped Dataset with Traceable URLs & Audit Tags
└── Myntra_Wishlist_Growth_Project.xlsx # Multi-Tab Financial & Growth Strategy Workbook
```

---

## 🔬 Research Methodology & Provenance

* **Sample Size**: $n=150$ public conversations across Reddit (`r/IndianFashionAddicts`, `r/myntra`), Google Play Store, Apple App Store, and fashion blogs.
* **Classification Validation**: $90.0\%$ friction-tag agreement on a $20\%$ random human audit sample ($30/150$ items audited).
* **Multi-Label Model**: Non-mutually exclusive category tagging (prevalence percentages represent sample density).
