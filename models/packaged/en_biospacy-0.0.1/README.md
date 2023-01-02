A spaCy pipeline for parsing biology texts. Data for the plant EntityRuler was found at: http://www.worldfloraonline.org/

| Feature | Description |
| --- | --- |
| **Name** | `en_biospacy` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.4.4,<3.5.0` |
| **Default Pipeline** | `sentencizer`, `plant_taxonomy`, `binomina` |
| **Components** | `sentencizer`, `plant_taxonomy`, `binomina` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [W.J.B. Mattingly](https://github.com/wjbmattingly/biospacy) |

### Label Scheme

<details>

<summary>View label scheme (12 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`plant_taxonomy`** | `DOMAIN`, `FAMILY`, `GENUS`, `KINGDOM`, `ORDER`, `PHYLUM-ANIMALIA`, `PHYLUM-BACTERIA`, `PHYLUM-FUNGI`, `PHYLUM-PLANTS`, `PHYLUM-PROTISTA`, `SPECIES`, `SUBFAMILY` |

</details>