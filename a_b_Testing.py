from scipy.stats import ttest_ind


def membership_spendingABTesting(data):
    # Örnek olarak, üyelik türlerine göre harcama farklılıklarını test etme
    gold_members = data[data['Membership Type'] == 'Gold']['Total Spend']
    bronze_members = data[data['Membership Type'] == 'Bronze']['Total Spend']
    t_stat, p_val = ttest_ind(gold_members, bronze_members)
    print("T-test Sonucu: p-değeri membership-spending =", p_val)

def membership_satisfactionABTesting(data):
    gold_members = data[data['Membership Type'] == 'Gold']['Satisfaction Level']
    bronze_members = data[data['Membership Type'] == 'Bronze']['Satisfaction Level']
    t_stat, p_val = ttest_ind(gold_members, bronze_members)
    print("T-test Sonucu: p-değeri membership-satisfaction =", p_val)

