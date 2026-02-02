# T.1 Phiên bản cơ bản
authorized_dealers = [
  {
    "name" : "An Phát",
    "city" : "TPHCM",
    "rating" : "4.8",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "Nguyễn Công",
    "city" : "DN",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
  {
    "name" : "Đại Việt",
    "city" : "TPHCM",
    "rating" : "4.8",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "Long Hân",
    "city" : "HN",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
  {
    "name" : "Phúc Thịnh",
    "city" : "TPHCM",
    "rating" : "4.4",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "An Vinh",
    "city" : "DL",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
  {
    "name" : "Ngọc An",
    "city" : "TPHCM",
    "rating" : "4.7",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "An Cường",
    "city" : "GL",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
]

# T.1
favor_dealer = [dealer['name'] for dealer in authorized_dealers if (float(dealer['rating'])) > 4.6 and dealer["city"] == "TPHCM" ]
print(favor_dealer)

# T.1 Phiên bản refactor
def dealer_filter():
  authorized_dealers = [
  {
    "name" : "An Phát",
    "city" : "TPHCM",
    "rating" : "4.8",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "Nguyễn Công",
    "city" : "DN",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
  {
    "name" : "Đại Việt",
    "city" : "TPHCM",
    "rating" : "4.8",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "Long Hân",
    "city" : "HN",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
  {
    "name" : "Phúc Thịnh",
    "city" : "TPHCM",
    "rating" : "4.4",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "An Vinh",
    "city" : "DL",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
  {
    "name" : "Ngọc An",
    "city" : "TPHCM",
    "rating" : "4.7",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "An Cường",
    "city" : "GL",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
]
  filtered_dealer = [d['name'] for d in authorized_dealers if (float(d['rating'])) > 4.6 and d["city"] == "TPHCM"]
  return filtered_dealer
result = dealer_filter()
print(result)