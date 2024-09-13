CATEGORY_COLUMN = 'Category_'
CATEGORY_COLUMN_ID = 3
COLUMN_NUMBER = 7
LLP_COLUMN_SUM = 'LLP TJS'

CATEGORY = {
  "c1": {
    "id": 1,
    "desc": "Standard",
    "TJS": 0.02,
    "USD": 0.03,
  },
  "c2": {
    "id": 2,
    "desc": "Under_control",
    "TJS": 0.05,
    "USD": 0.1
    # late 8-30 days
  },
  "c3": {
    "id": 3,
    "desc": "Not_standard",
    "TJS": 0.3,
    "USD": 0.4
    # late 30-90 days or RSCHD or Court case
    # 100% if not collateral
  },
  "c4": {
    "id": 4,
    "desc": "Uncertain",
    "TJS": 0.75,
    "USD": 0.85
    # late 90-180 days or RSCHD or Court case
    # 100% if not collateral
  },
  "c5": {
    "id": 5,
    "desc": "Hopeless",
    "TJS": 1.0,
    "USD": 1.0
    # late more than 180 days or RSCHD or Court case
    # 100% if not collateral
  }
}