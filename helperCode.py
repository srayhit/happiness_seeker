pos_actions_list = ['music', 'friends', 'share', 'vacation', 'family', 'restaurant','movies','workout','activity']
neg_actions_list = ['jokes', 'music', 'friends', 'vacation', 'family', 'restaurant','movies','workout','partner','doctor','activity']
neu_actions_list = ['music', 'friends','movies','workout','partner','doctor','activity']


set_1 =set(pos_actions_list)
set_2 =set(neg_actions_list)
set_3 = set(neu_actions_list)

pos_not_in_neg = list(set_1 - set_2)
comb_pos_neg = neg_actions_list + pos_not_in_neg

set_4 = set(comb_pos_neg)
comb_not_in_neu = list(set_4 - set_3)

comb = neu_actions_list + comb_not_in_neu

print(comb)