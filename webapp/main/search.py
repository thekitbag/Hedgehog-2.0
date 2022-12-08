class Search():
         
    def getSearchResults(search_term):
        results ={
            "number_of_results": 3,
            "results": [
                {
                    'id': 1,
                    "name": "restyrestaurant",
                    "photo_url": "https://www.cornerhouserestaurants.co.uk/templates/yootheme/cache/homepage-07-06bba36c.webp",
                    "score": 52,
                    "number_of_reviews": 469,
                    "most_mentioned": "Service, Cold, Wait"
                },
                {
                    'id': 2,
                    "name": "pubbypub",
                    "photo_url": "https://ichef.bbci.co.uk/news/1024/branded_news/D58F/production/_85217645_1024duke-william-3-public-b.jpg",
                    "score": 88,
                    "number_of_reviews": 133,
                    "most_mentioned": "Ales, Quiz, Landlord" 
                },
                {
                    'id': 3,
                    "name": "cacacacafe",
                    "photo_url": "https://www.spikeisland.org.uk/wp-content/uploads/2021/06/Spike_Cafe_Max-McClure_2621_sRGB_web.jpg",
                    "score": 68,
                    "number_of_reviews": 988,
                    "most_mentioned": "Cheap, Sausages, Friendly"
                },
            ]
        }
        return results


