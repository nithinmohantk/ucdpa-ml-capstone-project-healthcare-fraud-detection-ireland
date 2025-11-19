"""
Extract all PNG images from Jupyter notebook for PDF report generation
Run this script after executing all cells in the notebook
"""

import json
import base64
from pathlib import Path
import sys

def extract_images_from_notebook(notebook_path, output_dir='docs/visualizations'):
    """
    Extract all PNG images from a Jupyter notebook
    
    Args:
        notebook_path: Path to the .ipynb file
        output_dir: Directory to save extracted images
    """
    # Convert to Path objects
    notebook_path = Path(notebook_path)
    output_dir = Path(output_dir)
    
    # Read notebook
    print(f"📖 Reading notebook: {notebook_path}")
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Output directory: {output_dir}")
    
    # Extract all PNG images
    viz_count = 0
    extracted_images = []
    
    print("\n" + "="*80)
    print("Extracting PNG Images:")
    print("="*80)
    
    for cell_idx, cell in enumerate(nb['cells'], 1):
        if cell.get('cell_type') == 'code':
            outputs = cell.get('outputs', [])
            
            for output_idx, output in enumerate(outputs):
                if 'data' in output and 'image/png' in output.get('data', {}):
                    viz_count += 1
                    png_data = output['data']['image/png']
                    
                    # Remove newlines from base64 data
                    png_data = png_data.replace('\n', '')
                    
                    # Decode and save
                    try:
                        img_bytes = base64.b64decode(png_data)
                        output_path = output_dir / f'viz_cell_{cell_idx:02d}_{viz_count:02d}.png'
                        
                        with open(output_path, 'wb') as f:
                            f.write(img_bytes)
                        
                        exec_count = cell.get('execution_count', 'N/A')
                        if exec_count != 'N/A':
                            exec_count = str(exec_count)
                        
                        # Get cell preview
                        code = ''.join(cell.get('source', []))
                        code_preview = code[:70].replace('\n', ' ').strip()
                        
                        print(f"{viz_count:2d}. Cell {cell_idx:2d} (exec={exec_count:>3s}): {output_path.name}")
                        print(f"    Code: {code_preview}...")
                        
                        extracted_images.append({
                            'number': viz_count,
                            'cell': cell_idx,
                            'exec_count': exec_count,
                            'filename': output_path.name,
                            'path': str(output_path),
                            'code_preview': code_preview
                        })
                        
                    except Exception as e:
                        print(f"    ❌ Error saving image: {e}")
    
    print("="*80)
    print(f"\n✅ Extracted {viz_count} images to {output_dir}/")
    
    return extracted_images


def generate_image_manifest(images, output_path='docs/visualizations/IMAGE_MANIFEST.md'):
    """Generate a markdown manifest of all extracted images"""
    
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Extracted Notebook Visualizations\n\n")
        f.write(f"**Total Images:** {len(images)}\n\n")
        f.write("---\n\n")
        
        for img in images:
            f.write(f"## {img['number']}. {img['filename']}\n\n")
            f.write(f"- **Cell Number:** {img['cell']}\n")
            f.write(f"- **Execution Count:** {img['exec_count']}\n")
            f.write(f"- **File Path:** `{img['path']}`\n")
            f.write(f"- **Code Preview:** `{img['code_preview']}...`\n")
            f.write(f"\n---\n\n")
    
    print(f"📄 Image manifest saved to: {output_path}")


def main():
    """Main execution"""
    # Get project root (parent of scripts directory)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Notebook path
    notebook_path = project_root / 'notebooks' / 'healthcare_fwa_consolidated_final.ipynb'
    
    # Output directory
    output_dir = project_root / 'docs' / 'visualizations'
    
    if not notebook_path.exists():
        print(f"❌ Notebook not found: {notebook_path}")
        print("\n💡 Usage:")
        print(f"   python {Path(__file__).name} [notebook_path] [output_dir]")
        return 1
    
    print("="*80)
    print("Jupyter Notebook Image Extractor")
    print("="*80)
    print()
    
    # Extract images
    images = extract_images_from_notebook(notebook_path, output_dir)
    
    if images:
        # Generate manifest
        manifest_path = output_dir / 'IMAGE_MANIFEST.md'
        generate_image_manifest(images, manifest_path)
        
        print("\n" + "="*80)
        print("Extraction Complete!")
        print("="*80)
        print(f"\n📊 Total images: {len(images)}")
        print(f"📁 Location: {output_dir}/")
        print(f"📄 Manifest: {manifest_path}")
        print("\n💡 You can now run generate_report.py to create the PDF with these images")
    else:
        print("\n⚠️  No images found in notebook!")
        print("\n💡 Make sure to:")
        print("   1. Open the notebook in Jupyter")
        print("   2. Run all cells (Cell → Run All)")
        print("   3. Save the notebook (Ctrl+S)")
        print("   4. Run this script again")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
