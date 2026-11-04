// Small "play with it" drawings for lessons. In lesson.md write <div class="explore" data-widget="NAME"></div>.
// Each widget gets its element, adds sliders and an SVG, and redraws on every change.

const ACCENT = "#6c4cf5", RED = "#e5484d", GREEN = "#30a46c", ORANGE = "#d97706";
const fmt = (x, d = 2) => (Math.abs(x) >= 1000 ? x.toFixed(0) : x.toFixed(d));

function frame(el, controls, caption) {
  el.innerHTML = `<div class="explore-title">🎛️ Try it: move the slider</div>
    <svg viewBox="0 0 420 240" width="100%" role="img" aria-label="${caption}"></svg>
    <div class="explore-controls">${controls}</div><p class="explore-readout" aria-live="polite"></p>`;
  return { svg: el.querySelector("svg"), readout: el.querySelector(".explore-readout") };
}

// Map math coordinates to the 420 × 240 picture.
function scale([x0, x1], [y0, y1]) {
  const sx = (x) => 36 + ((x - x0) / (x1 - x0)) * 370, sy = (y) => 210 - ((y - y0) / (y1 - y0)) * 190;
  const axes = `<line x1="30" y1="${sy(Math.max(y0, 0))}" x2="410" y2="${sy(Math.max(y0, 0))}" stroke="currentColor" opacity=".4"/>
    <line x1="${sx(Math.max(x0, 0))}" y1="15" x2="${sx(Math.max(x0, 0))}" y2="215" stroke="currentColor" opacity=".4"/>`;
  const curve = (f, color = ACCENT, w = 2.5) => {
    let d = "";
    for (let i = 0; i <= 120; i++) {
      const x = x0 + ((x1 - x0) * i) / 120, y = f(x);
      if (y >= y0 - 1 && y <= y1 + 1) d += `${d ? "L" : "M"}${sx(x).toFixed(1)},${sy(y).toFixed(1)}`;
    }
    return `<path d="${d}" fill="none" stroke="${color}" stroke-width="${w}"/>`;
  };
  return { sx, sy, axes, curve };
}

function slider(id, label, min, max, step, value) {
  return `<label>${label} <input type="range" id="${id}" min="${min}" max="${max}" step="${step}" value="${value}"> <output for="${id}"></output></label>`;
}

function wire(el, draw) {
  el.querySelectorAll("input").forEach((i) => (i.oninput = draw));
  draw();
}

const WIDGETS = {
  // Math 3: the slope between x = 3 and x = 3 + h heads to 6 as h shrinks.
  derivative(el) {
    const { svg, readout } = frame(el, slider("h", "step h", -3, 0.3, 0.01, 0), "Secant line on y = x squared");
    const s = scale([0, 5], [0, 25]), f = (x) => x * x;
    wire(el, () => {
      const h = 10 ** Number(el.querySelector("#h").value), m = (f(3 + h) - 9) / h;
      el.querySelector("output").textContent = fmt(h, 3);
      svg.innerHTML = s.axes + s.curve(f) + s.curve((x) => 9 + m * (x - 3), RED, 2) +
        `<circle cx="${s.sx(3)}" cy="${s.sy(9)}" r="5" fill="${RED}"/><circle cx="${s.sx(3 + h)}" cy="${s.sy(f(3 + h))}" r="5" fill="${ORANGE}"/>`;
      readout.innerHTML = `slope = (f(3 + h) − f(3)) ÷ h = (${fmt(f(3 + h), 4)} − 9) ÷ ${fmt(h, 3)} = <b>${fmt(m, 4)}</b>. Make h tiny: it heads to 6.`;
    });
  },

  // Math 5 / crash course: gradient descent on (x − 2)² + 1, where the learning rate decides everything.
  "gradient-descent"(el) {
    const { svg, readout } = frame(el, slider("lr", "learning rate", 0.05, 1.1, 0.05, 0.3) +
      ` <button type="button" class="btn small" data-step>Take a step</button> <button type="button" class="btn small ghost" data-reset>Start again</button>`,
      "Gradient descent steps on a curve");
    const s = scale([-2, 6], [0, 18]), f = (x) => (x - 2) ** 2 + 1;
    let path = [-1.5];
    const draw = () => {
      const lr = Number(el.querySelector("#lr").value), x = path.at(-1);
      el.querySelector("output").textContent = fmt(lr);
      svg.innerHTML = s.axes + s.curve(f) + path.map((p, i) => `<circle cx="${s.sx(p)}" cy="${s.sy(Math.min(f(p), 18))}" r="${i === path.length - 1 ? 6 : 3.5}" fill="${i === path.length - 1 ? RED : ORANGE}"/>`).join("");
      const note = Math.abs(x - 2) < 0.01 ? "You reached the bottom!" : lr > 1 ? "Too big: each step jumps past the bottom and lands higher." : lr >= 0.9 ? "Big steps: it zig-zags across the valley." : lr < 0.15 ? "Small steps: safe but slow." : "";
      readout.innerHTML = `step ${path.length - 1}: x = ${fmt(x)}, loss = ${fmt(f(x))}, slope = 2·(x − 2) = ${fmt(2 * (x - 2))}. ${note}`;
    };
    el.querySelector("[data-step]").onclick = () => {
      const lr = Number(el.querySelector("#lr").value), x = path.at(-1);
      if (Math.abs(x) < 1e6) path.push(x - lr * 2 * (x - 2));
      draw();
    };
    el.querySelector("[data-reset]").onclick = () => { path = [-1.5]; draw(); };
    wire(el, () => { path = [-1.5]; draw(); });
  },

  // LLMs 1 / crash course: temperature divides the scores before softmax.
  temperature(el) {
    const { svg, readout } = frame(el, slider("t", "temperature T", 0.1, 3, 0.1, 1), "Next-token probabilities at a temperature");
    const words = ["time", "day", "hill", "zebra"], scores = [2.0, 1.0, 0.5, -1.0];
    wire(el, () => {
      const t = Number(el.querySelector("#t").value), e = scores.map((x) => Math.exp((x - 2) / t)), sum = e.reduce((a, b) => a + b);
      const p = e.map((x) => x / sum);
      el.querySelector("output").textContent = fmt(t, 1);
      svg.innerHTML = p.map((v, i) => `<text x="20" y="${45 + i * 50}" font-size="14" fill="currentColor">${words[i]}</text>
        <rect x="80" y="${28 + i * 50}" width="${(v * 300).toFixed(1)}" height="24" rx="4" fill="${i ? ACCENT : RED}"/>
        <text x="${88 + v * 300}" y="${45 + i * 50}" font-size="13" fill="currentColor">${(v * 100).toFixed(1)}%</text>`).join("");
      readout.innerHTML = `Scores 2.0, 1.0, 0.5, −1.0 are divided by T = ${fmt(t, 1)}, then softmax. ${t < 0.5 ? "Low T: the top word almost always wins." : t > 1.5 ? "High T: even “zebra” gets picked sometimes." : ""}`;
    });
  },

  // Math 2: dot product and angle between two arrows.
  vectors(el) {
    const { svg, readout } = frame(el, slider("aa", "angle of a", 0, 360, 5, 20) + slider("ab", "angle of b", 0, 360, 5, 70) + slider("lb", "length of b", 0.5, 2, 0.25, 1),
      "Two vectors and the angle between them");
    const s = scale([-3.5, 3.5], [-2, 2]);
    const arrow = (x, y, color, name) => `<line x1="${s.sx(0)}" y1="${s.sy(0)}" x2="${s.sx(x)}" y2="${s.sy(y)}" stroke="${color}" stroke-width="3"/>
      <circle cx="${s.sx(x)}" cy="${s.sy(y)}" r="4" fill="${color}"/><text x="${s.sx(x) + 6}" y="${s.sy(y) - 6}" font-size="14" fill="${color}">${name}</text>`;
    wire(el, () => {
      const [aa, ab, lb] = ["#aa", "#ab", "#lb"].map((q) => Number(el.querySelector(q).value)), rad = Math.PI / 180;
      el.querySelectorAll("output").forEach((o, i) => (o.textContent = [aa + "°", ab + "°", lb][i]));
      const a = [1.5 * Math.cos(aa * rad), 1.5 * Math.sin(aa * rad)], b = [lb * Math.cos(ab * rad), lb * Math.sin(ab * rad)];
      const dot = a[0] * b[0] + a[1] * b[1], la = Math.hypot(...a), lbn = Math.hypot(...b), cos = dot / (la * lbn);
      svg.innerHTML = s.axes + arrow(...a, ACCENT, "a") + arrow(...b, GREEN, "b");
      readout.innerHTML = `a · b = ${fmt(a[0])}·${fmt(b[0])} + ${fmt(a[1])}·${fmt(b[1])} = <b>${fmt(dot)}</b>, ‖a‖ = ${fmt(la)}, ‖b‖ = ${fmt(lbn)}, cos θ = <b>${fmt(cos)}</b>, θ = ${fmt(Math.acos(Math.max(-1, Math.min(1, cos))) / rad, 0)}°. ${Math.abs(cos) < 0.02 ? "Perpendicular: the dot product is 0." : cos < 0 ? "Pointing apart: negative." : ""}`;
    });
  },

  // Math 6: PCA finds the direction that keeps the most spread.
  pca(el) {
    const { svg, readout } = frame(el, slider("ang", "line angle", 0, 180, 1, 90), "Projecting points onto a line");
    const s = scale([-4, 4], [-2.3, 2.3]);
    const pts = Array.from({ length: 24 }, (_, i) => { const t = (i * 7.3) % 6 - 3, n = Math.sin(i * 12.9898) * 0.6; return [t, 0.5 * t + n]; });
    const m = [0, 1].map((k) => pts.reduce((a, p) => a + p[k], 0) / pts.length), c = pts.map((p) => [p[0] - m[0], p[1] - m[1]]);
    const spread = (u) => c.reduce((a, p) => a + (p[0] * u[0] + p[1] * u[1]) ** 2, 0) / c.length;
    const total = c.reduce((a, p) => a + p[0] ** 2 + p[1] ** 2, 0) / c.length;
    let best = 0, bestA = 0;
    for (let d = 0; d < 180; d++) { const v = spread([Math.cos(d * Math.PI / 180), Math.sin(d * Math.PI / 180)]); if (v > best) { best = v; bestA = d; } }
    wire(el, () => {
      const ang = Number(el.querySelector("#ang").value), u = [Math.cos(ang * Math.PI / 180), Math.sin(ang * Math.PI / 180)], v = spread(u);
      el.querySelector("output").textContent = ang + "°";
      svg.innerHTML = s.axes + `<line x1="${s.sx(-4 * u[0])}" y1="${s.sy(-4 * u[1])}" x2="${s.sx(4 * u[0])}" y2="${s.sy(4 * u[1])}" stroke="${RED}" stroke-width="2"/>` +
        c.map((p) => { const k = p[0] * u[0] + p[1] * u[1];
          return `<line x1="${s.sx(p[0])}" y1="${s.sy(p[1])}" x2="${s.sx(k * u[0])}" y2="${s.sy(k * u[1])}" stroke="currentColor" opacity=".3"/>
            <circle cx="${s.sx(p[0])}" cy="${s.sy(p[1])}" r="4" fill="${ACCENT}"/><circle cx="${s.sx(k * u[0])}" cy="${s.sy(k * u[1])}" r="3" fill="${RED}"/>`; }).join("");
      readout.innerHTML = `Spread (variance) along the line: <b>${fmt(v)}</b> of ${fmt(total)} total = <b>${fmt((100 * v) / total, 0)}%</b> kept. ${Math.abs(ang - bestA) <= 2 ? "That's the first principal component: no angle keeps more." : "Turn the line to keep more spread."}`;
    });
  },
};

// "Predict first" questions: <div class="quiz" data-answer="1" data-why="..."><p>question</p><button>A</button>...</div>
function setUpQuiz(q) {
  const buttons = [...q.querySelectorAll("button")], right = Number(q.dataset.answer);
  buttons.forEach((b, i) => {
    b.type = "button";
    b.classList.add("btn");
    b.onclick = () => {
      b.classList.add(i === right ? "right" : "wrong");
      if (i !== right) return; // wrong guesses stay clickable, so you can try again
      buttons.forEach((x) => (x.disabled = true));
      q.insertAdjacentHTML("beforeend", `<p class="why">✓ ${q.dataset.why || "Right!"}</p>`);
    };
  });
}

export function setUpInteractive(body) {
  body.querySelectorAll(".explore[data-widget]").forEach((el) => WIDGETS[el.dataset.widget]?.(el));
  body.querySelectorAll(".quiz[data-answer]").forEach(setUpQuiz);
}
