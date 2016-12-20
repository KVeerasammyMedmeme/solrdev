import scorched

print("Starting Solr Demo..")

#memBody:(heart failure OR cardiac insufficiency OR chf OR Congestive cardiomyopathy OR congestive heart failure OR Dilated Cardiomyopathy OR Familial dilated cardiomyopathy OR Heart failure congestive OR Idiopathic dilation cardiomyopathy OR primary dilated cardiomyopathy)
try:

    si=scorched.SolrInterface("http://localhost:8983/solr/Abstracts/")
    # response=si.query(memBody="cancer").execute()
    #
    # for r in response:
    #     print(r['id'])
    # response =  si.query(memBody_S="pancreatitis").postings_highlight(['memBody_S']).execute()
    # response=si.query(memBody="cancer").facet_by('year').execute()
    # facets=response.facet_counts.facet_fields
    # facet_list = facets['year']
    #
    # sorted_facet_list = sorted(facet_list, key=lambda year: year[0], reverse=True)
    # for key, val in sorted_facet_list:
    #     print(key, val)

    # print(facets)
    # print(facets['year'])
    # facet_list=[]
    # for key in facets:


    # count=0
    # for r in response:
    #     print(r)
    #     print(" ")
    #     count=count+1
    #     if count>=15:
    #         break

    resp = si.query(memBody_S="pancreatitis").postings_highlight(['memBody_S']).execute()
    for re in resp:
       print(re)
    #  print("Hello")
    #response=si.query(memBody="digoxin").execute()

    #print(response)
    #"""Query Pete's Example Declare Filter query for client subscription, then query in that subset"""

    #response=si.query(memBody="digoxin").filter(si.Q(si.Q(memBody="heart failure OR cardiac insufficiency OR chf OR Congestive cardiomyopathy OR congestive heart failure OR Dilated Cardiomyopathy OR Familial dilated cardiomyopathy OR Heart failure congestive OR Idiopathic dilation cardiomyopathy OR primary dilated cardiomyopathy")
                                                  # &
     #si.Q(txtTitle="heart failure OR cardiac insufficiency OR chf OR Congestive cardiomyopathy OR congestive heart failure OR Dilated Cardiomyopathy OR Familial dilated cardiomyopathy OR Heart failure congestive OR Idiopathic dilation cardiomyopathy OR primary dilated cardiomyopathy"))
                                            # ).postings_highlight(['memBody','txtTitle']).highlight("digoxin").options()
    #result=solr_interface.query(memBody="diagoxin").filter(memBody="heartfilter" | memBody="cardiac insufficency")


    #print(result)
    #for r in result:
     #   print(r['id'])


    #for d in response:
        #print(d)

except Exception as e:
    print(e)


