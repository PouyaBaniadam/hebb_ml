# University Admissions Dataset

### Predicting Applicant Success for a Competitive Graduate Program

This dataset simulates a real-world binary classification problem: determining whether an applicant should be admitted (`+1`) or rejected (`-1`) from a competitive university's graduate program. The data is designed to be **linearly separable**, meaning a model like the one you built can learn a clear boundary between successful and unsuccessful candidates.

## Dataset Structure
- **Total Samples:** 150 applicants
- **Features:** 7 distinct attributes for each applicant
- **Target (Label):** 1 binary outcome (Admitted/Rejected)

---

## Feature Breakdown

The model's decision is based on a combination of the following seven features. Each feature tells a part of the applicant's story.

| Feature Name | CSV Column | Description | Data Type | Range / Values | Expected Impact on Admission |
| :--- | :---: | :--- | :---: | :---: | :---: |
| `GPA` | 1 | The applicant's Grade Point Average from their undergraduate degree. | `Float` | 2.5 - 4.0 | **Positive** (Higher is better) |
| `Exam Score` | 2 | The score achieved on a standardized entrance exam (e.g., GRE). | `Float` | 140 - 170 | **Positive** (Higher is better) |
| `Papers` | 3 | The number of academic papers the applicant has published. | `Integer` | 0 - 4 | **Positive** (Higher is better) |
| `University Rank`| 4 | The ranking of the applicant's previous university. | `Integer` | 1 - 100 | **Negative** (_Lower is better_) |
| `Recommendation`| 5 | The strength of recommendation letters, scored on a 5-point scale. | `Float` | 2.5 - 5.0 | **Positive** (Higher is better) |
| `Work Experience`| 6 | Years of relevant work experience in their field of study. | `Integer` | 0 - 5 | **Positive** (Higher is better) |
| `Is International`| 7 | A binary flag indicating if the applicant is an international student. | `Integer` | 0 or 1 | **Slightly Negative** (Minor penalty) |

---

## The Target Variable: `label`

This is the final column in the dataset and represents the ground truth—the decision the admissions committee actually made.

*   ✅ **Admitted (`+1`):** These applicants generally have a strong profile across most of the positive-impact features. They demonstrate academic excellence and potential.

*   ❌ **Rejected (`-1`):** These applicants may be weak in one or more key areas (e.g., low GPA, poor exam score) or have a combination of several mediocre scores.

> ### The Underlying Logic: A Balancing Act
> No single feature guarantees admission or rejection. The dataset is designed to reflect a realistic balancing act. For example:
> *   A student with a perfect `GPA` but a very low `Exam Score` might be **rejected**.
> *   A student from a lower-ranked university (`University Rank` is high) might be **admitted** if they have an exceptional number of `Papers` and strong `Recommendations`.
>
> Your model's task is to learn the "weights" or importance of each feature to find the optimal combination that best separates the admitted students from the rejected ones.

---

### Data Snippet (`.csv`)

Here is what the raw data looks like in the file. Each row is a unique applicant.

```csv
# GPA, Exam, Papers, Rank, Reco, Work, Intl, Label
3.81,164,2,20,4.6,1,0,1
3.83,166,2,15,4.7,0,0,1
2.85,149,0,95,3.2,0,1,-1
3.76,162,1,28,4.4,2,0,1
3.73,163,1,23,4.3,0,1,1
2.81,145,0,100,3.0,0,0,-1