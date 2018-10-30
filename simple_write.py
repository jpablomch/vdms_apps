import vdms

db = vdms.vdms()
db.connect('localhost', 55555)

props = {}
props["name"] = "Luis Remis"
props["team"] = "Boca Juniors"

addEntity = {}
addEntity["properties"] = props
addEntity["class"] = "TestClass"

query = {}
query["AddEntity"] = addEntity

all_queries = []
all_queries.append(query)

response, res_arr = db.query(all_queries)
