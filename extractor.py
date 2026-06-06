import re
import json

def extract_legal_description(text: str):
    text = text.upper()

    data = {
        "subdivision": None,
        "section": None,
        "block": None,
        "lot": None,
        "county": None,
        "raw": text.strip()
    }

    # Pattern 1: BLOCK X, <SUBDIVISION> SEC/SECTION
    subdiv_match = re.search(
        r"BLOCK\s+\d+,\s*([A-Z\s]+?)\s+(SEC|SECTION)",
        text
    )

    # Pattern 2: <SUBDIVISION> SEC/SECTION (e.g., CANDELA SEC 13)
    if not subdiv_match:
        subdiv_match = re.search(
            r"^([A-Z\s]+?)\s+(SEC|SECTION)\s+\d+",
            text
        )

    if subdiv_match:
        data["subdivision"] = subdiv_match.group(1).strip()

    # SECTION
    sec_match = re.search(r"(SEC|SECTION)\s+(\d+)", text)
    if sec_match:
        data["section"] = sec_match.group(2)

    # BLOCK
    block_match = re.search(r"BLOCK\s+(\d+)", text)
    if block_match:
        data["block"] = block_match.group(1)

    # LOT
    lot_match = re.search(r"LOT\s+(\d+)", text)
    if lot_match:
        data["lot"] = lot_match.group(1)

    # COUNTY
    if "FORT BEND" in text or "FB" in text or "FORT BEND COUNTY" in text or "FBC" in text:
        data["county"] = "Fort Bend"

    return data


if __name__ == "__main__":
    sample = input("Paste legal description:\n")
    result = extract_legal_description(sample)
    print("\nExtracted JSON:\n")
    print(json.dumps(result, indent=4))
