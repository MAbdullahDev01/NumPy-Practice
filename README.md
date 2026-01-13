# NumPy-30-Days-Practice Repository

Welcome to the **NumPy-30-Days-Practice** repository! 🚀
This repository is designed for **mastering NumPy in 30 days** through **daily hands-on practice**, following a carefully structured, beginner-to-intermediate roadmap focused on real-world data science usage.

---

## **Repository Structure**

```
NumPy-30-Days-Practice/
│
├─ README.md                  # Overview, roadmap, and guidelines
├─ .gitignore
├─ Week_1_Foundations/        # ND-arrays, creation, indexing, dtypes
├─ Week_2_Manipulation/       # Reshaping, stacking, masking, filtering
├─ Week_3_Math_Vectorization/ # Ufuncs, broadcasting, aggregations
├─ Week_4_Advanced/           # Linear algebra, randomness, I/O, performance
├─ Projects/                  # Mini-projects & real-world applications
└─ utils/                     # Helper scripts & reusable functions
```

Each week is organized into its own folder.
Daily practice files are named using the format:

```
Day_XX_Topic.py
```

This keeps progress chronological and easy to track.

---

## **30-Day Learning Plan Overview**

### **Week 1 — Foundations of ND-Arrays**

* Day 1: NumPy arrays vs Python lists
* Day 2: Array creation methods (`zeros`, `ones`, `arange`, `linspace`)
* Day 3: Data types and type casting
* Day 4: Array attributes (`shape`, `size`, `ndim`)
* Day 5: Basic indexing (1D & 2D)
* Day 6: Slicing and subarrays
* Day 7: Views vs copies + weekly review

---

### **Week 2 — Array Manipulation & Logic**

* Day 8: Reshaping arrays
* Day 9: Flattening and raveling
* Day 10: Transpose and axis manipulation
* Day 11: Stacking arrays (vertical & horizontal)
* Day 12: Splitting arrays
* Day 13: Boolean masking and filtering
* Day 14: Conditional logic with `np.where` + review

---

### **Week 3 — Mathematical Operations & Vectorization**

* Day 15: Element-wise operations
* Day 16: Universal functions (ufuncs)
* Day 17: Aggregations and reductions
* Day 18: Broadcasting rules
* Day 19: Cumulative operations
* Day 20: Comparison and logical operations
* Day 21: Vectorization vs Python loops + optimization

---

### **Week 4 — Advanced NumPy & Real-World Applications**

* Day 22: Linear algebra fundamentals
* Day 23: Matrix inverse & determinant
* Day 24: Eigenvalues and eigenvectors
* Day 25: Random number generation
* Day 26: Statistical sampling & simulations
* Day 27: File I/O with NumPy
* Day 28: Performance optimization techniques
* Day 29: Mini-project (real dataset analysis)
* Day 30: Final review & interview-style problems

---

## **Git Commit Guidelines**

* Commit **each day’s work separately**.
* Follow this commit message format:

```
feat(NumPy-DayXX): implemented [topic/problem]
```

### **Examples**

```
git commit -m "feat(NumPy-Day05): implemented array slicing and indexing"
git commit -m "feat(NumPy-Day18): practiced broadcasting rules"
git commit -m "feat(Project): completed NumPy-based data analysis mini-project"
```

* Optional weekly milestone tags:

```
git tag Week_1_Completed
git tag Week_2_Completed
```

---

## **Tips for Effective Practice**

1. Write **pure NumPy solutions** before using loops.
2. Always inspect array **shape and dtype** when debugging.
3. Try to **vectorize first**, then compare with loop-based code.
4. Add comments explaining *why* an approach works.
5. Revisit older problems and optimize them using new concepts.

---

## **Goal of This Repository**

By the end of 30 days, this repository will demonstrate:

* Strong command of NumPy fundamentals
* Ability to manipulate and analyze real datasets
* Efficient, vectorized numerical computing skills
* Readiness for **Pandas, Machine Learning, and Scientific Computing**

---

📌 **Consistency matters more than speed. Commit daily and build real mastery.**
