# Visualization Capture and Report Assembly Guide

This guide shows you how to capture visualizations from your Jupyter notebook and assemble them into your final PDF report.

## Quick Start: 3-Step Process

1. **Run notebook and capture screenshots** (15-20 minutes)
2. **Convert markdown to Word/Google Docs** (5 minutes)
3. **Insert screenshots and export to PDF** (10-15 minutes)

**Total Time:** ~30-40 minutes

---

## Step 1: Run Notebook and Capture Visualizations

### 1.1 Open and Run Notebook

```bash
# Navigate to notebooks directory
cd /mnt/d/Workspace/python/ucdpa-ml-capstone-project-healthcare-fraud-detection-ireland/notebooks

# Start Jupyter
jupyter notebook healthcare_fwa_consolidated_final.ipynb
```

### 1.2 Execute All Cells

In Jupyter:
1. Click **Cell** → **Run All** (or press `Shift + Enter` repeatedly)
2. Wait for all cells to complete (~2-5 minutes depending on data size)
3. Scroll through to verify all visualizations rendered correctly

### 1.3 Capture Required Visualizations

**15 Key Visualizations to Capture:**

#### Section 1: Demographics & EDA (5 screenshots)
```
[VIZ-01] Age Distribution by Region
Location: Section 5 - Exploratory Data Analysis
What to capture: Histogram showing age distribution across Dublin/Galway/Limerick
Screenshot name: viz01_age_distribution.png

[VIZ-02] Gender Distribution
Location: Section 5 - Exploratory Data Analysis  
What to capture: Bar chart or pie chart showing male/female/other breakdown
Screenshot name: viz02_gender_distribution.png

[VIZ-03] Claim Amount Distribution
Location: Section 5 - Exploratory Data Analysis
What to capture: Histogram (log scale) of claim amounts
Screenshot name: viz03_claim_amounts.png

[VIZ-04] Claims Over Time
Location: Section 5 - Exploratory Data Analysis
What to capture: Time series line chart showing claims from 2010-2023
Screenshot name: viz04_claims_timeline.png

[VIZ-05] Correlation Heatmap
Location: Section 5 - Exploratory Data Analysis
What to capture: Seaborn heatmap showing feature correlations
Screenshot name: viz05_correlation_matrix.png
```

#### Section 2: Anomaly Detection (3 screenshots)
```
[VIZ-06] Anomaly Score Distribution
Location: Section 6 - Isolation Forest Anomaly Detection
What to capture: Histogram showing distribution of anomaly scores
Screenshot name: viz06_anomaly_scores.png

[VIZ-07] Top Anomalous Claims
Location: Section 6 - Isolation Forest Anomaly Detection
What to capture: Bar chart showing top 20 most anomalous claims
Screenshot name: viz07_top_anomalies.png

[VIZ-08] Anomaly Score vs Claim Amount
Location: Section 6 - Isolation Forest Anomaly Detection
What to capture: Scatter plot showing relationship
Screenshot name: viz08_anomaly_vs_amount.png
```

#### Section 3: Supervised Learning (4 screenshots)
```
[VIZ-09] Confusion Matrix
Location: Section 7 - Random Forest Classification
What to capture: Heatmap confusion matrix
Screenshot name: viz09_confusion_matrix.png

[VIZ-10] ROC Curve
Location: Section 7 - Random Forest Classification
What to capture: ROC curve with AUC score
Screenshot name: viz10_roc_curve.png

[VIZ-11] Feature Importance
Location: Section 7 - Random Forest Classification
What to capture: Horizontal bar chart of top 15 features
Screenshot name: viz11_feature_importance.png

[VIZ-12] Precision-Recall Curve
Location: Section 7 - Random Forest Classification
What to capture: PR curve (if available)
Screenshot name: viz12_precision_recall.png
```

#### Section 4: Network Analysis (3 screenshots)
```
[VIZ-13] Provider-Patient Network Overview
Location: Section 8 - Graph Analysis
What to capture: Full network visualization (may be dense)
Screenshot name: viz13_network_full.png

[VIZ-14] High-Centrality Providers
Location: Section 8 - Graph Analysis
What to capture: Subgraph showing providers with highest centrality
Screenshot name: viz14_high_centrality_providers.png

[VIZ-15] Degree Distribution
Location: Section 8 - Graph Analysis
What to capture: Histogram of node degrees
Screenshot name: viz15_degree_distribution.png
```

### 1.4 Screenshot Capture Methods

**Option A: Windows Snipping Tool (Recommended for WSL)**
```
1. Windows Key + Shift + S (open Snipping Tool)
2. Select area around visualization
3. Paste into Paint (Ctrl+V)
4. Save as PNG in docs/visualizations/ folder
```

**Option B: Browser Screenshot Extension**
```
1. Install: "Awesome Screenshot" or "GoFullPage" extension
2. Click extension icon
3. Select "Capture visible part of page"
4. Save to docs/visualizations/
```

**Option C: Jupyter Built-in**
```python
# Right-click on any plot → "Save image as..."
# Or add to notebook cell:
fig.savefig('../docs/visualizations/viz01_age_distribution.png', dpi=300, bbox_inches='tight')
```

### 1.5 Create Visualizations Directory

```bash
mkdir -p /mnt/d/Workspace/python/ucdpa-ml-capstone-project-healthcare-fraud-detection-ireland/docs/visualizations
```

---

## Step 2: Convert Markdown to Editable Format

### Method A: Using Pandoc (Recommended)

**Install Pandoc (if not already installed):**
```bash
# Ubuntu/Debian
sudo apt-get install pandoc

# Or download from: https://pandoc.org/installing.html
```

**Convert to Word:**
```bash
cd /mnt/d/Workspace/python/ucdpa-ml-capstone-project-healthcare-fraud-detection-ireland/docs

# Basic conversion
pandoc PROJECT_REPORT_CONTENT.md -o UCD_ML_Project_Report.docx

# With table of contents
pandoc PROJECT_REPORT_CONTENT.md -o UCD_ML_Project_Report.docx --toc --toc-depth=3

# With reference document (for formatting)
pandoc PROJECT_REPORT_CONTENT.md -o UCD_ML_Project_Report.docx --reference-doc=template.docx
```

### Method B: Using Online Converter

1. Open https://www.markdowntopdf.com/ or https://dillinger.io/
2. Copy entire contents of `PROJECT_REPORT_CONTENT.md`
3. Paste into converter
4. Click "Export to Word" or "Export to PDF"
5. Download result

### Method C: Import to Google Docs

1. Go to https://docs.google.com
2. **File** → **Import** → **Upload**
3. Select `PROJECT_REPORT_CONTENT.md`
4. Google Docs will auto-format
5. Manually adjust formatting as needed

---

## Step 3: Insert Screenshots and Finalize

### 3.1 Open Document in Word/Google Docs

Open the converted `UCD_ML_Project_Report.docx`

### 3.2 Insert Visualizations

**Find each placeholder:**
```
[INSERT VISUALIZATION 1: Age Distribution by Region]
```

**Replace with actual image:**
1. Delete the placeholder text
2. **Insert** → **Image** → **From File**
3. Select corresponding visualization (e.g., `viz01_age_distribution.png`)
4. Resize to fit page width (~6.5 inches)
5. Add caption below image

**Caption Format:**
```
Figure 1: Patient age distribution across three Irish regions (Dublin, Galway, Limerick). 
Shows concentration in 30-60 age range with slight regional variations.
```

### 3.3 Formatting Checklist

- [ ] **Title Page:** Add your name, student ID, date
- [ ] **Table of Contents:** Auto-generate (References → Table of Contents)
- [ ] **Page Numbers:** Insert footer with page numbers
- [ ] **Headings:** Apply Heading 1, 2, 3 styles consistently
- [ ] **Tables:** Format with borders, alternating row colors
- [ ] **Images:** Resize consistently (all ~6-6.5 inches wide)
- [ ] **Image Captions:** Number sequentially (Figure 1, Figure 2, ...)
- [ ] **Font:** Use professional font (Arial 11pt or Times New Roman 12pt)
- [ ] **Margins:** 1 inch all sides
- [ ] **Line Spacing:** 1.15 or 1.5

### 3.4 Export to PDF

**From Microsoft Word:**
```
File → Save As → PDF
- Options: High quality (300 DPI)
- Include: Document structure tags for accessibility
```

**From Google Docs:**
```
File → Download → PDF Document (.pdf)
```

**From LibreOffice:**
```
File → Export as PDF
- Quality: 100%
- Reduce image resolution: Uncheck
```

---

## Step 4: Quality Check

### 4.1 Final Review Checklist

- [ ] All 15 visualizations inserted and properly labeled
- [ ] No placeholder text remaining `[INSERT...]`
- [ ] Page numbers on all pages except title page
- [ ] Table of contents reflects actual page numbers
- [ ] All tables formatted consistently
- [ ] References section complete
- [ ] Student name, ID, date on title page
- [ ] File named correctly: `Lastname_Firstname_ML_Project_Report.pdf`

### 4.2 Technical Checks

```bash
# Check PDF file size (should be 3-8 MB with images)
ls -lh UCD_ML_Project_Report.pdf

# Verify PDF is not corrupted
pdf-info UCD_ML_Project_Report.pdf  # If pdfinfo installed

# Open in PDF reader to verify
xdg-open UCD_ML_Project_Report.pdf  # Linux
```

### 4.3 Common Issues and Fixes

**Issue:** Images too large (file >15 MB)
- Fix: Compress images before inserting
```bash
# Using ImageMagick
mogrify -resize 1920x1080 -quality 85 *.png
```

**Issue:** Table of contents doesn't match page numbers
- Fix: Update TOC (Right-click TOC → Update Field → Update entire table)

**Issue:** Images pixelated
- Fix: Re-capture screenshots at higher resolution (use `dpi=300` in savefig)

**Issue:** Markdown formatting lost
- Fix: Manually reapply heading styles in Word

---

## Alternative: Automated Screenshot Capture

If you want to automate screenshot capture from notebook:

### Create Screenshot Script

```python
# Save as: capture_visualizations.py
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from PIL import Image
import io
import base64
import os

# Execute notebook
with open('notebooks/healthcare_fwa_consolidated_final.ipynb') as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})

# Extract images from outputs
os.makedirs('docs/visualizations', exist_ok=True)
img_counter = 1

for cell in nb.cells:
    if cell.cell_type == 'code' and 'outputs' in cell:
        for output in cell.outputs:
            if 'data' in output and 'image/png' in output.data:
                img_data = base64.b64decode(output.data['image/png'])
                img = Image.open(io.BytesIO(img_data))
                img.save(f'docs/visualizations/viz{img_counter:02d}_auto.png')
                print(f"Saved visualization {img_counter}")
                img_counter += 1

print(f"\nTotal visualizations captured: {img_counter - 1}")
```

**Run:**
```bash
python3 capture_visualizations.py
```

---

## Summary: Complete Workflow

```
┌─────────────────────────────────────────────────┐
│ 1. Run Notebook → Capture 15 Screenshots       │
│    Time: 20 minutes                             │
│    Output: viz01.png - viz15.png                │
└─────────────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│ 2. Convert Markdown to Word                     │
│    Tool: Pandoc or online converter             │
│    Time: 5 minutes                              │
│    Output: UCD_ML_Project_Report.docx           │
└─────────────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│ 3. Insert Screenshots & Format                  │
│    Replace [INSERT...] with actual images       │
│    Time: 15 minutes                             │
│    Output: Formatted Word document              │
└─────────────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│ 4. Export to PDF & Quality Check                │
│    File → Save As PDF                           │
│    Time: 5 minutes                              │
│    Output: Lastname_Firstname_ML_Report.pdf     │
└─────────────────────────────────────────────────┘
```

**Total Time:** ~45 minutes  
**Final Output:** Professional PDF report with all visualizations

---

## Need Help?

### Troubleshooting Resources

1. **Jupyter not starting:** Check if port 8888 is free, try `jupyter notebook --port 8889`
2. **Plots not showing:** Add `%matplotlib inline` at top of notebook
3. **Pandoc errors:** Try online converter as fallback
4. **Word formatting issues:** Use LibreOffice as alternative

### Contact

If you encounter issues specific to the UCD project submission requirements, contact your course instructor or refer to the UCD Professional Academy submission guidelines.

---

**READY TO START?** 

Run this command to begin:
```bash
cd /mnt/d/Workspace/python/ucdpa-ml-capstone-project-healthcare-fraud-detection-ireland/notebooks
jupyter notebook healthcare_fwa_consolidated_final.ipynb
```

Good luck with your report! 🎓
