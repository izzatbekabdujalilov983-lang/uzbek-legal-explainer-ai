import json
from pathlib import Path

def create_video_manifest(topic: str, statute_ref: str, scenes: list[dict]) -> dict:
    """
    Generates a structured JSON manifest for automated legal explainer videos
    combining Uzbek TTS narration and slide timings.
    """
    manifest = {
        "project": "Uzbek Legal Explainer AI",
        "topic": topic,
        "legal_basis": statute_ref,
        "language": "uz-UZ",
        "voice_engine": "neural-tts",
        "scenes": scenes,
    }
    return manifest

if __name__ == "__main__":
    sample_scenes = [
        {"scene_id": 1, "duration_sec": 15, "visual": "office_dispute_2d", "text": "Xodim ishdan ketish uchun ariza yozdi."},
        {"scene_id": 2, "duration_sec": 20, "visual": "labor_code_160", "text": "Mehnat kodeksi 160-moddasiga ko‘ra 14 kun oldin ogohlantirish yetarli."},
        {"scene_id": 3, "duration_sec": 15, "visual": "calendar_15_day", "text": "15-kuni xodim to‘liq hisob-kitob bilan ishni to‘xtatishga haqli."}
    ]
    result = create_video_manifest(
        topic="Mehnat shartnomasini bekor qilish",
        statute_ref="O‘zR Mehnat kodeksi, 160-modda",
        scenes=sample_scenes
    
    )
    Path("manifest.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Video manifest successfully generated.")
