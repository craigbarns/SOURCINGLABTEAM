#!/usr/bin/env python3
"""
send_emails.py — Envoi des 10 emails de prospection Sourcing Lab USA via IONOS SMTP.

Usage:
  DRY-RUN (par défaut) : génère des fichiers .eml dans deliverables/outbox/ pour relecture
      /tmp/agent-env/bin/python deliverables/send_emails.py
  ENVOI RÉEL :
      /tmp/agent-env/bin/python deliverables/send_emails.py --send
  Limité aux 3 premiers, 120s entre chaque :
      /tmp/agent-env/bin/python deliverables/send_emails.py --send --limit 3 --delay 120

Configuration : copier .email_config.example.json vers .email_config.json et remplir.
"""
import argparse
import json
import re
import smtplib
import ssl
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
from pathlib import Path

BASE = Path(__file__).resolve().parent
CONFIG = BASE / ".email_config.json"
MISSION_EMAILS_MD = BASE.parent / "missions" / "2026-10-25-prospection-generale" / "deliverables" / "emails-prospection-2026-10-25.md"
FALLBACK_EMAILS_MD = BASE / "emails-prospection-2026-10-25.md"
EMAILS_MD = MISSION_EMAILS_MD if MISSION_EMAILS_MD.exists() else FALLBACK_EMAILS_MD
OUTBOX = BASE / "outbox"

HDR_RE = re.compile(
    r"^##\s*\d+\.\s*(?P<company>.+?)\s+—\s+(?P<contact>.+?)\s+—\s+"
    r"(?P<to>[\w.\-+]+@[\w.\-]+)\s+—\s+Score\s+(?P<score>\d+)",
    re.M,
)
SUBJ_RE = re.compile(r"\*\*Subject:\s*(?P<subject>.+?)\*\*")


def load_config() -> dict:
    if not CONFIG.exists():
        sys.exit(
            f"❌ Config introuvable : {CONFIG}\n"
            f"   → cp {BASE / '.email_config.example.json'} {CONFIG} puis remplissez les valeurs."
        )
    cfg = json.loads(CONFIG.read_text())
    for key in ("smtp_host", "smtp_port", "sender_email", "sender_name"):
        if not cfg.get(key):
            sys.exit(f"❌ Champ manquant dans la config : '{key}'")
    if not cfg.get("sender_password"):
        sys.exit("❌ 'sender_password' vide dans la config.")
    return cfg


def parse_emails(md_text: str, signature: str, footer: str) -> list[dict]:
    emails = []
    for block in re.split(r"\n---\n", md_text):
        h = HDR_RE.search(block)
        s = SUBJ_RE.search(block)
        if not h or not s:
            continue
        body = block[s.end():].strip()
        body = body.replace("[SIGNATURE]", signature).strip()
        if footer:
            body += "\n\n" + footer
        emails.append(
            {
                "company": h.group("company"),
                "contact": h.group("contact"),
                "to": h.group("to"),
                "score": int(h.group("score")),
                "subject": s.group("subject").strip(),
                "body": body,
            }
        )
    return emails


def build_message(cfg: dict, e: dict) -> MIMEMultipart:
    msg = MIMEMultipart("alternative")
    msg["From"] = f"{cfg['sender_name']} <{cfg['sender_email']}>"
    msg["To"] = e["to"]
    msg["Subject"] = e["subject"]
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain=cfg["sender_email"].split("@")[1])
    msg.attach(MIMEText(e["body"], "plain", "utf-8"))
    return msg


def main() -> None:
    ap = argparse.ArgumentParser(description="Envoi emails prospection via IONOS SMTP")
    ap.add_argument("--send", action="store_true", help="Envoi réel (défaut : dry-run .eml)")
    ap.add_argument("--limit", type=int, default=0, help="Envoyer seulement les N premiers")
    ap.add_argument("--delay", type=int, default=90, help="Secondes entre chaque envoi")
    ap.add_argument("--emails", type=str, default=None,
                    help="Chemin du fichier markdown des emails (défaut : détection auto)")
    args = ap.parse_args()

    cfg = load_config()
    emails_md = Path(args.emails) if args.emails else EMAILS_MD
    if not emails_md.exists():
        sys.exit(f"❌ Fichier emails introuvable : {emails_md}\n"
                 f"   → utilisez --emails /chemin/vers/emails-prospection.md")
    footer = (cfg.get("can_spam_footer") or "").format(**cfg)
    emails = parse_emails(emails_md.read_text(), cfg.get("signature", ""), footer)
    if not emails:
        sys.exit("❌ Aucun email détecté dans le markdown — vérifiez le format.")
    if args.limit:
        emails = emails[: args.limit]

    print(f"📋 {len(emails)} emails détectés. Mode : {'ENVOI RÉEL' if args.send else 'DRY-RUN (.eml)'}\n")

    if not args.send:
        OUTBOX.mkdir(exist_ok=True)
        for i, e in enumerate(emails, 1):
            msg = build_message(cfg, e)
            path = OUTBOX / f"{i:02d}_{e['company'].replace(' ', '_').lower()}.eml"
            path.write_bytes(msg.as_bytes())
            print(f"  ✉️  {i:02d}. {e['company']} → {e['to']} | {e['subject']}")
            print(f"       📄 {path}")
        print(f"\n✅ {len(emails)} brouillons .eml générés dans {OUTBOX} — relisez-les avant --send.")
        return

    # Envoi réel
    use_ssl = int(cfg["smtp_port"]) == 465
    print(f"🔌 Connexion SMTP {cfg['smtp_host']}:{cfg['smtp_port']} "
          f"({'SSL' if use_ssl else 'STARTTLS'})…")
    if use_ssl:
        server = smtplib.SMTP_SSL(cfg["smtp_host"], int(cfg["smtp_port"]),
                                  context=ssl.create_default_context(), timeout=30)
    else:
        server = smtplib.SMTP(cfg["smtp_host"], int(cfg["smtp_port"]), timeout=30)
        server.ehlo()
        server.starttls(context=ssl.create_default_context())
        server.ehlo()
    server.login(cfg["sender_email"], cfg["sender_password"])
    print(f"✅ Authentifié : {cfg['sender_email']}\n")

    sent, failed = 0, 0
    for i, e in enumerate(emails, 1):
        try:
            msg = build_message(cfg, e)
            server.sendmail(cfg["sender_email"], [e["to"]], msg.as_string())
            sent += 1
            print(f"  📤 {i:02d}/{len(emails)} envoyé → {e['company']} ({e['to']})")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"  ❌ {i:02d}/{len(emails)} ÉCHEC {e['company']} ({e['to']}) : {exc}")
        if i < len(emails):
            print(f"       ⏳ pause {args.delay}s…")
            time.sleep(args.delay)
    server.quit()
    print(f"\n🏁 Terminé : {sent} envoyés, {failed} échecs.")


if __name__ == "__main__":
    main()
