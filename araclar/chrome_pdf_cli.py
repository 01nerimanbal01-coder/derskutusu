"""Başsız Chrome belge işini, tamamlanmış çıktı ve sınırlı kapanış süresiyle çalıştırır."""
import html
import json
import re
import subprocess
import time


def dom_tamam(path, marker):
    if not path.exists():
        return False
    text = path.read_text(encoding='utf-8')
    match = re.search(r'<pre id="' + re.escape(marker) + r'">(\[.*?\])</pre>', text, re.S)
    if not text.rstrip().endswith('</html>') or not match:
        return False
    try:
        return isinstance(json.loads(html.unescape(match.group(1))), list)
    except (ValueError, TypeError):
        return False


def calistir(command, stdout_path, stderr_path, ready, timeout=180):
    """Çıktı hazır olduktan sonra kendi CLI sürecine normal sonlanma fırsatı verir.

    Hazır ölçütü çağıran tarafından verilir: tamamı yazılmış DOM/JSON veya
    EOF işaretli, açılabilen yeni PDF. Başarısız/eksik çıktı yayıma ilerlemez.
    """
    start = time.monotonic()
    ready_since = None
    with stdout_path.open('w', encoding='utf-8') as out, stderr_path.open('w', encoding='utf-8') as err:
        proc = subprocess.Popen(command, stdout=out, stderr=err)
        try:
            while True:
                code = proc.poll()
                complete = ready()
                if code is not None:
                    if code != 0:
                        raise subprocess.CalledProcessError(code, command)
                    if not complete:
                        raise RuntimeError('Chrome kapandı ancak belge çıktısı tamamlanmadı: ' + str(stdout_path))
                    return
                if complete:
                    ready_since = ready_since or time.monotonic()
                    if time.monotonic() - ready_since >= 5:
                        # Yalnız bu çağrının oluşturduğu, çıktısını tamamlamış CLI süreci.
                        proc.terminate()
                        proc.wait(timeout=15)
                        if not ready():
                            raise RuntimeError('Chrome kapanışından sonra çıktı doğrulanamadı.')
                        print('Chrome belge çıktısı tamam; CLI kapanışı tamamlandı.', flush=True)
                        return
                else:
                    ready_since = None
                if time.monotonic() - start >= timeout:
                    raise subprocess.TimeoutExpired(command, timeout)
                time.sleep(0.25)
        finally:
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait()
