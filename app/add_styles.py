from model import Artwork, Style, DB
import requests
from progress.bar import Bar

addr = 'https://api.artsy.net/api/'
client_keys = {"client_id":"533eee8fdca1be50c953",
               "client_secret":"f998c3a6b51290031fe9a90b4373e158"}
auth_response = requests.post(addr + 'tokens/xapp_token', data=client_keys)
del client_keys
token = auth_response.json()['token']
headers = {'X-Xapp-Token':token}

def add_styles():
    artworks = Artwork.query.all()
    bar = Bar('Retrieving genes', max=len(artworks))
    for w in artworks:
	bar.next()
        gene_url = addr + 'genes'
        gene_params = {'artwork_id':w.id}
        gene_response = requests.get(gene_url, params=gene_params,
                                     headers=headers)
        genes = gene_response.json()['_embedded']['genes']
        for g in genes:
            style = Style.query.filter_by(id=g['id']).first()
            if style is not None:
                style.artworks.append(w)
                DB.session.commit()
    bar.finish()

if __name__ == '__main__':
    add_styles()
