import os
import sys
import shutil
import win32com.client

python_exe = r"C:\Users\sanja\.gemini\antigravity\scratch\swiggy_instamart_discovery\.venv\Scripts\python.exe"
work_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"

def convert_pptx_to_pdf(pptx_path, pdf_path):
    print(f"Converting {pptx_path} to vector PDF at {pdf_path}...")
    # Kill any open PowerPoint processes first to avoid file lock
    os.system("taskkill /f /im POWERPNT.EXE 2>nul")
    
    ppt_app = win32com.client.Dispatch("PowerPoint.Application")
    ppt_app.Visible = True
    try:
        abs_pptx = os.path.abspath(pptx_path)
        abs_pdf = os.path.abspath(pdf_path)
        deck = ppt_app.Presentations.Open(abs_pptx, WithWindow=False)
        # Format 32 is ppSaveAsPDF (Vector PDF format)
        deck.SaveAs(abs_pdf, 32)
        deck.Close()
        print(f"Successfully created vector PDF: {abs_pdf}")
    finally:
        ppt_app.Quit()

if __name__ == "__main__":
    # 1. Run build script to generate PowerPoint deck
    print("Building PowerPoint deck...")
    import build_final_submission_pptx
    build_final_submission_pptx.create_presentation()
    
    # 2. Make space-free version copies
    src_pptx = os.path.join(work_dir, "NL Myntra.pptx")
    dst_pptx_nodash = os.path.join(work_dir, "NL_Myntra.pptx")
    shutil.copyfile(src_pptx, dst_pptx_nodash)
    print("Created NL_Myntra.pptx copy.")
    
    # 3. Export PDF
    src_pdf = os.path.join(work_dir, "NL Myntra.pdf")
    dst_pdf_nodash = os.path.join(work_dir, "NL_Myntra.pdf")
    
    convert_pptx_to_pdf(src_pptx, src_pdf)
    shutil.copyfile(src_pdf, dst_pdf_nodash)
    
    # 4. Copy to Desktop & Downloads for user local access
    user_desktop = r"C:\Users\sanja\Desktop"
    user_downloads = r"C:\Users\sanja\Downloads"
    
    for folder in [user_desktop, user_downloads]:
        shutil.copy(src_pptx, os.path.join(folder, "NL Myntra.pptx"))
        shutil.copy(dst_pptx_nodash, os.path.join(folder, "NL_Myntra.pptx"))
        shutil.copy(src_pdf, os.path.join(folder, "NL Myntra.pdf"))
        shutil.copy(dst_pdf_nodash, os.path.join(folder, "NL_Myntra.pdf"))
        print(f"Copied PPTX and PDF files to {folder}")
