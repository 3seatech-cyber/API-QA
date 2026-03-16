const apiInput = document.getElementById('apiBase');
const output = document.getElementById('output');
const saveBtn = document.getElementById('saveApi');
const swaggerBtn = document.getElementById('swaggerBtn');
const testButtons = document.querySelectorAll('.test-btn');

const KEY = 'roboapi_lab_api_base';
const defaultBase = localStorage.getItem(KEY) || 'http://127.0.0.1:8000';
apiInput.value = defaultBase;

function normalizeBase(url) {
  return url.replace(/\/$/, '');
}

function setBase() {
  const base = normalizeBase(apiInput.value.trim());
  localStorage.setItem(KEY, base);
  output.textContent = `URL guardada: ${base}`;
}

async function runGet(endpoint) {
  const base = normalizeBase(apiInput.value.trim());
  const url = `${base}${endpoint}`;
  output.textContent = `Consultando ${url} ...`;
  try {
    const res = await fetch(url, { headers: { 'Accept': 'application/json' } });
    const text = await res.text();
    let formatted = text;
    try { formatted = JSON.stringify(JSON.parse(text), null, 2); } catch {}
    output.textContent = `HTTP ${res.status}\n\n${formatted}`;
  } catch (err) {
    output.textContent = `No fue posible conectar con ${url}.\n\nVerifica despliegue, CORS y la URL configurada.\n\nDetalle: ${err.message}`;
  }
}

saveBtn.addEventListener('click', setBase);
swaggerBtn.addEventListener('click', () => {
  const base = normalizeBase(apiInput.value.trim());
  window.open(`${base}/docs`, '_blank', 'noopener');
});

testButtons.forEach(btn => {
  btn.addEventListener('click', () => runGet(btn.dataset.endpoint));
});
