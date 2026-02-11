# HTML 轉 PDF 工具 (HTML to PDF Converter)

這個專案包含兩個 Python 程式，可以協助你將 HTML 檔案轉換為高品質的 PDF，並將它們合併成一個單一的檔案。

## 功能介紹

*   **`html_to_pdf.py`**: 
    *   自動搜尋目錄下所有的 `.html` 檔案。
    *   使用 Playwright (Chromium 核心) 進行渲染，確保 PDF 樣式與網頁一致。
    *   輸出對應的 `.pdf` 檔案。

*   **`merge_pdfs.py`**: 
    *   自動搜尋目錄下所有的 `.pdf` 檔案。
    *   依照檔名排序 (例如 `page_001`, `page_002`...)。
    *   將所有 PDF 合併為一個檔案：`merged_output.pdf`。

## 環境準備 (第一次使用時)

1.  確保已安裝 Python。
2.  安裝必要的 Python 套件：
    ```bash
    pip install -r requirements.txt
    ```
    (或者手動安裝：`pip install playwright pypdf`)
    
3.  安裝瀏覽器核心 (如果尚未安裝)：
    ```bash
    playwright install chromium
    ```

## 使用步驟

### 步驟 1: 轉換 HTML
確保你的 `.html` 檔案都在這個資料夾中，然後執行：

```bash
python html_to_pdf.py
```

### 步驟 2: 合併 PDF
轉換完成後，執行以下指令將它們合併：

```bash
python merge_pdfs.py
```

### 步驟 3: 查看結果
完成後，你可以在資料夾中找到 **`merged_output.pdf`**。

---
**注意**: 如果遇到權限錯誤或瀏覽器無法啟動，請確認已正確執行 `playwright install chromium`。
