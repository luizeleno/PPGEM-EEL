from requests import RequestException
import orcid

api = orcid.PublicAPI('APP-H43S7S70C6QGG5GY', '67c4ec09-c890-494a-b64b-7428e9edee90', sandbox=True)

token = api.get_token_from_authorization_code(authorization_code, redirect_uri)

#search_results = api.search_public('text:English')
# Get the summary
#token = api.get_token('APP-H43S7S70C6QGG5GY', '67c4ec09-c890-494a-b64b-7428e9edee90', redirect_uri)
#summary = api.read_record_public('0000-0002-3117-5116', 'activities', token)
#summary = api.read_record_public('0000-0002-3117-5116', 'record', token)
