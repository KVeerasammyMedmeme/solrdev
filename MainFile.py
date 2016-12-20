import scorched

si=scorched.SolrInterface("http://10.30.2.170:8983/solr/Abstract")

"""Lets search for cancer"""
#response=si.query(memBody="cancer").execute()
#for r in response:
  #  print(r['id'])
    #print(r['txtTitle'])

"""To grab all id's do a cursor. Must include a sort_by the unique field"""
#for item in si.query(memBody="cancer").sort_by('id').cursor(rows=10000):
   # print(item['id'])

"""To get only the id fields..(other method).. dont recommend cannot create a cursor"""
#response = si.query(memBody="cancer").field_limit(["id"]).execute()

#for r in response:
 #   print(r)

