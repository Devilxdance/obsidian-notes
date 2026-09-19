"""
轻量级 PDF/DOCX 文本提取工具
零额外依赖，仅使用 mineru 已安装的 pypdf / pdfplumber / python-docx
用法: python extract_text.py <文件路径> [-o 输出路径] [--format md|txt] [--images]
"""
import sys, os, argparse, json
from pathlib import Path

# 强制 stdout/stderr 使用 UTF-8，解决 Windows 控制台 GBK 编码问题
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def extract_pdf_pypdf(filepath: str) -> str:
    """用 pypdf 快速提取 PDF 纯文本"""
    from pypdf import PdfReader
    reader = PdfReader(filepath)
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            pages.append(f"## 第 {i+1} 页\n\n{text.strip()}")
    return "\n\n---\n\n".join(pages)

def extract_pdf_plumber(filepath: str) -> str:
    """用 pdfplumber 提取 PDF 文本（保留更多布局信息，推荐）"""
    import pdfplumber
    pages = []
    with pdfplumber.open(filepath) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and text.strip():
                pages.append(f"## 第 {i+1} 页\n\n{text.strip()}")
            # 提取表格
            tables = page.extract_tables()
            if tables:
                for j, table in enumerate(tables):
                    if table:
                        md_table = "| " + " | ".join(table[0]) + " |\n"
                        md_table += "|" + "|".join(["---"] * len(table[0])) + "|\n"
                        for row in table[1:]:
                            md_table += "| " + " | ".join([c or "" for c in row]) + " |\n"
                        pages[-1] += "\n\n" + md_table
    return "\n\n---\n\n".join(pages)

def extract_docx(filepath: str, extract_images: bool = False) -> tuple[str, list]:
    """提取 DOCX 文本，可选标注图片位置"""
    from docx import Document
    doc = Document(filepath)
    paragraphs = []
    images = []
    
    for para in doc.paragraphs:
        style = para.style.name if para.style else ""
        text = para.text.strip()
        if not text:
            paragraphs.append("")
            continue
        
        img_count = sum(1 for run in para.runs 
            if run._element.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}drawing') or
               run._element.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict'))
        
        if img_count:
            if extract_images:
                images.append({"count": img_count, "context": text[:80]})
        
        if style and "Heading" in style:
            level = style.replace("Heading ", "").replace("Heading", "1")
            try:
                level = int(level)
            except ValueError:
                level = 2
            paragraphs.append(f"{'#' * min(level, 4)} {text}")
        elif style and "Title" in style:
            paragraphs.append(f"# {text}")
        else:
            paragraphs.append(text)
    
    # 提取表格
    for i, table in enumerate(doc.tables):
        rows_text = [[cell.text.strip() for cell in row.cells] for row in table.rows]
        if not rows_text or not any(any(cell for cell in row) for row in rows_text):
            continue
        paragraphs.append(f"\n### 表格 {i+1}\n")
        paragraphs.append("| " + " | ".join(rows_text[0]) + " |")
        paragraphs.append("|" + "|".join(["---"] * len(rows_text[0])) + "|")
        for row in rows_text[1:]:
            paragraphs.append("| " + " | ".join(row) + " |")
    
    return "\n\n".join(paragraphs), images

def main():
    parser = argparse.ArgumentParser(
        description="轻量级 PDF/DOCX 文本提取 (Markdown 输出)",
        epilog="示例:\n  python extract_text.py note.pdf -o note.md\n  python extract_text.py doc.docx --images"
    )
    parser.add_argument("file", help="PDF 或 DOCX 文件路径")
    parser.add_argument("-o", "--output", help="输出文件路径（默认输出到同目录同名 .md）")
    parser.add_argument("--engine", choices=["pypdf", "plumber"], default="plumber", 
                        help="PDF 引擎: pypdf(快速) / plumber(精确, 推荐)")
    parser.add_argument("--images", action="store_true", help="标注 DOCX 中图片位置")
    parser.add_argument("--stdout", action="store_true", help="强制输出到标准输出")
    args = parser.parse_args()
    
    filepath = Path(args.file).resolve()
    if not filepath.exists():
        print(f"[error] 文件不存在: {filepath}", file=sys.stderr)
        sys.exit(1)
    
    suffix = filepath.suffix.lower()
    print(f"[info] 提取 {filepath.name} ...", file=sys.stderr)
    
    if suffix == ".pdf":
        if args.engine == "pypdf":
            text = extract_pdf_pypdf(str(filepath))
        else:
            text = extract_pdf_plumber(str(filepath))
        images = []
    elif suffix in (".docx", ".doc"):
        text, images = extract_docx(str(filepath), extract_images=args.images)
    else:
        print(f"[error] 不支持的文件格式: {suffix}", file=sys.stderr)
        sys.exit(1)
    
    if not text.strip():
        print("[warn] 未能提取到文本（可能是扫描版 PDF，需要 mineru OCR）", file=sys.stderr)
    
    # 确定输出路径
    if args.stdout:
        output = None
    elif args.output:
        output = Path(args.output)
    else:
        output = filepath.with_suffix(".md")
    
    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[ok] → {output}", file=sys.stderr)
        if images:
            print(f"[info] 检测到 {len(images)} 处图片", file=sys.stderr)
    else:
        print(text)

if __name__ == "__main__":
    main()
