The REST service for the task assigned is created using a Flask application based on Python3.

It is necessary that the system which is used to run the application has python version >=3.10 installed, either globally or in some virtual environment.

If using a virtual environment, please activate the environment and then follow the instructions provided for running the server.

## Installation
### Flask Application Structure 

.  
|───server.py  
|───generator.py  
|───requirements.txt    
|───README.md  


### Install all the dependicies

pip install -r requirements.txt --user


## Run Flask

$ python server.py

In flask, Default port is 5000

Note : Make sure that nothing else is running on the port 5000

Default Route:  http://127.0.0.1:5000/

Product Search Route: http://127.0.0.1:5000/generate

## Description of the REST service:
The service basically takes *2* parameters via a *GET* request over the route http://127.0.0.1:5000/generate.
The description of the parameters is as follows:

> api : It takes the api_key which is used by the embedder used to process the query
> 
> query : It takes the query according to which we will performing the product fetch
>
Sample Keys :
bash
bCNtxW0EXr7iZJrzCHaHXnK8AfHkgKTXm9nB5oMl
1aUCEzPz8dppl4kmfl4OBrvUnbxHMj8sEY8iFsjr

Sample Query :
bash
Which recipe is butter cookie, what country

## Here is a sample GET request to the REST service:
#### Using a bash command
bash
curl --location 'http://127.0.0.1:5000/generate?api=SZj5v5c9I7uEvpjgSLNMoQpIYvAcYpEcxrqgkrZg&query=Which%20recipe%20is%20toothpate%2C%20what%20country'

#### Using a url
http://127.0.0.1:5000/generate?api=SZj5v5c9I7uEvpjgSLNMoQpIYvAcYpEcxrqgkrZg&query=Which recipe is toothpate, what country

## Here is the response of the above GET request:
JSON
[
    {
        "brand": "Pepsodent",
        "category": "Beauty & Hygiene",
        "description": "Get pearly white teeth with this Pepsodent Whitening Germ check+ Toothpaste. The specially designed formula of this toothpaste helps fight tooth cavities and decay. The protective elements in this toothpaste helps prevent plaque formation and gum sensitivity. With a fresh flavour, the toothpaste gives an everlasting fresh and clean breath. Regular use of it results in lesser bacteria and germ formation. This toothpaste is perfect for every member of your family from toddlers to elders. So dont worry about indulging in your favorite foods ever again!",
        "index": "910",
        "market_price": 100.0,
        "product": "Toothpaste - Whitening, Cavity Protection, 150 G",
        "rating": 4.2,
        "sale_price": 85.0,
        "sub_category": "Oral Care",
        "type": "Toothpaste"
    },
    {
        "brand": "Dabur",
        "category": "Beauty & Hygiene",
        "description": "Meswak is made from a rare herb, which grows slowly, resisting the brutal forces of nature amidst the sand dunes of Africa and South Asia. Even a small portion of this herb is capable to provide Complete Oral Care. Dabur brings to you, this herb in the form of Incredible Meswak Toothpaste. It is scientifically proven to help reduce tartar and plaque, fight germs and bacteria to keep gums healthy, helps prevent tooth decay, eliminate bad breath and ensure strong teeth, all at once to provide Complete Oral Care.",
        "index": "517",
        "market_price": 525.0,
        "product": "Meswak Toothpaste",
        "rating": 4.3,
        "sale_price": 426.3,
        "sub_category": "Oral Care",
        "type": "Toothpaste"
    },
    {
        "brand": "Clove",
        "category": "Beauty & Hygiene",
        "description": "Clove is your very own dental care expert made by Indians for Indians. Clove Power is an anti-cavity toothpaste that contains a unique formula that freshens breath with the goodness of clove oil. Formulated with Dentist approved ingredients, it helps clean teeth to make them whiter and stronger. It helps reduce the formation of plaque and tartar above the gum line which helps fight against gingivitis, stains, tartar, and cavities. Fluoride gives protection against tooth decay and strengthens teeth. Clove Power has excellent foaming action with smooth & easy flow ensuring it gets to every corner of your whole mouth and fights bacteria on teeth, tongue, cheeks, and gums. Also, it whitens the teeth, protects the enamel and prevents bleeding gums. Say goodbye to bad breath, decay and gum disease as you welcome Clove Power toothpaste. Clove Power has a unique flavour (Clove + Mint) formulated by Symrise, a world-renowned flavouring company based in Germany and manufactured in India by Dabur.\n \nClove is your very own dental care expert made by Indians for Indians. Clove Sensitive helps relieve the sharp or sudden pain caused by sensitive teeth. The toothpaste is formulated with Dentist approved ingredients to provide long-lasting relief from sensitivity and help prevent cavities. With the goodness of clove oil & mint, it helps reduce the formation of plaque and tartar above the gum line and fight against gingivitis, stains, tartar, and cavities. Fluoride gives protection against tooth decay and strengthens teeth. Clove Sensitive has excellent foaming action with smooth & easy flow ensuring it gets to every corner of your whole mouth and fights bacteria on teeth, tongue, cheeks, and gums, enamel protection and prevents bleeding gums. Say goodbye to sensitive teeth and gums as you welcome Clove Sensitive toothpaste. Clove Sensitive has a unique flavour (Clove + Mint) formulated by Symrise, a world-renowned flavouring company based in Germany and manufactured in India by Dabur.",
        "index": "381",
        "market_price": 240.0,
        "product": "Power - Fresh Breath Fluoride Toothpaste 100 g + Sensitive Toothpaste 80 g",
        "rating": NaN,
        "sale_price": 203.99,
        "sub_category": "Oral Care",
        "type": "Toothpaste"
    },
    {
        "brand": "Pepsodent",
        "category": "Beauty & Hygiene",
        "description": "Reduce those dental visits with this Expert Protection Gum Care Toothpaste from Pepsodent. Formulated with Zinc Citrate technology, this toothpaste not only takes care of your teeth, but provides you with the best gum care. Its advanced formula consists of Germ check and Gum guard to provide you with Complete-8 action oral care. Its anti-bacterial formula prevents your teeth from cavities, reduces tartar and lactic acid, and eliminates bacteria to give you a refreshing breath and healthier teeth & gums. \n\n\nPerfect for the whole family, this toothpaste should be used twice daily for effective results. Buy this value pack right away and get the complete oral care for your teeth and gums. A quality product of Unilever Dental Research. TM Regd. Made in India.",
        "index": "207",
        "market_price": 98.0,
        "product": "Toothpaste - Gum Care, Expert Protection",
        "rating": 4.3,
        "sale_price": 78.4,
        "sub_category": "Oral Care",
        "type": "Toothpaste"
    }
]
