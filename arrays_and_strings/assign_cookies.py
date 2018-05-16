"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most
one cookie. Each child i has a greed factor g_i, which is the minimum size of a cookie that the child will be content
with; and each cookie j has a size s_j. If s_j >= g_i, we can assign the cookie j to the child i, and the child i will
be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Example 1:
Input: [1, 2, 3], [1, 1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is
1 content. You need to output 1.
"""


def get_content_children(greed_factors, cookies):
    greed_factors = sorted(greed_factors)
    cookies = sorted(cookies)

    greed_factor_idx = 0
    cookies_idx = 0
    content_children = 0
    while greed_factor_idx < len(greed_factors) and cookies_idx < len(cookies):
        if cookies[cookies_idx] >= greed_factors[greed_factor_idx]:
            content_children = content_children + 1
            greed_factor_idx = greed_factor_idx + 1

        cookies_idx = cookies_idx + 1

    return content_children


assert get_content_children([1, 2, 3], [1, 1]) == 1
assert get_content_children([1, 2], [1, 2, 3]) == 2
assert get_content_children([2, 2, 3], [1, 1, 1]) == 0
print("All test cases passed successfully.")
