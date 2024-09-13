# first id from CIBT, second id from Abacus
from django.core.exceptions import ValidationError

DISTRICTS = [
  (25, 55),
  (26, 57),
  (53, 29),
  (27, 64),
  (63, 24),
  (64, 56),
  (18, 67),
  (5, 15),
  (6, 11),
  (41, 31),
  (54, 32),
  (7, 14),
  (29, 60),
  (65, 53),
  (55, 33),
  (19, 69),
  (30, 63),
  (31, 59),
  (1, 8),
  (37, 50),
  (66, 52),
  (32, 51),
  (20, 70),
  (44, 36),
  (33, 54),
  (56, 25),
  (40, 30),
  (34, 61),
  (58, 42),
  (21, 68),
  (12, 21),
  (47, 27),
  (59, 43),
  (35, 49),
  (48, 44),
  (39, 39),
  (28, 58),
  (45, 40),
  (43, 38),
  (42, 35),
  (11, 20),
  (57, 41),
  (46, 28),
  (8, 16),
  (15, 17),
  (13, 19),
  (14, 12),
  (22, 73),
  (23, 71),
  (49, 26),
  (2, 10),
  (36, 62),
  (16, 18),
  (60, 45),
  (9, 13),
  (17, 22),
  (3, 9),
  (61, 46),
  (68, 66),
  (67, 48),
  (50, 34),
  (51, 37),
  (62, 480),
  (10, 23),
  (38, 65),
  (4, 7),
  (24, 72),
  (52, 47),
]

def getDistrictIdByAbacusId(id):
  cibt_ids = [v[0] for i, v in enumerate(DISTRICTS) if v[1] == id]
  if len(cibt_ids) == 0:
    raise ValidationError('CIBT district not found')
  return cibt_ids[0]

REGIONS = [
  (3, 6),
  (4, 2),
  (4, 3),
  (1, 5),
  (2, 4),
]

def getRegionIdByAbacusId(id):
  cibt_ids = [v[0] for i, v in enumerate(REGIONS) if v[1] == id]
  if len(cibt_ids) == 0:
    raise ValidationError('CIBT region not found')
  return cibt_ids[0]