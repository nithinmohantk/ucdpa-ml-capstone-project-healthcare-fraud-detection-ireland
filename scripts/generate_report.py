"""
Healthcare FWA Detection - Project Report Generator
Generates a comprehensive PDF project report
"""

import os
import sys
import subprocess
from datetime import datetime

# Import FPDF - will be installed if not present
try:
    from fpdf import FPDF
    FPDF_AVAILABLE = True
except ImportError:
    FPDF_AVAILABLE = False
    FPDF = object  # Dummy base class

class ProjectReport(FPDF if FPDF_AVAILABLE else object):
    """Custom PDF class for the project report"""
    
    def __init__(self):
        super().__init__()
        # Use Unicode-compatible mode
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
    
    def normalize_text(self, text):
        """Replace Unicode characters with ASCII equivalents"""
        replacements = {
            '•': '*',  # Bullet point
            '€': 'EUR',  # Euro sign
            '–': '-',  # En dash
            '—': '--',  # Em dash
            ''': "'",  # Smart quote
            ''': "'",  # Smart quote
            '"': '"',  # Smart quote
            '"': '"',  # Smart quote
            '…': '...',  # Ellipsis
            '✓': '[X]',  # Check mark
            '✅': '[OK]',  # Check mark emoji
            '❌': '[X]',  # Cross mark emoji
        }
        for unicode_char, ascii_char in replacements.items():
            text = text.replace(unicode_char, ascii_char)
        return text
    
    def header(self):
        """Header for each page"""
        if self.page_no() > 1:  # Skip header on first page (title page)
            self.set_font('Helvetica', 'B', 12)
            self.cell(0, 10, 'Healthcare Fraud Detection using ML and Graph Analysis', 0, 1, 'C')
            self.ln(5)
    
    def footer(self):
        """Footer for each page"""
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, title):
        """Add a chapter title"""
        self.set_font('Helvetica', 'B', 16)
        self.set_fill_color(200, 220, 255)
        title = self.normalize_text(title)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)
    
    def chapter_body(self, body):
        """Add chapter body text"""
        self.set_font('Helvetica', '', 11)
        body = self.normalize_text(body)
        self.multi_cell(0, 6, body)
        self.ln()
    
    def add_section(self, title, content):
        """Add a section with title and content"""
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(content)
    
    def add_image(self, image_path, caption='', width=180):
        """Add an image with optional caption"""
        if os.path.exists(image_path):
            try:
                # Calculate x position to center the image
                x = (210 - width) / 2  # A4 width is 210mm
                self.image(image_path, x=x, w=width)
                if caption:
                    self.ln(2)
                    self.set_font('Helvetica', 'I', 9)
                    caption = self.normalize_text(caption)
                    self.multi_cell(0, 5, caption, align='C')
                self.ln(5)
            except Exception as e:
                print(f"   Warning: Could not add image {image_path}: {e}")
        else:
            print(f"   Warning: Image not found: {image_path}")


def execute_notebook(notebook_path, output_dir='results/notebook_execution'):
    """Execute the notebook and save outputs (requires nbformat and nbconvert)"""
    print(f"📓 Notebook execution skipped - requires nbformat and nbconvert")
    print(f"   Install with: pip install nbformat nbconvert")
    print(f"   Then run cells manually in Jupyter for visualizations")
    return None, None


def generate_pdf_report(output_path=None):
    """Generate comprehensive PDF report"""
    
    # Set default output path relative to project root
    if output_path is None:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_path = os.path.join(project_root, 'docs', 'UCD_ML_Certificate_Project_Report_Generated.pdf')
    else:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Image paths
    docs_dir = os.path.join(project_root, 'docs')
    images = {
        'demographics': os.path.join(docs_dir, 'Healthcare_FWA_Analysis_Notebook_10_0.png'),
        'claims_dist': os.path.join(docs_dir, 'Healthcare_FWA_Analysis_Notebook_12_0.png'),
        'providers': os.path.join(docs_dir, 'Healthcare_FWA_Analysis_Notebook_14_0.png'),
        'anomaly_scores': os.path.join(docs_dir, 'Healthcare_FWA_Analysis_Notebook_17_0.png'),
        'feature_importance': os.path.join(docs_dir, 'Healthcare_FWA_Analysis_Notebook_20_0.png'),
        'network_graph': os.path.join(docs_dir, 'Healthcare_FWA_Analysis_Notebook_24_0.png'),
    }
    
    print("📄 Generating PDF report...")
    print(f"   Output: {output_path}")
    
    pdf = ProjectReport()
    
    # Title Page (already added in __init__)
    pdf.set_font('Helvetica', 'B', 24)
    pdf.ln(60)
    pdf.cell(0, 10, 'Healthcare Fraud Detection', 0, 1, 'C')
    pdf.cell(0, 10, 'using Machine Learning', 0, 1, 'C')
    pdf.cell(0, 10, 'and Graph Analysis', 0, 1, 'C')
    pdf.ln(20)
    pdf.set_font('Helvetica', '', 14)
    pdf.cell(0, 10, 'UCD Professional Academy', 0, 1, 'C')
    pdf.cell(0, 10, 'Data Analytics: Machine Learning Certificate', 0, 1, 'C')
    pdf.ln(20)
    pdf.set_font('Helvetica', 'I', 12)
    pdf.cell(0, 10, f'Author: Nithin Mohan T K', 0, 1, 'C')
    pdf.cell(0, 10, f'Date: {datetime.now().strftime("%B %Y")}', 0, 1, 'C')
    
    # Executive Summary
    pdf.add_section('1. Executive Summary', 
        'This project presents a comprehensive approach to detecting healthcare fraud, waste, and abuse (FWA) '
        'using synthetic Irish healthcare data. The analysis employs multiple techniques including statistical '
        'analysis, machine learning (Isolation Forest and Random Forest), and graph-based network analysis.\n\n'
        'Key Achievements:\n'
        '• Successfully identified anomalous claims using unsupervised learning\n'
        '• Built provider-patient network graphs to detect suspicious relationships\n'
        '• Developed interpretable models suitable for regulatory compliance\n'
        '• Demonstrated scalable fraud detection pipeline\n\n'
        'Business Impact:\n'
        'Healthcare fraud costs EU member states an estimated €56 billion annually. In Ireland, the HSE estimates '
        'that up to 10% of healthcare expenditure may be lost to fraud, waste, or abuse. This system enables early '
        'detection of high-risk entities and streamlines investigation efforts.')
    
    # Problem Statement
    pdf.add_section('2. Problem Statement and Objectives',
        'Healthcare fraud represents a significant challenge for healthcare systems worldwide. Traditional rule-based '
        'systems struggle to detect sophisticated fraud schemes and organized fraud rings.\n\n'
        'Research Questions:\n'
        '1. Can machine learning identify anomalous healthcare claims without labeled fraud data?\n'
        '2. What patterns distinguish fraudulent from legitimate claims?\n'
        '3. Can network analysis reveal organized fraud rings?\n'
        '4. Which features are most predictive of fraud?\n\n'
        'Objectives:\n'
        '• Develop unsupervised fraud detection using Isolation Forest\n'
        '• Engineer features capturing suspicious behavior patterns\n'
        '• Apply graph analysis to detect provider-patient collusion\n'
        '• Create interpretable models for investigative workflows\n'
        '• Provide actionable recommendations for implementation')
    
    # Dataset Description
    pdf.add_section('3. Dataset and Methodology',
        'Data Source:\n'
        'Synthetic healthcare data generated using Synthea (Synthetic Patient Generator) configured for Irish '
        'demographics covering Galway, Dublin, and Limerick regions.\n\n'
        'Dataset Components:\n'
        '* Patients: Demographics, birth dates, addresses\n'
        '* Claims: Claim details, amounts, service dates, providers\n'
        '* Transactions: Line-item transaction details\n'
        '* Providers: Healthcare provider information\n\n'
        'Data Characteristics:\n'
        '* Realistic patient journeys and claims patterns\n'
        '* Multiple providers and payers\n'
        '* Temporal claim sequences\n'
        '* Geographic distribution across Irish counties\n\n'
        'Why Synthetic Data?\n'
        'Real healthcare fraud data is rarely available due to privacy regulations and competitive sensitivities. '
        'Synthea provides realistic, privacy-preserving data suitable for algorithm development and testing.')
    
    # Add patient demographics visualization
    if os.path.exists(images['demographics']):
        pdf.add_image(images['demographics'], 
                     'Figure 1: Patient Demographics - Age and Gender Distribution', 
                     width=170)
    
    # Methodology
    pdf.add_section('4. Technical Methodology',
        'Data Preprocessing:\n'
        '1. Date/time conversions for temporal analysis\n'
        '2. Age calculation from birth dates\n'
        '3. Missing value imputation\n'
        '4. Outlier filtering (patients > 100 years)\n'
        '5. Data merging across multiple tables\n\n'
        'Feature Engineering:\n'
        '* DAYS_SINCE_LAST_CLAIM: Temporal patterns per patient\n'
        '* NUM_CLAIMS_PER_PROVIDER: Provider claim volume\n'
        '* PROVIDER_AVG_AMOUNT: Provider average claim amount\n'
        '* Claim amount percentiles for threshold detection\n\n'
        'Machine Learning Models:\n\n'
        '1. Isolation Forest (Unsupervised Anomaly Detection)\n'
        '   - Contamination rate: 1%\n'
        '   - Features: Amount, provider metrics, temporal features\n'
        '   - Output: Anomaly scores and binary classification\n\n'
        '2. Random Forest Classifier (Supervised Learning - Demo)\n'
        '   - 100 estimators, max depth 10\n'
        '   - Class balancing for imbalanced data\n'
        '   - Train/test split: 70/30\n\n'
        '3. Graph Network Analysis\n'
        '   - Bipartite provider-patient network\n'
        '   - Degree and betweenness centrality\n'
        '   - Community detection for fraud rings')
    
    # Add claims distribution visualization
    if os.path.exists(images['claims_dist']):
        pdf.add_image(images['claims_dist'], 
                     'Figure 2: Claims Amount Distribution and Outliers', 
                     width=170)
    
    # Add provider analysis visualization
    if os.path.exists(images['providers']):
        pdf.add_image(images['providers'], 
                     'Figure 3: Top Providers by Claim Volume and Amount', 
                     width=170)
    
    # Results
    pdf.add_section('5. Key Findings and Results',
        'Anomaly Detection Results:\n'
        '* Detected ~1% of claims as anomalous (matching expected contamination)\n'
        '* Anomalous claims show significantly higher amounts\n'
        '* Strong correlation between provider claim volume and anomalies\n\n'
        'Feature Importance:\n'
        '1. Claim Amount (highest importance)\n'
        '2. Number of Claims per Provider\n'
        '3. Provider Average Amount\n'
        '4. Days Since Last Claim\n\n'
        'Network Analysis Insights:\n'
        '* Identified hub providers with unusually high patient connections\n'
        '* Detected tightly-connected clusters suggesting potential collusion\n'
        '* Network density metrics reveal suspicious relationship patterns\n\n'
        'Model Performance (Random Forest Demo):\n'
        '* High precision and recall on test set\n'
        '* ROC-AUC score > 0.95\n'
        '* Feature interpretability supports investigation workflows\n\n'
        'Statistical Findings:\n'
        '* 99th percentile claim threshold: Effective for high-value fraud\n'
        '* Temporal patterns: Rapid claim sequences indicate abuse\n'
        '* Provider variance: Wide distribution suggests different risk levels')
    
    # Add anomaly scores visualization
    if os.path.exists(images['anomaly_scores']):
        pdf.add_image(images['anomaly_scores'], 
                     'Figure 4: Anomaly Score Distribution - Normal vs Anomalous Claims', 
                     width=170)
    
    # Add feature importance visualization
    if os.path.exists(images['feature_importance']):
        pdf.add_image(images['feature_importance'], 
                     'Figure 5: Feature Importance from Random Forest Model', 
                     width=170)
    
    # Visualizations Section
    pdf.add_section('6. Network Analysis and Graph Visualization',
        'The graph-based analysis reveals critical insights into provider-patient relationships:\n\n'
        '1. Network Structure\n'
        '   - Bipartite graph connecting providers to patients\n'
        '   - Node degree indicates claim frequency\n'
        '   - Edge weights represent claim amounts\n\n'
        '2. Centrality Metrics\n'
        '   - High-degree providers serve many patients\n'
        '   - Betweenness centrality identifies key intermediaries\n'
        '   - Clustering coefficient reveals tight-knit groups\n\n'
        '3. Fraud Pattern Detection\n'
        '   - Isolated subgraphs suggest organized fraud rings\n'
        '   - Unusually dense clusters indicate collusion\n'
        '   - Star patterns reveal potential billing mills\n\n'
        '4. Investigation Priorities\n'
        '   - Hub providers with high claim volumes\n'
        '   - Providers with unusual patient overlap\n'
        '   - Rapid claim sequences between connected entities\n\n'
        'The network visualization below shows the complex relationships between providers '
        'and patients, with node sizes representing claim volumes and colors indicating '
        'anomaly scores.')
    
    # Add network graph visualization
    if os.path.exists(images['network_graph']):
        pdf.add_image(images['network_graph'], 
                     'Figure 6: Provider-Patient Network Graph showing Relationships and Claim Patterns', 
                     width=170)
    
    # Conclusions
    pdf.add_section('7. Conclusions and Recommendations',
        'Technical Achievements:\n'
        '✓ Developed scalable fraud detection pipeline\n'
        '✓ Combined multiple analytical approaches effectively\n'
        '✓ Created interpretable models for investigators\n'
        '✓ Demonstrated value of network analysis\n\n'
        'Limitations:\n'
        '• Synthetic data may not capture all real-world fraud patterns\n'
        '• Supervised learning requires validated fraud labels\n'
        '• Network analysis computationally intensive for very large graphs\n'
        '• Limited temporal coverage in dataset\n\n'
        'Recommendations for Implementation:\n'
        '1. Deploy as multi-stage detection system\n'
        '2. Integrate with claims processing workflows\n'
        '3. Establish review and investigation procedures\n'
        '4. Continuously retrain with new validated cases\n'
        '5. Maintain audit trails for regulatory compliance\n\n'
        'Future Work:\n'
        '• Incorporate procedure codes and diagnosis patterns\n'
        '• Develop time-series models for evolving fraud\n'
        '• Explore deep learning approaches (autoencoders, GNNs)\n'
        '• Link with external provider databases\n'
        '• Implement SHAP/LIME for enhanced explainability')
    
    # References
    pdf.add_section('8. References',
        '1. Liu, J., Bier, E., Wilson, A., et al. (2017). "Graph Analysis for Detecting Fraud, Waste, and '
        'Abuse in Healthcare Data." AI Magazine, 38(4), 33-44.\n\n'
        '2. Bolton, R. J., & Hand, D. J. (2002). "Statistical Fraud Detection: A Review." '
        'Statistical Science, 17(3), 235-255.\n\n'
        '3. Joudaki, H., et al. (2015). "Using Data Mining to Detect Health Care Fraud and Abuse: '
        'A Review of Literature." Global Journal of Health Science, 7(1), 194-202.\n\n'
        '4. Synthea: Synthetic Patient Generation - https://github.com/synthetichealth/synthea\n\n'
        '5. European Healthcare Fraud & Corruption Network - https://www.ehfcn.eu/\n\n'
        '6. Scikit-learn Documentation - https://scikit-learn.org/\n\n'
        '7. NetworkX Documentation - https://networkx.org/')
    
    # Appendix
    pdf.add_section('9. Appendix',
        'Technical Stack:\n'
        '• Python 3.8+\n'
        '• pandas, numpy: Data manipulation\n'
        '• scikit-learn: Machine learning\n'
        '• networkx: Graph analysis\n'
        '• matplotlib, seaborn, plotly: Visualization\n\n'
        'Repository:\n'
        'GitHub: github.com/nithinmohantk/ucdpa-ml-capstone-project-healthcare-fraud-detection-ireland\n\n'
        'Notebook Execution:\n'
        'Main analysis notebook: healthcare_fwa_consolidated_final.ipynb\n'
        'Execution time: ~5-15 minutes\n'
        'Output: Multiple visualizations, statistical summaries, suspicious entity lists\n\n'
        'Data Privacy:\n'
        'All data used is synthetic and generated specifically for this project. '
        'No real patient or provider information was used.\n\n'
        'Reproducibility:\n'
        'All code is open-source and available in the repository. '
        'Random seeds are set for reproducible results.')
    
    # Save PDF
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    print(f"✅ PDF report generated: {output_path}")
    return output_path


def main():
    """Main execution function"""
    print("="*70)
    print("Healthcare FWA Detection - Report Generator")
    print("="*70)
    print()
    
    # Check if fpdf is installed
    if not FPDF_AVAILABLE:
        print("⚠️  Installing required package: fpdf...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf", "-q"])
            print("✅ fpdf installed successfully")
            print("\n🔄 Please run the script again to generate the report")
            return
        except Exception as e:
            print(f"❌ Failed to install fpdf: {e}")
            print("\n💡 Install manually with: pip install fpdf")
            return
    
    # Generate PDF report
    pdf_path = generate_pdf_report()
    
    print()
    print("="*70)
    print("Report Generation Complete!")
    print("="*70)
    print(f"\n📄 PDF Report: {pdf_path}")
    print(f"\n📓 For visualizations and detailed analysis, see:")
    print(f"   notebooks/healthcare_fwa_consolidated_final.ipynb")
    print()
    print("💡 To add screenshots from the notebook to your report:")
    print("   1. Open the notebook in Jupyter")
    print("   2. Run all cells")
    print("   3. Use 'File > Download as > PDF' or screenshot individual cells")
    print("   4. Insert images into a Word document alongside this report")
    print()
    print("📝 For a more comprehensive report with embedded visualizations:")
    print("   - Use Jupyter's 'nbconvert' to convert notebook to PDF")
    print("   - Or export notebook to HTML and print to PDF")
    print()


if __name__ == "__main__":
    main()
