import {
  EditorView, basicSetup, EditorState, keymap, indentWithTab, indentUnit, python, rust, oneDark,
  StreamLanguage, lua,
} from "/vendor/codemirror.js";
import { marked } from "/vendor/marked.js";

const app = document.getElementById("app");
const LANG_INFO = {
  python: { icon: "🐍", blurb: "Runs right in your browser.", unit: "    " },
  gdscript: { icon: "🎮", blurb: "The language of the Godot game engine.", unit: "\t" },
  lua: { icon: "🌙", blurb: "Small scripting language used in Roblox, LÖVE and Defold. Runs in your browser.", unit: "    " },
  rust: { icon: "🦀", blurb: "Fast, safe systems programming.", unit: "    " },
  nix: { icon: "❄️", blurb: "The language NixOS, nixpkgs and flakes are written in.", unit: "  " },
  git: { icon: "🌿", blurb: "Track changes, branch, merge and share your code.", unit: "  " },
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
  return showHome();
}

// ------------------------------------------------------------------ home ---

async function showHome() {
  document.title = "CodeQuest";
  const { courses, profile } = await api("/api/courses");
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
    <section class="courses">
      ${courses.map(courseCard).join("")}
    </section>`;
  if (onLan) document.getElementById("phone-btn").onclick = () => showPhoneDialog(info.urls);
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
      <span class="muted">${escapeHtml(lesson.course_name)} · Lesson ${lesson.index} of ${lesson.total}</span>
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
          ${lesson.solution ? `<button class="btn ghost" id="solution">Solution</button>` : ""}
          <button class="btn ghost" id="reset">Reset</button>
        </div>
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
  if (solBtn) solBtn.onclick = () => {
    if (confirm("Replace your code with the official solution?")) setCode(lesson.solution);
  };

  browserRunners[lang]?.warmUp();
}

function createEditor(doc, lang, onChange) {
  // GDScript reads well with Python highlighting.
  const language = lang === "rust" ? rust() : lang === "lua" ? StreamLanguage.define(lua)
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
  }
  renderResult(out, result, mode, lesson);
}

function renderResult(out, r, mode, lesson) {
  let html = "";
  if (r.output) html += `<pre class="stdout">${escapeHtml(r.output)}</pre>`;
  else if (!r.error) html += `<p class="muted">(no output)</p>`;
  if (r.error) html += `<pre class="stderr">${escapeHtml(r.error)}</pre>`;
  if (r.warnings && !r.error) html += `<details><summary>Warnings</summary><pre class="warn-text">${escapeHtml(r.warnings)}</pre></details>`;

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
}

function celebrate(xp, newLevel) {
  const el = document.createElement("div");
  el.className = "celebrate";
  el.innerHTML = `<div class="burst">+${xp} XP</div>${newLevel ? `<div class="levelup">Level ${newLevel}!</div>` : ""}`;
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 1800);
}

// ------------------------------------- in-browser runners (Python, Lua) ---

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
};

// ---------------------------------------------------------------- utils ---

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function langName(lang) {
  return { python: "Python", gdscript: "GDScript", lua: "Lua", rust: "Rust", nix: "Nix", git: "Git" }[lang] || lang;
}

route().catch((err) => {
  app.innerHTML = `<p class="stderr">Couldn't load CodeQuest: ${escapeHtml(err.message)}</p>`;
});
