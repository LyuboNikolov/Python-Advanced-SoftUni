def even_odd_filter(**kw_nums):
    if "even" in kw_nums:
        kw_nums["even"] = [num for num in kw_nums["even"] if int(num) % 2 == 0]

    if "odd" in kw_nums:
        kw_nums["odd"] = [num for num in kw_nums["odd"] if int(num) % 2 != 0]

    return dict(sorted(kw_nums.items(), key=lambda x: (-len(x[1]))))
