import requests
import json
import pprint

data = {"data" : "24.3"}
data_json = json.dumps(data)
# Accept: application/json

headers = {'Accept': 'application/json'}

resp_person = requests.get("https://research.vu.nl/ws/api/59/persons?q=harmelen&apiKey=1aecc9b3-0b58-4e00-b757-c1a8026cbbfd",  headers=headers)
response_person = resp_person.json()
pprint.pprint(response_person)

#Details author
title = response_person['items'][0]['titles'][0]['value']
firstName = response_person['items'][0]['name']['firstName']
lastName = response_person['items'][0]['name']['lastName']
scopusID = (response_person['items'][0]['ids'][1]['value'])
pureID = response_person['items'][0]['uuid']

print type(str(pureID)

resp_research_outputs = requests.get("https://research.vu.nl/ws/api/59/persons/" + "/research-outputs?apiKey=1aecc9b3-0b58-4e00-b757-c1a8026cbbfd")
if resp_person.status_code != 200:
    # This means something went wrong.
    print('life is hard')
    raise ApiError('GET /tasks/ {}'.format(resp_person.status_code))



# print(type(resp))
# print (resp.status_code)

# print(title)
# print(firstName)
# print(lastName)
# print(scopusID)
print(pureID)
#
# lastName.split()
#
# lastName = lastName.replace(" ","_")
# firstName = firstName.replace(" ","_")
# title = title.replace(" ","_")


#==============================
# Extra Information from PURE
#==============================
# #IDS
# print(response_person['items'][0]['externalableInfo']['secondarySources']) #Same ID a Scopus ID
# print(response_person['items'][0]['ids']) #Second element [1] is the same as the scopus ID
# id_person = response_person['items'][0]['uuid'] #Person-ID of Pure?
#
#     #Name Variance
# print(response_person['items'][0]['nameVariants'])
# #Name Title
# print(response_person['items'][0]['titles'])
#
# #E-mail
# print(response_person['items'][0]['staffOrganisationAssociations'][0]['emails'][0]['value'])


#Keywords workfield?
# print(response_person['items'][0]['keywordGroups'][0]['keywords'])



# #=========================
# # Publications
# #========================
# resp_publications = requests.get("https://research.vu.nl/ws/api/59/persons/" + id_person +"/research-outputs?apiKey=1aecc9b3-0b58-4e00-b757-c1a8026cbbfd",  headers=headers)
#
#
# resp_publications = requests.get("https://research.vu.nl/ws/api/59/persons/b36edb65-746c-46be-9ecb-e532eb23c24e/research-outputs?apiKey=1aecc9b3-0b58-4e00-b757-c1a8026cbbfd",  headers=headers)
# if resp_publications.status_code != 200:
#     # This means something went wrong.
#     print('life is hard')
#     raise ApiError('GET /tasks/ {}'.format(resp_publications.status_code))
#
# response_publications = resp_publications.json()
# pprint.pprint(response_publications)
#
#
# print (response_publications['count'])
#
# print (response_publications['items'])



#=======================
#RDFLIB
#=======================

# from rdflib import Graph, RDF, Namespace, Literal, URIRef

# g = Graph()
#
# EX = Namespace('http://example.com/KE4KE/')
# g.bind('ex', EX)

# rdfLastName = URIRef("http://example.com/KE4KE/" + scopusID)


from rdflib import URIRef, BNode, Literal

# title = URIRef("http://example.org/title/" + title)
# firstName = URIRef("http://example.org/firstname/" + firstName)
# lastName = URIRef("http://example.org/lastName/" + lastName)
# scopusID = URIRef("http://example.org/scopusID/" + scopusID)
# pureID = URIRef("http://example.org/pureID/" + pureID)


title = Literal(title)
firstName = Literal(firstName)
lastName = Literal(lastName)
scopusID = Literal(scopusID)
pureID = Literal(pureID)

hasScopusID = URIRef("http://example.org/hasScopusID")
hasPureID = URIRef("http://example.org/hasPureID")


linda = BNode() # a GUID is generated



# print(title)
# print(firstName)
# print(lastName)

from rdflib import Namespace

n = Namespace("http://example.org/people/")
#
# n.scopusID = rdflib.term.URIRef(u'http://example.org/people/bob')
# n.eve = rdflib.term.URIRef(u'http://example.org/people/eve')


from rdflib.namespace import RDF, FOAF


# RDF.type = rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type')

# FOAF.knows = rdflib.term.URIRef(u'http://xmlns.com/foaf/0.1/knows')


from rdflib import Graph
g = Graph()

g.add( (lastName, RDF.type, FOAF.Person) )
g.add( (lastName, FOAF.title, title) )
g.add( (lastName, FOAF.firstName, firstName) )
g.add( (lastName, FOAF.lastName, lastName) )
g.add( (lastName, hasScopusID, scopusID) )
g.add( (lastName, hasPureID, pureID) )


# print (g.serialize(format='turtle'))


file = open("data.ttl", mode="w")

def serialize(filename):
    g.serialize(destination=filename, format='turtle')
    print("File is saved")

def save(filename):
    with open(filename, 'w') as f:
        g.serialize(f, format='turtle')


def load(filename):
    with open(filename, 'r') as f:
        g.load(f, format='turtle')


serialize('data.ttl')
