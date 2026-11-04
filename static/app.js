import {
  EditorView, basicSetup, EditorState, keymap, indentWithTab, indentUnit, python, rust, oneDark,
  StreamLanguage, lua, javascript,
} from "/vendor/codemirror.js";
import { marked } from "/vendor/marked.js";

const app = document.getElementById("app");
const LANG_INFO = {
  python: { icon: "🐍", blurb: "Runs right in your browser.", unit: "    " },
  gdscript: { icon: "🎮", blurb: "The language of the Godot game engine.", unit: "\t" },
  lua: { icon: "🌙", blurb: "Small scripting language used in Roblox, LÖVE and Defold. Runs in your browser.", unit: "    " },
  typescript: { icon: "🔷", blurb: "JavaScript with types. Runs in your browser.", unit: "  " },
  rust: { icon: "🦀", blurb: "Fast, safe systems programming.", unit: "    " },
  nix: { icon: "❄️", blurb: "The language NixOS, nixpkgs and flakes are written in.", unit: "  " },
  git: { icon: "🌿", blurb: "Track changes, branch, merge and share your code.", unit: "  " },
  pyhost: { icon: "🧪", blurb: "Python with real AI libraries, run on your computer.", unit: "    " },
};
const HOST_TOOL = { gdscript: "Godot", rust: "Rust", nix: "Nix", git: "Git" };

// Small highlighters for Nix and for the shell-style Git lesson scripts.
const nixLang = {
  name: "nix",
  token(stream, state) {
    // state.quote is the closing quote of the string we're in: " or ''
    if (state.quote) {
      if (stream.match("${")) { if (stream.skipTo("}")) stream.next(); else stream.skipToEnd(); return "meta"; }
      while (!stream.eol()) {
        if (stream.match(state.quote)) { state.quote = null; break; }
        if (stream.match("${", false)) break;
        if (stream.next() === "\\" && state.quote === '"') stream.next();
      }
      return "string";
    }
    if (stream.eatSpace()) return null;
    if (stream.match("#")) { stream.skipToEnd(); return "comment"; }
    if (stream.match('"')) { state.quote = '"'; return "string"; }
    if (stream.match("''")) { state.quote = "''"; return "string"; }
    if (stream.match(/^\d+(\.\d+)?/)) return "number";
    if (stream.match(/^(let|in|rec|with|inherit|if|then|else|assert|or)\b/)) return "keyword";
    if (stream.match(/^(true|false|null)\b/)) return "atom";
    if (stream.match(/^(builtins|import|map|throw|toString|pkgs|lib)\b/)) return "builtin";
    if (stream.match(/^[A-Za-z_][\w'-]*/)) return "variable";
    if (stream.match(/^(\.\/|\.\.\/|<)[\w./-]*>?/)) return "string";
    stream.next();
    return null;
  },
  startState: () => ({ quote: null }),
  languageData: { commentTokens: { line: "#" } },
};
const shellLang = {
  name: "shell",
  token(stream) {
    if (stream.eatSpace()) return null;
    if (stream.match("#")) { stream.skipToEnd(); return "comment"; }
    if (stream.match(/^"([^"\\]|\\.)*"?/) || stream.match(/^'[^']*'?/)) return "string";
    if (stream.sol() || stream.string.slice(0, stream.start).trim() === "") {
      if (stream.match(/^\S+/)) return "keyword";
    }
    if (stream.match(/^--?[\w-]+/)) return "attribute";
    if (stream.match(/^>>?/)) return "operator";
    stream.match(/^\S+/) || stream.next();
    return null;
  },
  languageData: { commentTokens: { line: "#" } },
};
const prefersDark = window.matchMedia("(prefers-color-scheme: dark)");

// ------------------------------------------------------------------ API ---

function storedPin() {
  try { return localStorage.getItem("codequest-pin") || ""; } catch { return ""; }
}

async function api(path, body) {
  const res = await fetch(path, {
    method: body ? "POST" : "GET",
    headers: { "Content-Type": "application/json", "X-CodeQuest-Pin": storedPin() },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (res.status === 401) {
    await askForPin();
    return api(path, body);
  }
  if (!res.ok) throw new Error((await res.json().catch(() => ({}))).error || res.statusText);
  return res.json();
}

function askForPin() {
  const dialog = document.getElementById("pin-dialog");
  const input = document.getElementById("pin-input");
  input.value = "";
  return new Promise((resolve) => {
    dialog.addEventListener("close", () => {
      try { localStorage.setItem("codequest-pin", input.value.trim()); } catch {}
      resolve();
    }, { once: true });
    dialog.showModal();
  });
}

// --------------------------------------------------------------- header ---

let lastProfile = null;

function showProfile(p) {
  if (!p) return;
  lastProfile = p;
  document.getElementById("stats").hidden = false;
  document.getElementById("level").textContent = `Lv ${p.level}`;
  document.getElementById("xp").textContent = `${p.xp} XP`;
  document.getElementById("xpfill").style.width = `${Math.round((p.level_xp / p.level_needed) * 100)}%`;
  const streak = document.getElementById("streak");
  streak.textContent = `🔥 ${p.streak}`;
  streak.classList.toggle("cold", !p.practised_today);
  streak.title = p.practised_today ? "Days in a row. You practised today!" : "Finish a lesson today to keep your streak.";
}

function toast(text) {
  const el = document.getElementById("toast");
  el.textContent = text;
  el.hidden = false;
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => (el.hidden = true), 2500);
}

// ---------------------------------------------------------------- router ---

function navigate(url) {
  history.pushState({}, "", url);
  route();
}

document.addEventListener("click", (e) => {
  const a = e.target.closest("a[data-link]");
  if (a && !e.metaKey && !e.ctrlKey) {
    e.preventDefault();
    navigate(a.getAttribute("href"));
  }
});
window.addEventListener("popstate", route);

function route() {
  const m = location.pathname.match(/^\/learn\/([\w-]+)\/([\w-]+)/);
  if (m) return showLesson(m[1], m[2]);
  if (location.pathname === "/review") return showReviews();
  return showHome();
}

// ------------------------------------------------------------------ home ---

async function showHome() {
  document.title = "CodeQuest";
  const { courses, profile, reviews_due: due } = await api("/api/courses");
  showProfile(profile);
  const info = await fetch("/api/info").then((r) => r.json());
  const onLan = info.urls.length > 0 && ["localhost", "127.0.0.1"].includes(location.hostname);

  app.innerHTML = `
    <section class="hero">
      <div>
        <h1>Choose your quest</h1>
        <p>${profile.completed ? `${profile.completed} ${profile.completed === 1 ? "lesson" : "lessons"} cleared. Keep going!` : "Pick a language and clear your first lesson."}</p>
      </div>
      ${onLan ? `<button class="btn" id="phone-btn">📱 Open on phone</button>` : ""}
    </section>
    ${due.length ? `<a class="review-card" href="/review" data-link>🧠 <strong>${due.length} review ${due.length === 1 ? "question" : "questions"} due</strong>
      <span class="muted">A 2-minute warm-up that makes old lessons stick.</span></a>` : ""}
    ${groupCourses(courses).map(([track, levels]) => `
      <section class="track">
        <h2 class="track-title">${escapeHtml(track)}</h2>
        ${levels.map(([level, list]) => `
          ${level ? `<h3 class="level-title">${escapeHtml(level)}</h3>` : ""}
          <div class="courses">${list.map(courseCard).join("")}</div>`).join("")}
      </section>`).join("")}`;
  if (onLan) document.getElementById("phone-btn").onclick = () => showPhoneDialog(info.urls);
}

// Courses arrive sorted by order; keep that order for tracks and levels (by their first course).
function groupCourses(courses) {
  const tracks = new Map();
  for (const c of courses) {
    if (!tracks.has(c.track)) tracks.set(c.track, new Map());
    const levels = tracks.get(c.track);
    if (!levels.has(c.level)) levels.set(c.level, []);
    levels.get(c.level).push(c);
  }
  return [...tracks].map(([track, levels]) => [track, [...levels]]);
}

function courseCard(c) {
  const done = c.lessons.filter((l) => l.completed).length;
  const next = c.lessons.find((l) => !l.completed) || c.lessons[0];
  const meta = LANG_INFO[c.lang];
  const icon = c.icon || meta.icon, blurb = c.blurb || meta.blurb;
  const missing = HOST_TOOL[c.lang];
  return `
    <article class="course ${c.available ? "" : "unavailable"}">
      <header>
        <span class="icon" aria-hidden="true">${icon}</span>
        <div>
          <h2>${escapeHtml(c.name)}</h2>
          ${c.topic ? `<span class="chip">${escapeHtml(c.topic)}</span>` : ""}
          <p>${escapeHtml(blurb)}</p>
        </div>
      </header>
      <div class="progress" role="progressbar" aria-valuenow="${done}" aria-valuemax="${c.lessons.length}">
        <span style="width:${c.lessons.length ? (done / c.lessons.length) * 100 : 0}%"></span>
      </div>
      <p class="muted">${done} of ${c.lessons.length} lessons</p>
      ${c.available ? "" : `<p class="warn">${missing} isn't installed on the computer running CodeQuest yet. You can read the lessons, but Run won't work.</p>`}
      <ol class="lessons">
        ${c.lessons.map((l) => `
          <li class="${l.completed ? "done" : ""}">
            <a href="/learn/${c.id}/${l.slug}" data-link>
              <span class="mark">${l.completed ? "✓" : ""}</span>
              <span class="title">${escapeHtml(l.title)}</span>
              <span class="mins">~${l.minutes} min</span>
              <span class="reward">${l.xp} XP</span>
            </a>
          </li>`).join("")}
      </ol>
      ${next ? `<a class="btn primary" href="/learn/${c.id}/${next.slug}" data-link>${done ? "Continue" : "Start"}</a>` : ""}
    </article>`;
}

function showPhoneDialog(urls) {
  const qrBox = document.getElementById("qr");
  qrBox.innerHTML = "";
  if (window.qrcode) {
    const qr = window.qrcode(0, "M");
    qr.addData(urls[0]);
    qr.make();
    qrBox.innerHTML = qr.createSvgTag({ cellSize: 6, margin: 2, scalable: true });
  }
  document.getElementById("lan-urls").innerHTML = urls.map((u) => `<li><code>${u}</code></li>`).join("");
  document.getElementById("phone-dialog").showModal();
}

// ---------------------------------------------------------------- lesson ---

let editor = null;
let saveTimer = null;

async function showLesson(course, slug) {
  const lesson = await api(`/api/lesson/${course}/${slug}`);
  const lang = lesson.lang;
  document.title = `${lesson.title} · CodeQuest`;
  if (lastProfile === null) api("/api/courses").then((d) => showProfile(d.profile));

  app.innerHTML = `
    <div class="lesson-head">
      <a href="/" data-link class="back">← Quests</a>
      <span class="muted">${escapeHtml(lesson.course_name)} · Lesson ${lesson.index} of ${lesson.total} · ~${lesson.minutes} min</span>
      <span class="reward-pill ${lesson.completed ? "done" : ""}">${lesson.completed ? "✓ Cleared" : `+${lesson.xp} XP`}</span>
    </div>
    <div class="tabs" role="tablist">
      <button role="tab" data-tab="read" aria-selected="true">Lesson</button>
      <button role="tab" data-tab="code" aria-selected="false">Code</button>
    </div>
    <div class="lesson-grid" data-show="read">
      <article class="lesson-body pane-read">${marked.parse(lesson.body)}</article>
      <section class="workbench pane-code">
        <div class="editor" id="editor"></div>
        <div class="symbols" aria-label="Insert symbol">
          ${["Tab", "(", ")", ":", '"', "[", "]", "{", "}", "=", ";", "."].map((s) =>
            `<button type="button" data-sym="${s === '"' ? "&quot;" : s}">${s === "Tab" ? "⇥ Tab" : escapeHtml(s)}</button>`).join("")}
        </div>
        <div class="actions">
          <button class="btn" id="run">▶ Run</button>
          <button class="btn primary" id="submit">Submit</button>
          <span class="spacer"></span>
          ${lesson.has_solution ? `<button class="btn ghost" id="hint">💡 Hint</button>` : ""}
          <button class="btn ghost" id="solution" ${lesson.solution ? "" : "hidden"}>Solution</button>
          <button class="btn ghost" id="reset">Reset</button>
        </div>
        <div class="hints" id="hints" aria-live="polite"></div>
        <div class="output" id="output" aria-live="polite">
          <p class="muted">${browserRunners[lang] ? "Your output will show here." : "Your code runs on the computer hosting CodeQuest. Output shows here."}</p>
        </div>
      </section>
    </div>`;

  // Tabs only matter on narrow screens; on wide screens both panes show.
  const grid = app.querySelector(".lesson-grid");
  const tabs = app.querySelectorAll("[data-tab]");
  const selectTab = (name) => {
    grid.dataset.show = name;
    tabs.forEach((t) => t.setAttribute("aria-selected", String(t.dataset.tab === name)));
    if (name === "code") editor?.focus();
  };
  tabs.forEach((t) => (t.onclick = () => selectTab(t.dataset.tab)));
  app.querySelector(".lesson-body").insertAdjacentHTML("beforeend",
    `<button class="btn primary to-code" type="button">Start coding →</button>`);
  app.querySelector(".to-code").onclick = () => selectTab("code");

  createEditor(lesson.code, lang, (code) => {
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => api("/api/save", { course, slug, code }).catch(() => {}), 1200);
  });

  app.querySelectorAll("[data-sym]").forEach((b) => {
    b.onmousedown = (e) => e.preventDefault(); // keep the editor focused and the keyboard open
    b.onclick = () => insertText(b.dataset.sym === "Tab" ? LANG_INFO[lang].unit : b.dataset.sym);
  });
  document.getElementById("run").onclick = () => execute(lesson, "run");
  document.getElementById("submit").onclick = () => execute(lesson, "submit");
  document.getElementById("reset").onclick = () => {
    if (confirm("Replace your code with the starter code?")) setCode(lesson.starter);
  };
  const solBtn = document.getElementById("solution");
  solBtn.onclick = () => {
    if (confirm("Replace your code with the official solution?")) setCode(lesson.solution);
  };
  const hintBtn = document.getElementById("hint");
  let hintsUsed = 0;
  if (hintBtn) hintBtn.onclick = async () => {
    const h = await api("/api/hint", { course, slug, code: editor.state.doc.toString(), n: hintsUsed++ });
    document.getElementById("hints").insertAdjacentHTML("beforeend", `<div class="hint"><strong>Hint ${hintsUsed}:</strong> ${escapeHtml(h.hint)}
      ${h.line ? `<pre>${escapeHtml(h.line)}</pre>` : ""}</div>`);
    hintBtn.textContent = "💡 Another hint";
    if (h.solution && !lesson.solution) {
      lesson.solution = h.solution;
      solBtn.hidden = false;
    }
  };
  setUpParts(app.querySelector(".lesson-body"), lesson);
  setUpReview(app.querySelector(".lesson-body"), lesson);
  setUpChecklists(app.querySelector(".lesson-body"), lesson);

  browserRunners[lang]?.warmUp();
}

function createEditor(doc, lang, onChange) {
  // GDScript reads well with Python highlighting.
  const language = lang === "rust" ? rust() : lang === "lua" ? StreamLanguage.define(lua)
    : lang === "typescript" ? javascript({ typescript: true })
    : lang === "nix" ? StreamLanguage.define(nixLang) : lang === "git" ? StreamLanguage.define(shellLang) : python();
  editor = new EditorView({
    parent: document.getElementById("editor"),
    state: EditorState.create({
      doc,
      extensions: [
        basicSetup,
        keymap.of([indentWithTab]),
        indentUnit.of(LANG_INFO[lang].unit),
        EditorState.tabSize.of(4),
        language,
        prefersDark.matches ? oneDark : [],
        EditorView.updateListener.of((u) => u.docChanged && onChange(u.state.doc.toString())),
        EditorView.contentAttributes.of({ autocapitalize: "off", autocorrect: "off", spellcheck: "false" }),
      ],
    }),
  });
}

function insertText(text) {
  const { from, to } = editor.state.selection.main;
  editor.dispatch({ changes: { from, to, insert: text }, selection: { anchor: from + text.length } });
  editor.focus();
}

function setCode(code) {
  editor.dispatch({ changes: { from: 0, to: editor.state.doc.length, insert: code } });
}

async function execute(lesson, mode) {
  const out = document.getElementById("output");
  const buttons = [document.getElementById("run"), document.getElementById("submit")];
  buttons.forEach((b) => (b.disabled = true));
  const code = editor.state.doc.toString();
  const runner = browserRunners[lesson.lang];
  out.innerHTML = `<p class="muted">${lesson.lang === "rust" ? "Compiling…" : runner && !runner.isReady ? `Starting ${langName(lesson.lang)} (first time only)…` : "Running…"}</p>`;

  let result;
  const started = Date.now();
  const ticker = lesson.lang === "gdscript" && setInterval(() => {
    const secs = Math.round((Date.now() - started) / 1000);
    out.innerHTML = `<p class="muted">${mode === "submit" ? "Godot is playing your code against the check" : "Godot is running your code"}… ${secs} s
      <span class="busy"><span style="width:${Math.min(100, secs * 12)}%"></span></span></p>`;
  }, 500);
  try {
    if (runner) {
      result = await runner.run({ code, check: lesson.check, expected: lesson.expected_output, prelude: lesson.prelude, mode });
      if (mode === "submit") Object.assign(result, await api("/api/complete", {
        course: lesson.course, slug: lesson.slug, code, passed: result.passed,
      }));
    } else {
      result = await api("/api/run", { course: lesson.course, slug: lesson.slug, code, mode });
    }
  } catch (err) {
    result = { output: "", error: String(err.message || err) };
  } finally {
    buttons.forEach((b) => (b.disabled = false));
    if (ticker) clearInterval(ticker);
  }
  renderResult(out, result, mode, lesson);
}

function renderResult(out, r, mode, lesson) {
  let html = "";
  if (r.output) html += `<pre class="stdout">${escapeHtml(r.output)}</pre>`;
  else if (!r.error) html += `<p class="muted">(no output)</p>`;
  if (r.error) html += `<pre class="stderr">${escapeHtml(r.error)}</pre>`;
  if (r.warnings && !r.error) html += `<details><summary>Warnings</summary><pre class="warn-text">${escapeHtml(r.warnings)}</pre></details>`;

  if (mode === "submit" && r.total > 1) {
    html = `<div class="parts" title="Checks passed"><span style="width:${(r.done / r.total) * 100}%"></span></div>
      <p class="parts-text">${"✓".repeat(r.done)}${"○".repeat(r.total - r.done)} ${r.done} of ${r.total} checks passed</p>` + html;
  }
  if (mode === "submit") {
    if (r.passed) {
      html = `<div class="verdict pass">
          <strong>Quest cleared!</strong> ${r.gained ? `+${r.gained} XP` : "(XP already earned)"}
          ${lesson.next ? `<a class="btn primary" href="/learn/${lesson.course}/${lesson.next}" data-link>Next lesson →</a>`
                        : `<a class="btn primary" href="/" data-link>Back to quests</a>`}
        </div>` + html;
      const before = lastProfile?.level;
      showProfile(r.profile);
      if (r.gained) celebrate(r.gained, before && r.profile.level > before ? r.profile.level : null);
    } else {
      html = `<div class="verdict fail"><strong>Not yet.</strong> <span class="msg">${escapeHtml(r.message || "")}</span>
        ${r.expected ? `<div class="expected"><span>Expected output:</span><pre>${escapeHtml(r.expected)}</pre></div>` : ""}
      </div>` + html;
      if (r.profile) showProfile(r.profile);
    }
  }
  out.innerHTML = html;
  if (r.replay) showReplay(out, r.replay, mode);
}

// Replay: the Godot runner records where every body was while your code ran, drawn here as boxes.
function showReplay(out, replay, mode) {
  const frames = replay.frames, is3d = replay.dim === 3;
  if (!frames?.length || !frames.some((f) => f.some((e) => e[1] !== 1))) return;
  const box = document.createElement("div");
  box.className = "replay";
  box.innerHTML = `<div class="replay-head"><strong>🎬 Replay</strong>
      <span class="muted">${mode === "submit" ? "what happened during the check" : "your node in the test scene"}</span></div>
    <canvas></canvas>
    <div class="replay-controls"><button class="btn small" data-play>⏸ Pause</button>
      <input type="range" min="0" max="${frames.length - 1}" value="0" aria-label="Replay time">
      <span class="muted time">0.0 s</span></div>
    <p class="replay-key muted"><span class="k you"></span>you <span class="k solid"></span>floor and walls <span class="k area"></span>areas <span class="k other"></span>other bodies</p>`;
  const verdict = out.querySelector(".verdict");
  if (verdict) verdict.after(box); else out.prepend(box);
  const canvas = box.querySelector("canvas"), ctx = canvas.getContext("2d");
  const slider = box.querySelector("input"), timeLabel = box.querySelector(".time"), playBtn = box.querySelector("[data-play]");

  // 3D: look from the side (x, y) when things move up and down more than forwards, else from above (x, z).
  const spread = (i) => { const v = frames.flatMap((f) => f.filter((e) => e[1] === 0).map((e) => e[i])); return v.length ? Math.max(...v) - Math.min(...v) : 0; };
  const topDown = is3d && spread(4) > spread(3);
  const view = (e) => is3d
    ? (topDown ? { x: e[2], y: e[4], w: e[5], h: e[7] } : { x: e[2], y: -e[3], w: e[5], h: e[6] })
    : { x: e[2], y: e[3], w: e[4], h: e[5] };

  // Frame the moving things (not the huge floor), with some room around them.
  const moving = frames.flatMap((f) => f.filter((e) => e[1] !== 1).map(view));
  const xs = moving.flatMap((v) => [v.x - v.w / 2, v.x + v.w / 2]), ys = moving.flatMap((v) => [v.y - v.h / 2, v.y + v.h / 2]);
  const minSpan = is3d ? 6 : 160;
  let [x0, x1, y0, y1] = [Math.min(...xs), Math.max(...xs), Math.min(...ys), Math.max(...ys)];
  const padX = Math.max((minSpan - (x1 - x0)) / 2, (x1 - x0) * 0.15), padY = Math.max((minSpan / 2 - (y1 - y0)) / 2, (y1 - y0) * 0.25);
  x0 -= padX; x1 += padX; y0 -= padY; y1 += padY;

  const css = getComputedStyle(document.documentElement);
  const color = (n) => css.getPropertyValue(n).trim();
  const fills = [color("--accent"), color("--muted"), color("--gold"), color("--bad")];
  let at = 0, playing = true, last = 0;

  function draw() {
    const w = canvas.clientWidth, h = canvas.clientHeight, dpr = window.devicePixelRatio || 1;
    if (canvas.width !== Math.round(w * dpr)) { canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr); }
    const scale = Math.min(w / (x1 - x0), h / (y1 - y0));
    const ox = (w - (x1 - x0) * scale) / 2, oy = (h - (y1 - y0) * scale) / 2;
    const sx = (x) => ox + (x - x0) * scale, sy = (y) => oy + (y - y0) * scale;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);
    // the path you took so far
    ctx.strokeStyle = fills[0]; ctx.globalAlpha = 0.35; ctx.lineWidth = 2; ctx.beginPath();
    frames.slice(0, at + 1).forEach((f, i) => { const me = f.find((e) => e[1] === 0); if (me) { const v = view(me); ctx[i ? "lineTo" : "moveTo"](sx(v.x), sy(v.y)); } });
    ctx.stroke(); ctx.globalAlpha = 1;
    for (const e of [...frames[at]].sort((a, b) => (a[1] === 0) - (b[1] === 0))) {
      const v = view(e), px = sx(v.x - v.w / 2), py = sy(v.y - v.h / 2), pw = Math.max(v.w * scale, 3), ph = Math.max(v.h * scale, 3);
      if (e[1] === 2) { ctx.setLineDash([4, 3]); ctx.strokeStyle = fills[2]; ctx.lineWidth = 2; ctx.strokeRect(px, py, pw, ph); ctx.setLineDash([]); }
      else { ctx.fillStyle = fills[e[1]]; ctx.globalAlpha = e[1] === 1 ? 0.5 : 1; ctx.fillRect(px, py, pw, ph); ctx.globalAlpha = 1; }
    }
    slider.value = at;
    timeLabel.textContent = `${(at / 30).toFixed(1)} s`;
  }
  function tick(t) {
    if (!box.isConnected) return;
    if (playing && t - last > 1000 / 30) {
      last = t;
      at = at < frames.length - 1 ? at + 1 : 0;
      draw();
    }
    requestAnimationFrame(tick);
  }
  playBtn.onclick = () => { playing = !playing; playBtn.textContent = playing ? "⏸ Pause" : "▶ Play"; };
  slider.oninput = () => { playing = false; playBtn.textContent = "▶ Play"; at = Number(slider.value); draw(); };
  draw();
  requestAnimationFrame(tick);
}

function celebrate(xp, newLevel) {
  const el = document.createElement("div");
  el.className = "celebrate";
  el.innerHTML = `<div class="burst">+${xp} XP</div>${newLevel ? `<div class="levelup">Level ${newLevel}!</div>` : ""}`;
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 1800);
}

// ------------------------- in-browser runners (Python, Lua, TypeScript) ---

const makeWorkerRunner = (url, name) => ({
  worker: null,
  isReady: false,
  pending: new Map(),
  nextId: 1,
  warmUp() {
    if (this.worker) return;
    this.worker = new Worker(url, { type: "module" });
    this.worker.onmessage = (e) => {
      const msg = e.data;
      if (msg.type === "ready") this.isReady = true;
      if (msg.type === "failed") toast(`${name} couldn't start: ` + msg.error);
      if (msg.type === "result") {
        const p = this.pending.get(msg.id);
        if (p) { clearTimeout(p.timer); this.pending.delete(msg.id); p.resolve(msg.result); }
      }
    };
  },
  run(job) {
    this.warmUp();
    const id = this.nextId++;
    return new Promise((resolve) => {
      // Generous limit on the first run while Python downloads; 10 seconds after that.
      const limit = this.isReady ? 10000 : 60000;
      const timer = setTimeout(() => {
        this.pending.delete(id);
        this.worker.terminate();
        this.worker = null;
        this.isReady = false;
        resolve({ output: "", passed: false, message: "",
          error: "Your program ran too long and was stopped. Is there a loop that never ends?" });
      }, limit);
      this.pending.set(id, { resolve, timer });
      this.worker.postMessage({ id, ...job });
    });
  },
});

const browserRunners = {
  python: makeWorkerRunner("/static/py-worker.js", "Python"),
  lua: makeWorkerRunner("/static/lua-worker.js", "Lua"),
  typescript: makeWorkerRunner("/static/ts-worker.js", "TypeScript"),
};

// ---------------------------------------------------------------- utils ---

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function langName(lang) {
  return { python: "Python", gdscript: "GDScript", lua: "Lua", typescript: "TypeScript", rust: "Rust", nix: "Nix", git: "Git", pyhost: "Python" }[lang] || lang;
}

route().catch((err) => {
  app.innerHTML = `<p class="stderr">Couldn't load CodeQuest: ${escapeHtml(err.message)}</p>`;
});

// ------------------------------------------------------- reading helpers ---

// Focus mode: show a long lesson one "## part" at a time, so there's always one small next step.
function setUpParts(body, lesson) {
  const startBtn = body.querySelector(".to-code");
  const parts = [[]];
  for (const node of [...body.childNodes].filter((n) => n !== startBtn)) {
    if (node.nodeName === "H2" && parts.at(-1).some((n) => n.nodeType === 1)) parts.push([]);
    parts.at(-1).push(node);
  }
  if (parts.length < 3) return;
  const sections = parts.map((nodes) => {
    const sec = document.createElement("section");
    sec.className = "part";
    sec.append(...nodes);
    return sec;
  });
  body.prepend(...sections);
  const nav = document.createElement("div");
  nav.className = "part-nav";
  body.insertBefore(nav, startBtn);
  let focus = true, at = 0;
  try { focus = localStorage.getItem("codequest-focus") !== "off"; } catch {}
  const show = () => {
    sections.forEach((sec, i) => (sec.hidden = focus && i !== at));
    nav.innerHTML = focus
      ? `<button class="btn ghost" data-go="-1" ${at ? "" : "disabled"}>← Back</button>
         <span class="dots">${sections.map((_, i) => `<span class="${i <= at ? "on" : ""}"></span>`).join("")}</span>
         ${at < sections.length - 1 ? `<button class="btn primary" data-go="1">Next part (${at + 2} of ${sections.length}) →</button>` : ""}
         <button class="btn ghost small" data-mode="off">Show all</button>`
      : `<button class="btn ghost small" data-mode="on">One part at a time</button>`;
    if (startBtn) startBtn.hidden = focus && at < sections.length - 1;
  };
  nav.onclick = (e) => {
    const b = e.target.closest("button");
    if (!b) return;
    if (b.dataset.go) { at += Number(b.dataset.go); body.scrollIntoView({ block: "start" }); }
    if (b.dataset.mode) {
      focus = b.dataset.mode === "on";
      try { localStorage.setItem("codequest-focus", focus ? "on" : "off"); } catch {}
    }
    show();
  };
  show();
}

// "- [ ]" task lists (like a capstone's "on your machine" steps) can be ticked; saved on this device.
function setUpChecklists(body, lesson) {
  const key = `codequest-tasks-${lesson.course}-${lesson.slug}`;
  let ticked = [];
  try { ticked = JSON.parse(localStorage.getItem(key) || "[]"); } catch {}
  body.querySelectorAll('input[type="checkbox"]').forEach((box, i) => {
    box.disabled = false;
    box.checked = ticked.includes(i);
    box.onchange = () => {
      ticked = box.checked ? [...ticked, i] : ticked.filter((t) => t !== i);
      try { localStorage.setItem(key, JSON.stringify(ticked)); } catch {}
    };
  });
}

// "## Review" questions: after opening one, say whether you knew it; it comes back later (spaced repetition).
function setUpReview(body, lesson) {
  const head = [...body.querySelectorAll("h2")].find((h) => h.textContent.trim() === "Review");
  if (!head) return;
  for (const d of body.querySelectorAll("details")) {
    if (!(head.compareDocumentPosition(d) & Node.DOCUMENT_POSITION_FOLLOWING)) continue;
    const question = d.querySelector("summary")?.textContent.trim();
    if (!question) continue;
    const answer = d.textContent.slice(d.querySelector("summary").textContent.length).trim();
    d.insertAdjacentHTML("beforeend", `<div class="grade">Did you know it?
      <button class="btn small" data-knew="1">✓ Yes</button><button class="btn small" data-knew="0">Not yet</button></div>`);
    const grade = d.querySelector(".grade");
    grade.onclick = async (e) => {
      const b = e.target.closest("button");
      if (!b) return;
      const r = await api("/api/review", { course: lesson.course, slug: lesson.slug, question, answer, knew: b.dataset.knew === "1" });
      grade.innerHTML = `<span class="muted">Saved. It comes back on ${r.due}.</span>`;
    };
  }
}

async function showReviews() {
  document.title = "Review · CodeQuest";
  const { reviews_due: due, profile } = await api("/api/courses");
  showProfile(profile);
  app.innerHTML = `
    <div class="lesson-head"><a href="/" data-link class="back">← Quests</a><span class="muted">${due.length} due</span></div>
    <article class="lesson-body review-list">
      <h1>Review</h1>
      <p class="muted">Think of the answer first, then open it. Say honestly if you knew it: what you knew comes back later, what you didn't comes back tomorrow.</p>
      ${due.length ? due.map((q, i) => `
        <details data-i="${i}"><summary>${escapeHtml(q.question)}</summary><p>${escapeHtml(q.answer)}</p>
          <div class="grade"><button class="btn small" data-knew="1">✓ I knew it</button><button class="btn small" data-knew="0">Not yet</button>
          <a class="muted" href="/learn/${q.course}/${q.slug}" data-link>Open lesson</a></div></details>`).join("")
        : `<p>Nothing due. Nice work!</p>`}
    </article>`;
  app.querySelectorAll(".review-list details").forEach((d) => {
    d.querySelector(".grade").onclick = async (e) => {
      const b = e.target.closest("button");
      if (!b) return;
      const q = due[d.dataset.i];
      await api("/api/review", { course: q.course, slug: q.slug, question: q.question, answer: q.answer, knew: b.dataset.knew === "1" });
      d.remove();
      if (!app.querySelector(".review-list details")) app.querySelector(".review-list").insertAdjacentHTML("beforeend", "<p>All done for today! 🎉</p>");
    };
  });
}
