# Healthcare FWA Analysis - Notebook Guide

## 📘 Consolidated Final Notebook

**File**: `healthcare_fwa_consolidated_final.ipynb`

### Overview
This is the **primary notebook** for the UCD ML Certificate project submission. It consolidates analysis from all other notebooks with comprehensive documentation and visualizations.

### What's Inside

#### 1. **Executive Summary & Problem Statement**
- Project objectives
- Business context (€56B annual EU healthcare fraud)
- Research questions

#### 2. **Data Loading & Preprocessing**
- Configurable data location (Galway, Dublin, Limerick)
- Date/time conversions
- Age calculation
- Feature engineering (temporal features, provider metrics)
- Data filtering and quality checks

#### 3. **Exploratory Data Analysis (EDA)**
- **Patient Demographics**: Age distribution, gender analysis
- **Claims Analysis**: Amount distributions, temporal patterns, top providers
- **Correlation Analysis**: Feature relationship heatmaps

#### 4. **Anomaly Detection (Isolation Forest)**
- Unsupervised learning approach
- ~1% contamination rate
- Anomaly score visualization
- Comparison of normal vs. anomalous claims

#### 5. **Supervised Learning (Random Forest)**
- Demonstration using synthetic labels
- Train/test split
- Classification metrics
- Feature importance analysis
- ROC curve and confusion matrix

#### 6. **Graph-Based Network Analysis**
- Provider-patient bipartite network
- Degree and betweenness centrality
- Suspicious provider identification
- Network visualizations

#### 7. **Results Summary**
- Comprehensive metrics across all methods
- Key findings and insights
- Suspicious claims export

#### 8. **Conclusions & Recommendations**
- Technical achievements
- Limitations and constraints
- Future work recommendations
- Business impact assessment

### How to Run

1. **Prerequisites**:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly scikit-learn networkx jupyter
   ```

2. **Configure Data Location**:
   - Open the notebook
   - In Section 2, change `data_location = 'galway'` to your desired location

3. **Execute**:
   - Run all cells sequentially (Cell → Run All)
   - Total execution time: 5-15 minutes

### Key Features

✅ **Comprehensive**: Covers full ML pipeline from data loading to conclusions  
✅ **Well-Documented**: Extensive markdown explanations for each section  
✅ **Visualizations**: 15+ charts and graphs  
✅ **Production-Ready**: Error handling, logging, and data validation  
✅ **Academic Standard**: Suitable for UCD ML Certificate project submission  

### Output

The notebook generates:
- Multiple visualizations for each analysis phase
- Statistical summaries
- Suspicious claims/providers lists
- Model performance metrics
- Network graphs

### Comparison with Other Notebooks

| Notebook | Purpose | Use Case |
|----------|---------|----------|
| `healthcare_fwa_analysis.ipynb` | Initial EDA & outlier detection | Exploratory work |
| `healthcare_fwa_graph_analysis.ipynb` | Research paper implementation | Graph-focused analysis |
| `healthcare_fwa_opt2_analysis.ipynb` | ML anomaly detection | ML-focused experiments |
| **`healthcare_fwa_consolidated_final.ipynb`** | **Complete analysis** | **Final submission** ⭐ |

### Tips for Customization

1. **Adjust Anomaly Threshold**: Change `contamination=0.01` in Isolation Forest
2. **Modify Features**: Update `feature_columns` list for different feature sets
3. **Change Network Size**: Adjust `top_providers[:5]` for subgraph visualization
4. **Export Results**: Uncomment save commands to export to CSV/PNG

### Troubleshooting

**Issue**: File not found errors  
**Solution**: Verify data_location path and ensure CSV files exist

**Issue**: Memory errors with large datasets  
**Solution**: Filter data by date range or sample randomly

**Issue**: Long execution time for network analysis  
**Solution**: Reduce number of nodes or use approximation methods

---

## 📊 Alignment with UCD ML Certificate Requirements

✅ **Problem Definition**: Clear business problem with real-world impact  
✅ **Data Collection**: Synthetic data with documented sources  
✅ **Data Preprocessing**: Comprehensive cleaning and feature engineering  
✅ **EDA**: Multiple visualizations and statistical analysis  
✅ **Feature Engineering**: Temporal, aggregated, and network features  
✅ **Model Selection**: Multiple algorithms (unsupervised & supervised)  
✅ **Model Evaluation**: Appropriate metrics and visualizations  
✅ **Results Interpretation**: Clear findings and actionable insights  
✅ **Conclusions**: Limitations, recommendations, future work  
✅ **Documentation**: Well-structured with markdown explanations  

---

**Last Updated**: November 2025  
**Author**: Nithin Mohan T K  
**Contact**: Available via GitHub repository
