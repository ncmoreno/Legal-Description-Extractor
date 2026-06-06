# Legal-Description-Extractor
Tiny Python tool that converts legal descriptions into structured JSON
## Example

Input:
LOT 12, BLOCK 3, MEADOWS SEC 4, FORT BEND COUNTY

Output:
{
  "lot": "12",
  "block": "3",
  "section": "4",
  "subdivision": "MEADOWS",
  "county": "Fort Bend",
  "unit": null
}

## Why this exists
Legal descriptions are inconsistent and often poorly formatted.  
This tool provides a quick way to normalize them for:

- parcel research  
- appraisal workflows  
- GIS preprocessing  
- QA checks  

## Usage
Run the script:
extractor.py
Paste a legal description when prompted.

## Notes
This is a simple rule-based extractor.  
It can be extended with AI or NLP for more complex descriptions.
