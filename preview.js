/* SPDX-License-Identifier: MIT */
"use strict";

// Optional owner/repository for a custom domain. Standard GitHub Pages is automatic.
const PUBLISHED_REPOSITORY = "";

(() => {
  const states = {
    idle: {row: 0, durations: [280,110,110,140,140,320], label: "待机 · Idle"},
    "running-right": {row: 1, durations: [120,120,120,120,120,120,120,220], label: "向右走 · Walking right"},
    "running-left": {row: 2, durations: [120,120,120,120,120,120,120,220], label: "向左走 · Walking left"},
    waving: {row: 3, durations: [140,140,140,280], label: "挥挥手 · Hello"},
    jumping: {row: 4, durations: [140,140,140,140,280], label: "跳一下 · Jumping"},
    failed: {row: 5, durations: [140,140,140,140,140,140,140,240], label: "有点为难 · Oops"},
    waiting: {row: 6, durations: [150,150,150,150,150,260], label: "等你回应 · Waiting"},
    running: {row: 7, durations: [120,120,120,120,120,220], label: "思考中 · Thinking"},
    review: {row: 8, durations: [150,150,150,150,150,280], label: "检查结果 · Review"}
  };
  const directions = ["向上","右上偏上","右上","右上偏右","向右","右下偏右","右下","右下偏下","向下","左下偏下","左下","左下偏左","向左","左上偏左","左上","左上偏上"];
  const $ = (id) => document.getElementById(id);
  const canvas = $("pet");
  const ctx = canvas.getContext("2d");
  const image = new Image();
  let current = "idle", frame = 0, elapsed = 0, last = 0, lookIndex = null;
  let paused = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const stateButtons = [...document.querySelectorAll("[data-state]")];
  document.querySelectorAll('a[href="#install-help"]').forEach((link) => link.addEventListener("click", () => {
    $("install-help").open = true;
  }));

  function draw() {
    if (!image.complete || !image.naturalWidth) return;
    const row = lookIndex === null ? states[current].row : 9 + Math.floor(lookIndex / 8);
    const col = lookIndex === null ? frame : lookIndex % 8;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.imageSmoothingEnabled = true;
    ctx.imageSmoothingQuality = "high";
    ctx.drawImage(image, col * 192, row * 208, 192, 208, 0, 0, canvas.width, canvas.height);
  }

  function selectState(id) {
    current = id; frame = 0; elapsed = 0; lookIndex = null;
    $("state-label").textContent = states[id].label;
    canvas.setAttribute("aria-label", "GPT 小龙女：" + states[id].label);
    stateButtons.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.state === id)));
    draw();
  }

  function selectLook(index) {
    lookIndex = Math.max(0, Math.min(15, index));
    $("direction").value = lookIndex;
    const label = directions[lookIndex] + " · " + (lookIndex * 22.5) + "°";
    $("direction-value").textContent = label;
    $("state-label").textContent = "环视 · " + label;
    canvas.setAttribute("aria-label", "GPT 小龙女看向" + directions[lookIndex]);
    stateButtons.forEach((button) => button.setAttribute("aria-pressed", "false"));
    draw();
  }

  function tick(now) {
    const delta = last ? Math.min(now - last, 100) : 0;
    last = now;
    if (!paused && !document.hidden && lookIndex === null) {
      elapsed += delta;
      const durations = states[current].durations;
      while (elapsed >= durations[frame]) {
        elapsed -= durations[frame];
        frame = (frame + 1) % durations.length;
      }
      draw();
    }
    requestAnimationFrame(tick);
  }

  stateButtons.forEach((button) => button.addEventListener("click", () => selectState(button.dataset.state)));
  $("direction").addEventListener("input", (event) => selectLook(Number(event.target.value)));
  $("scale").addEventListener("input", (event) => {
    const value = Number(event.target.value);
    canvas.style.width = (192 * value) + "px";
    $("scale-value").textContent = value.toFixed(1) + "×";
  });
  $("pause").textContent = paused ? "播放" : "暂停";
  $("pause").addEventListener("click", () => {
    paused = !paused;
    $("pause").textContent = paused ? "播放" : "暂停";
  });
  document.querySelectorAll("[data-bg]").forEach((button) => button.addEventListener("click", () => {
    $("stage").className = "stage" + (button.dataset.bg === "light" ? "" : " " + button.dataset.bg);
    document.querySelectorAll("[data-bg]").forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
  }));
  $("stage").addEventListener("pointermove", (event) => {
    if (!$("follow").checked) return;
    const box = canvas.getBoundingClientRect();
    const dx = event.clientX - box.left - box.width / 2;
    const dy = event.clientY - box.top - box.height / 3;
    const angle = (Math.atan2(dx, -dy) * 180 / Math.PI + 360) % 360;
    selectLook(Math.round(angle / 22.5) % 16);
  });
  $("stage").addEventListener("pointerleave", () => {
    if ($("follow").checked) selectState(current);
  });
  $("follow").addEventListener("change", () => {
    if (!$("follow").checked) selectState(current);
  });

  function repository() {
    if (/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(PUBLISHED_REPOSITORY)) return PUBLISHED_REPOSITORY;
    const host = location.hostname;
    if (!host.endsWith(".github.io")) return null;
    const owner = host.slice(0, -".github.io".length);
    const path = location.pathname.split("/").filter(Boolean);
    const name = path[0];
    if (!name || name === "index.html") return null;
    const candidate = owner + "/" + name;
    return /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(candidate) ? candidate : null;
  }

  const repo = repository();
  if (repo) {
    const query = new URLSearchParams({
      name: "GPT小龙女",
      description: "银白长发、紫眸双角与白紫裙装的Q版小龙女。",
      imageUrl: "https://raw.githubusercontent.com/" + repo + "/main/spritesheet.png",
      spriteVersionNumber: "2"
    });
    $("install-link").href = "codex://pets/install?" + query.toString();
    $("install-link").hidden = false;
    $("install-note").textContent = "在电脑上打开安装链接，由客户端确认添加。也可以下载文件，按安装说明手动安装。";
    $("source-link").href = "https://github.com/" + repo;
    $("source-link").textContent = "GitHub ↗";
  }

  image.onload = () => {
    $("status").textContent = "九组动作 · 十六个视线方向";
    draw();
    requestAnimationFrame(tick);
  };
  image.onerror = () => {
    $("status").textContent = "图集未加载，请确认 spritesheet.png 与页面在同一目录。";
    $("status").setAttribute("role", "alert");
  };
  image.src = "spritesheet.png";
})();
