// ==UserScript==
// @name         Google Flow Auto Studio — Biệt Đội Gara
// @version      1.0
// @description  Tự động nạp kịch bản và tạo video trên flow.google.com
// @author       Antigravity
// @match        https://flow.google.com/*
// ==/UserScript==

(function() {
  const SERVER_URL = 'http://localhost:8765';
  const WIDGET_ID = 'flow-auto-studio-panel';

  if (document.getElementById(WIDGET_ID)) {
    document.getElementById(WIDGET_ID).remove();
  }

  let currentScene = 3;
  let clips = [];
  let currentClipIndex = 0;
  let isRunning = false;

  // Helper an toàn không bao giờ dính lỗi Trusted Types
  function setSafeHTML(element, html) {
    if (window.trustedTypes && window.trustedTypes.createPolicy) {
      try {
        const p = window.trustedTypes.defaultPolicy || window.trustedTypes.createPolicy('flow-safe', { createHTML: s => s });
        element.innerHTML = p.createHTML(html);
        return;
      } catch (e) {}
    }
    try {
      element.innerHTML = html;
    } catch (e) {
      // Nếu browser chặn hoàn toàn innerHTML, dùng fallback parse
      const range = document.createRange();
      element.appendChild(range.createContextualFragment(html));
    }
  }

  // 1. Tạo Giao Diện Floating Widget
  const panel = document.createElement('div');
  panel.id = WIDGET_ID;
  panel.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    width: 360px;
    max-height: 85vh;
    background: rgba(15, 23, 42, 0.95);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(56, 189, 248, 0.4);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    border-radius: 14px;
    z-index: 999999;
    color: #f8fafc;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 13px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  `;

  // Build UI safely with elements
  const header = document.createElement('div');
  header.id = 'flow-header';
  header.style.cssText = 'background: linear-gradient(135deg, #0284c7, #2563eb); padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; cursor: move;';
  
  const titleDiv = document.createElement('div');
  titleDiv.style.cssText = 'font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;';
  titleDiv.textContent = '🎬 Auto Flow Studio';
  
  const closeBtn = document.createElement('button');
  closeBtn.id = 'flow-close-btn';
  closeBtn.style.cssText = 'background: transparent; border: none; color: #fff; font-size: 16px; cursor: pointer; line-height: 1;';
  closeBtn.textContent = '✕';
  
  header.appendChild(titleDiv);
  header.appendChild(closeBtn);
  panel.appendChild(header);

  const bodyDiv = document.createElement('div');
  bodyDiv.style.cssText = 'padding: 14px; display: flex; flex-direction: column; gap: 10px; overflow-y: auto; flex: 1;';

  // Scene select row
  const sceneRow = document.createElement('div');
  sceneRow.style.cssText = 'display: flex; gap: 8px;';

  const startCol = document.createElement('div');
  startCol.style.cssText = 'flex: 1;';
  const sceneLabel = document.createElement('label');
  sceneLabel.style.cssText = 'font-weight: 600; color: #94a3b8; font-size: 11px; text-transform: uppercase;';
  sceneLabel.textContent = 'Từ Cảnh:';
  const sceneSelect = document.createElement('select');
  sceneSelect.id = 'flow-scene-select';
  sceneSelect.style.cssText = 'width: 100%; margin-top: 4px; padding: 7px 10px; background: #1e293b; color: #f8fafc; border: 1px solid #334155; border-radius: 6px; outline: none; font-size: 12px;';
  const optDefault = document.createElement('option');
  optDefault.value = '3';
  optDefault.textContent = 'Đang tải cảnh...';
  sceneSelect.appendChild(optDefault);
  startCol.appendChild(sceneLabel);
  startCol.appendChild(sceneSelect);

  const endCol = document.createElement('div');
  endCol.style.cssText = 'width: 100px;';
  const endLabel = document.createElement('label');
  endLabel.style.cssText = 'font-weight: 600; color: #94a3b8; font-size: 11px; text-transform: uppercase;';
  endLabel.textContent = 'Đến Cảnh:';
  const endSelect = document.createElement('select');
  endSelect.id = 'flow-end-scene';
  endSelect.style.cssText = 'width: 100%; margin-top: 4px; padding: 7px 10px; background: #1e293b; color: #f8fafc; border: 1px solid #334155; border-radius: 6px; outline: none; font-size: 12px;';
  for (let s = 1; s <= 45; s++) {
    const o = document.createElement('option');
    o.value = s;
    o.textContent = `Cảnh ${s}`;
    if (s === 5) o.selected = true;
    endSelect.appendChild(o);
  }
  endCol.appendChild(endLabel);
  endCol.appendChild(endSelect);

  sceneRow.appendChild(startCol);
  sceneRow.appendChild(endCol);
  bodyDiv.appendChild(sceneRow);

  // Button actions row
  const btnRow = document.createElement('div');
  btnRow.style.cssText = 'display: flex; gap: 8px;';
  
  const autoBtn = document.createElement('button');
  autoBtn.id = 'flow-btn-autorun';
  autoBtn.style.cssText = 'flex: 1; padding: 9px; background: #10b981; color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 6px;';
  autoBtn.textContent = '▶️ Tự Động Chạy (Auto)';
  
  const pasteBtn = document.createElement('button');
  pasteBtn.id = 'flow-btn-paste';
  pasteBtn.style.cssText = 'flex: 1; padding: 9px; background: #3b82f6; color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 6px;';
  pasteBtn.textContent = '📋 Dán Clip Này';
  
  btnRow.appendChild(autoBtn);
  btnRow.appendChild(pasteBtn);
  bodyDiv.appendChild(btnRow);

  // Clip list header
  const clipListLabel = document.createElement('div');
  clipListLabel.style.cssText = 'font-weight: 600; color: #94a3b8; font-size: 11px; text-transform: uppercase; margin-top: 4px;';
  clipListLabel.textContent = 'Danh Sách 6 Clip (10s/clip):';
  bodyDiv.appendChild(clipListLabel);

  // Clip list container
  const clipList = document.createElement('div');
  clipList.id = 'flow-clip-list';
  clipList.style.cssText = 'display: flex; flex-direction: column; gap: 6px; max-height: 180px; overflow-y: auto;';
  bodyDiv.appendChild(clipList);

  // Log header
  const logLabel = document.createElement('div');
  logLabel.style.cssText = 'font-weight: 600; color: #94a3b8; font-size: 11px; text-transform: uppercase; margin-top: 4px;';
  logLabel.textContent = 'Nhật Ký Tác Vụ:';
  bodyDiv.appendChild(logLabel);

  // Log container
  const logBox = document.createElement('div');
  logBox.id = 'flow-log';
  logBox.style.cssText = 'background: #090d16; border: 1px solid #1e293b; border-radius: 6px; padding: 8px; font-family: monospace; font-size: 11px; color: #38bdf8; height: 90px; overflow-y: auto; white-space: pre-wrap;';
  logBox.textContent = '[Studio] Sẵn sàng kết nối...\n';
  bodyDiv.appendChild(logBox);

  panel.appendChild(bodyDiv);
  document.body.appendChild(panel);

  // Dragging logic
  const header = panel.querySelector('#flow-header');
  let isDragging = false, startX, startY, initialX, initialY;
  header.addEventListener('mousedown', (e) => {
    isDragging = true;
    startX = e.clientX;
    startY = e.clientY;
    const rect = panel.getBoundingClientRect();
    initialX = rect.left;
    initialY = rect.top;
  });
  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    const dx = e.clientX - startX;
    const dy = e.clientY - startY;
    panel.style.left = `${initialX + dx}px`;
    panel.style.top = `${initialY + dy}px`;
    panel.style.right = 'auto';
  });
  window.addEventListener('mouseup', () => isDragging = false);
  panel.querySelector('#flow-close-btn').addEventListener('click', () => panel.remove());

  function log(msg) {
    const logBox = document.getElementById('flow-log');
    const time = new Date().toLocaleTimeString('vi-VN');
    logBox.textContent += `[${time}] ${msg}\n`;
    logBox.scrollTop = logBox.scrollHeight;
  }

  // 2. Tìm phần tử ô Prompt và nút Generate trên Google Flow
  function findPromptInput() {
    // 1. Tìm textarea
    const textareas = Array.from(document.querySelectorAll('textarea'));
    for (const t of textareas) {
      if (t.offsetParent !== null && !t.disabled) return t;
    }
    // 2. Tìm div contenteditable
    const editables = Array.from(document.querySelectorAll('[contenteditable="true"]'));
    for (const ed of editables) {
      if (ed.offsetParent !== null) return ed;
    }
    return null;
  }

  function findGenerateButton() {
    const buttons = Array.from(document.querySelectorAll('button'));
    for (const b of buttons) {
      if (b.offsetParent === null) continue;
      const text = (b.innerText || b.getAttribute('aria-label') || '').toLowerCase();
      if (text.includes('generate') || text.includes('tạo') || text.includes('run') || text.includes('create')) {
        return b;
      }
    }
    // Fallback: tìm button có icon submit hoặc nằm ngay cạnh prompt input
    for (const b of buttons) {
      if (b.querySelector('svg') && b.offsetParent !== null) {
        const aria = (b.getAttribute('aria-label') || '').toLowerCase();
        if (aria.includes('submit') || aria.includes('send') || aria.includes('arrow') || aria.includes('generate')) {
          return b;
        }
      }
    }
    return null;
  }

  function setPromptValue(element, text) {
    element.focus();
    if (element.tagName.toLowerCase() === 'textarea' || element.tagName.toLowerCase() === 'input') {
      element.value = text;
      element.dispatchEvent(new Event('input', { bubbles: true }));
      element.dispatchEvent(new Event('change', { bubbles: true }));
    } else if (element.isContentEditable) {
      element.innerText = text;
      element.dispatchEvent(new Event('input', { bubbles: true }));
      element.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }

  // 3. Load Scenes và Clips từ local bridge server
  async function loadScenes() {
    try {
      const res = await fetch(`${SERVER_URL}/api/scenes`);
      const data = await res.json();
      const select = document.getElementById('flow-scene-select');
      select.textContent = '';
      data.scenes.forEach(s => {
        const opt = document.createElement('option');
        opt.value = s.num;
        opt.textContent = `${s.id}: ${s.title}`;
        if (s.num === currentScene) opt.selected = true;
        select.appendChild(opt);
      });
      log(`Đã tải danh mục ${data.scenes.length} cảnh.`);
      loadClips(currentScene);
    } catch (err) {
      log(`⚠️ Không kết nối được server ${SERVER_URL}. Bạn đã chạy flow_bridge.py chưa?`);
    }
  }

  async function loadClips(sceneNum) {
    try {
      currentScene = sceneNum;
      const res = await fetch(`${SERVER_URL}/api/clips?scene=${sceneNum}`);
      const data = await res.json();
      clips = data.clips;
      currentClipIndex = 0;
      renderClipList();
      log(`Đã nạp ${clips.length} clip của Cảnh ${sceneNum}.`);
    } catch (err) {
      log(`Lỗi tải clip cảnh ${sceneNum}: ${err.message}`);
    }
  }

  function renderClipList() {
    const list = document.getElementById('flow-clip-list');
    list.textContent = '';
    clips.forEach((c, idx) => {
      const item = document.createElement('div');
      item.style.cssText = `
        padding: 6px 10px;
        background: ${idx === currentClipIndex ? 'rgba(56, 189, 248, 0.15)' : '#1e293b'};
        border: 1px solid ${idx === currentClipIndex ? '#0284c7' : '#334155'};
        border-radius: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
      `;
      
      const titleSpan = document.createElement('span');
      titleSpan.style.cssText = `font-weight: 600; color: ${idx === currentClipIndex ? '#38bdf8' : '#e2e8f0'};`;
      titleSpan.textContent = `Clip ${c.num} (${c.file})`;

      const statusSpan = document.createElement('span');
      statusSpan.id = `clip-status-${idx}`;
      statusSpan.style.cssText = 'font-size: 11px; color: #94a3b8;';
      statusSpan.textContent = 'Sẵn sàng';

      item.appendChild(titleSpan);
      item.appendChild(statusSpan);

      item.addEventListener('click', () => {
        currentClipIndex = idx;
        renderClipList();
      });
      list.appendChild(item);
    });
  }

  // 4. Thực hiện dán prompt của 1 clip
  function pasteCurrentClip() {
    if (!clips[currentClipIndex]) return false;
    const input = findPromptInput();
    if (!input) {
      log('❌ Không tìm thấy ô nhập Prompt trên màn hình Flow!');
      return false;
    }
    const clip = clips[currentClipIndex];
    setPromptValue(input, clip.prompt);
    log(`✅ Đã điền prompt Clip ${clip.num} (${clip.length} ký tự).`);
    const status = document.getElementById(`clip-status-${currentClipIndex}`);
    if (status) {
      status.textContent = 'Đã điền 📝';
      status.style.color = '#38bdf8';
    }
    return true;
  }

  // 5. Tự động hóa tiến trình thông minh
  async function waitForGenerationComplete(timeoutSeconds = 180) {
    log('⏳ Đang theo dõi tiến trình tạo video trên Google Flow...');
    const start = Date.now();
    
    // Đợi 3 giây đầu để Flow kịp kích hoạt trạng thái generating
    await new Promise(r => setTimeout(r, 3000));

    while (isRunning && (Date.now() - start) < timeoutSeconds * 1000) {
      // 1. Kiểm tra xem nút Generate đã hồi phục trạng thái clickable chưa
      const genBtn = findGenerateButton();
      const isGenerating = document.querySelector('[role="progressbar"], .loading-spinner, [aria-busy="true"], .generating');
      
      // Nếu có thanh loading hoặc nút đang disabled -> vẫn đang tạo
      if (isGenerating || (genBtn && genBtn.disabled)) {
        const elapsed = Math.round((Date.now() - start) / 1000);
        if (elapsed % 10 === 0) {
          log(`⏳ Đang xử lý... (${elapsed}s)`);
        }
        await new Promise(r => setTimeout(r, 3000));
        continue;
      }

      // Nếu nút Generate đã sáng lại và không còn spinner -> đã xong!
      log('✅ Phát hiện video đã hoàn thành tạo!');
      return true;
    }
    return false;
  }

  function findExtendButton() {
    // Tìm nút Extend hoặc Nối dài trên video vừa tạo
    const buttons = Array.from(document.querySelectorAll('button, [role="button"]'));
    for (const b of buttons) {
      const text = (b.innerText || b.getAttribute('aria-label') || '').toLowerCase();
      if (text.includes('extend') || text.includes('nối dài') || text.includes('tiếp tục')) {
        return b;
      }
    }
    return null;
  }

  async function runAutoFlow() {
    const autoBtnEl = document.getElementById('flow-btn-autorun');
    if (isRunning) {
      isRunning = false;
      autoBtnEl.textContent = '▶️ Tiếp Tục Chạy';
      autoBtnEl.style.background = '#10b981';
      log('⏸️ Đã tạm dừng tự động.');
      return;
    }

    isRunning = true;
    autoBtnEl.textContent = '⏸️ Tạm Dừng';
    autoBtnEl.style.background = '#ef4444';
    log('🚀 Bắt đầu chu trình tự động sinh video...');

    while (currentClipIndex < clips.length && isRunning) {
      const clip = clips[currentClipIndex];
      log(`👉 Đang chuẩn bị Clip ${clip.num}/${clips.length}...`);
      
      // 1. Nếu từ Clip 2 trở đi, thử tìm và bấm Extend nếu có
      if (clip.num > 1) {
        const extendBtn = findExtendButton();
        if (extendBtn) {
          extendBtn.click();
          log(`🔗 Đã bấm nút Extend cho Clip ${clip.num}.`);
          await new Promise(r => setTimeout(r, 1500));
        }
      }

      // 2. Dán prompt
      const pasted = pasteCurrentClip();
      if (!pasted) {
        log('❌ Dừng tiến trình do không tìm thấy ô nhập prompt.');
        break;
      }

      // 3. Bấm nút Generate
      await new Promise(r => setTimeout(r, 1500));
      const btn = findGenerateButton();
      if (btn && !btn.disabled) {
        btn.click();
        log(`🔘 Đã click nút Generate cho Clip ${clip.num}.`);
        const status = document.getElementById(`clip-status-${currentClipIndex}`);
        if (status) {
          status.textContent = 'Đang tạo ⏳';
          status.style.color = '#f59e0b';
        }
      } else {
        log('⚠️ Nút Generate chưa sẵn sàng hoặc đang bị vô hiệu hóa.');
      }

      // 4. Chờ video hoàn tất thông minh
      await waitForGenerationComplete(180);

      const status = document.getElementById(`clip-status-${currentClipIndex}`);
      if (status) {
        status.textContent = 'Hoàn tất ✅';
        status.style.color = '#10b981';
      }

      // Chuyển sang clip tiếp theo
      currentClipIndex++;
      renderClipList();
      await new Promise(r => setTimeout(r, 2000));

      // Tự động chuyển tiếp sang Cảnh tiếp theo nếu chưa đạt cảnh đích
      if (currentClipIndex >= clips.length) {
        const endScene = parseInt(document.getElementById('flow-end-scene')?.value) || currentScene;
        if (currentScene < endScene && isRunning) {
          log(`🎉 Hoàn tất 6 Clip của Cảnh ${currentScene}!`);
          log(`⏩ Tự động chuyển tiếp sang Cảnh ${currentScene + 1}...`);
          currentScene++;
          const sel = document.getElementById('flow-scene-select');
          if (sel) sel.value = currentScene;
          await loadClips(currentScene);
          await new Promise(r => setTimeout(r, 3000));
          currentClipIndex = 0;
        }
      }
    }

    isRunning = false;
    autoBtnEl.textContent = '▶️ Tự Động Chạy';
    autoBtnEl.style.background = '#10b981';
    log('🎉 Chu trình hoàn tất toàn bộ các cảnh đã chọn!');
  }

  // Gắn sự kiện
  document.getElementById('flow-scene-select').addEventListener('change', (e) => {
    loadClips(parseInt(e.target.value));
  });
  document.getElementById('flow-btn-paste').addEventListener('click', pasteCurrentClip);
  document.getElementById('flow-btn-autorun').addEventListener('click', runAutoFlow);

  loadScenes();
})();
