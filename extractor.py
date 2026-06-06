import re
import json

def extract_legal_description(text: str):
    text = text.upper()

    data = {
        "lot": None,
        "block": None,
        "section": None,
        "subdivision": None,
        "county": None,
        "unit": None,
        "raw": text.strip()
    }

    # LOT
    lot_match = re.search(r"LOT\s+(\d+)", text)
    if lot_match:
        data["lot"] = lot_match.group(1)

    # BLOCK
    block_match = re.search(r"BLOCK\s+(\d+)", text)
    if block_match:
        data["block"] = block_match.group(1)

    # SECTION
    sec_match = re.search(r"(SEC|SECTION)\s+(\d+)", text)
    if sec_match:
        data["section"] = sec_match.group(2)

    # UNIT / PHASE
    unit_match = re.search(r"(UNIT|PHASE)\s+(\d+)", text)
    if unit_match:
        data["unit"] = unit_match.group(2)

    # SUBDIVISION (simple heuristic)
    subdiv_match = re.search(r"(?<=,)\s*([A-Z\s]+?)\s*(SEC|SECTION|BLOCK|LOT)", text)
    if subdiv_match:
        data["subdivision"] = subdiv_match.group(1).strip()

    # COUNTY
    if "FORT BEND" in text or "FBCAD" in text:
        data["county"] = "Fort Bend"

    return data


if __name__ == "__main__":
    sample = input("Paste legal description:\n")
    result = extract_legal_description(sample)
    print("\nExtracted JSON:\n")
    print(json.dumps(result, indent=4))
