class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        if veganFriendly == 1:
            for restaurant in restaurants:
                if restaurant[2] == 1 and restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                    res.append([restaurant[1], restaurant[0]])
        else:
            for restaurant in restaurants:
                if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                    res.append([restaurant[1], restaurant[0]])
        
        res.sort(reverse=True)
        ans = [x[1] for x in res]
        return ans