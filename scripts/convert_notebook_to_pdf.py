"""
Convert Jupyter Notebook to PDF with visualizations
This script converts the healthcare fraud analysis notebook to a professional PDF
"""

import os
import sys
import subprocess
from pathlib import Path

def convert_notebook_to_pdf(notebook_path, output_path=None):
    """
    Convert Jupyter notebook to PDF using nbconvert
    
    Args:
        notebook_path: Path to the notebook file
        output_path: Optional output PDF path
    """
    print("📓 Converting notebook to PDF...")
    print(f"   Source: {notebook_path}")
    
    if output_path is None:
        output_path = notebook_path.replace('.ipynb', '.pdf')
    
    print(f"   Output: {output_path}")
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        print(f"   Created directory: {output_dir}")
    
    # Get absolute paths
    notebook_path = os.path.abspath(notebook_path)
    output_path = os.path.abspath(output_path)
    
    try:
        # Method 1: Try nbconvert with LaTeX
        print("\n⚙️  Attempting conversion with nbconvert + LaTeX...")
        cmd = [
            'jupyter', 'nbconvert',
            '--to', 'pdf',
            '--output', output_path,
            notebook_path
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ PDF created successfully: {output_path}")
        return output_path
        
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"⚠️  LaTeX conversion failed: {e}")
        print("\n📋 Trying alternative method: HTML to PDF...")
        
        try:
            # Method 2: Convert to HTML first
            html_path = output_path.replace('.pdf', '.html')
            
            # Step 1: Convert to HTML
            cmd_html = [
                'jupyter', 'nbconvert',
                '--to', 'html',
                '--output', html_path,
                notebook_path
            ]
            subprocess.run(cmd_html, check=True)
            print(f"✅ HTML created: {html_path}")
            print("\n💡 To convert HTML to PDF, you can:")
            print("   1. Open the HTML file in a web browser (Chrome/Firefox)")
            print("   2. Press Ctrl+P (or Cmd+P on Mac)")
            print("   3. Select 'Save as PDF' as the destination")
            print(f"   4. Save to: {output_path}")
            
            return html_path
            
        except Exception as e2:
            print(f"❌ HTML conversion also failed: {e2}")
            return None


def check_requirements():
    """Check if required packages are installed"""
    print("🔍 Checking requirements...\n")
    
    requirements = {
        'jupyter': 'jupyter --version',
        'nbconvert': 'jupyter nbconvert --version',
        'pandoc': 'pandoc --version',
    }
    
    missing = []
    for name, cmd in requirements.items():
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ {name}: installed")
                if name == 'pandoc':
                    version = result.stdout.split('\n')[0]
                    print(f"   {version}")
            else:
                missing.append(name)
                print(f"❌ {name}: not found")
        except FileNotFoundError:
            missing.append(name)
            print(f"❌ {name}: not found")
    
    print()
    
    if missing:
        print("⚠️  Missing requirements detected!\n")
        
        if 'jupyter' in missing or 'nbconvert' in missing:
            print("📦 Install Python packages:")
            print("   pip install jupyter nbconvert")
            print()
        
        if 'pandoc' in missing:
            print("📦 Install Pandoc:")
            print("   Ubuntu/Debian/WSL:")
            print("     sudo apt-get update")
            print("     sudo apt-get install pandoc")
            print()
            print("   macOS:")
            print("     brew install pandoc")
            print()
            print("   Windows:")
            print("     Download from: https://pandoc.org/installing.html")
            print("     Or use: choco install pandoc")
            print()
        
        print("📌 For PDF conversion, you also need LaTeX (optional, for better formatting):")
        print("   Ubuntu/Debian/WSL:")
        print("     sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic")
        print()
        print("   macOS:")
        print("     brew install --cask mactex")
        print()
        print("   Windows:")
        print("     Download MiKTeX from https://miktex.org/download")
        print()
        
        return False
    
    return True


def main():
    """Main execution"""
    print("="*70)
    print("Jupyter Notebook to PDF Converter")
    print("="*70)
    print()
    
    # Check requirements
    if not check_requirements():
        print("\n⚠️  Please install missing requirements first.")
        return
    
    # Define paths relative to project root (parent of scripts/)
    project_root = Path(__file__).parent.parent
    notebook_path = project_root / 'notebooks' / 'healthcare_fwa_consolidated_final.ipynb'
    output_path = project_root / 'docs' / 'Healthcare_FWA_Analysis_Notebook.pdf'
    
    # Convert to strings
    notebook_path = str(notebook_path)
    output_path = str(output_path)
    
    if not os.path.exists(notebook_path):
        print(f"❌ Notebook not found: {notebook_path}")
        return
    
    # Convert
    result = convert_notebook_to_pdf(notebook_path, output_path)
    
    print("\n" + "="*70)
    print("Conversion Complete!")
    print("="*70)
    
    if result:
        print(f"\n📄 Output: {result}")
        print("\n💡 Tips:")
        print("   • Review the PDF for formatting and completeness")
        print("   • Combine with the project report for final submission")
        print("   • Check that all visualizations rendered correctly")


if __name__ == '__main__':
    main()
