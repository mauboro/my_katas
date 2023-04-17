websites = []
def add_to_websites():
    for i in range(1000):
        websites.extend(["codewars"])
    
add_to_websites()

#or

websites = ["codewars"] * 1000
