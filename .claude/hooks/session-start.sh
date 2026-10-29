#!/bin/bash
# Ders Kutusu — Claude Code bulut oturumu başlangıç kancası (.claude/settings.json → SessionStart).
# Sekiz Kapı denetiminin (araclar/sekiz_kapi.py) ve tarayıcı testlerinin (tests/*.cjs) gerek duyduğu araçları
# her oturumda kendiliğinden hazırlar; kurulu olanı yeniden kurmaz. Yerel bilgisayarda hiçbir şey yapmaz.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi
cd "${CLAUDE_PROJECT_DIR:-.}"

# 1. poppler-utils (pdfinfo, pdftotext): 5. kapının PDF sayfa sayısı ve üst üste binme taraması. Sistem geneli; yoksa kurulur.
if ! command -v pdftotext >/dev/null 2>&1; then
  if command -v apt-get >/dev/null 2>&1; then
    (apt-get update -qq && apt-get install -y -qq poppler-utils) >/dev/null 2>&1 || echo "[sekiz-kapi] poppler-utils kurulamadı; PDF binme taraması atlanır"
  fi
fi

# 2. pypdf: pdfinfo yoksa PDF sayfa sayısı için yedek.
if ! python3 -c "import pypdf" >/dev/null 2>&1; then
  pip install --quiet pypdf >/dev/null 2>&1 || pip install --quiet --break-system-packages pypdf >/dev/null 2>&1 || true
fi

# 3. @playwright/test: 6. kapı (tests/sekiz-kapi-yerlesim.cjs) ve tests/*.cjs. Depo dışına, bulut imajındaki playwright ile
#    aynı sürüm kurulur (tarayıcılar /opt/pw-browsers altında hazırdır); yalnız bu betik değişince yeniden kurulur.
QA="$HOME/.derskutusu-qa"
hashes="$QA/node_modules/.session-start.sha256"
if ! sha256sum --check --status "$hashes" 2>/dev/null; then
  rm -f "$hashes"
  SURUM="$(node -p "require('playwright/package.json').version" 2>/dev/null || true)"
  if [ -n "$SURUM" ]; then
    npm install --prefix "$QA" --no-save --package-lock=false --ignore-scripts --no-audit --no-fund --loglevel=error "@playwright/test@$SURUM"
  else
    npm install --prefix "$QA" --no-save --package-lock=false --ignore-scripts --no-audit --no-fund --loglevel=error "@playwright/test@1.56.1"
    "$QA/node_modules/.bin/playwright" install chromium
  fi
  mkdir -p "$QA/node_modules"
  sha256sum .claude/hooks/session-start.sh > "$hashes"
fi

# 4. Oturum ortam değişkenleri: tests/*.cjs ve 6. kapı Playwright'ı bu yoldan bulur; tarayıcılar imajdaki klasörden gelir.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export NODE_PATH=\"$QA/node_modules${NODE_PATH:+:$NODE_PATH}\"" >> "$CLAUDE_ENV_FILE"
  if [ -d /opt/pw-browsers ] && [ -z "${PLAYWRIGHT_BROWSERS_PATH:-}" ]; then
    echo 'export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers' >> "$CLAUDE_ENV_FILE"
  fi
fi

echo "[sekiz-kapi] Denetim araçları hazır: python3 araclar/sekiz_kapi.py --hizli  (tam: python3 araclar/sekiz_kapi.py)"
