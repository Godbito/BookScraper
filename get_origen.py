item = 'https://www.bookmarked.club/people/warren-buffett'

def split_url(my_item):
    author_with_dash = my_item.split('/')[-1]
    return author_with_dash

def remove_dash(recommended_by_with_dash):
    recommended_by_nodash = recommended_by_with_dash.split('-')
    return recommended_by_nodash

def capitalize_str(recommended_by_no_dash):
    recommender_uprcased = [x.capitalize() for x in recommended_by_no_dash]
    return recommender_uprcased

def list_to_string(capitalized_recommender_name):
    recommender = " "
    return (recommender.join(capitalized_recommender_name))
def get_origen(item):
    recommended_by_with_dash = split_url(item)
    recommended_by_no_dash = remove_dash(recommended_by_with_dash)
    capitalized_recommender_name = capitalize_str(recommended_by_no_dash)
    recommender = list_to_string(capitalized_recommender_name)
    return recommender

    #list_to_string



    #print(nodash)
    #
    #print(convert_to_upper)
    #origin =

get_origen(item)
