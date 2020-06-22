
def do_stuff():
    # get all keys/values from dict
    keys_ = list(some_dict.keys())
    formatted_values_ = ["%.2f" % member for member in list(some_dict.values())]
    
    # create aggregate lists
    
    # substring with last occurance of `.`
    subs_ = str_[0:str_.rfind(".")]
    module_names = [l[0:l.rfind(".")] for l in keys_]
    
    # dict
    _info = {}
    # double loop
    _data = list([f[i] for f in data_table] for i in [1, 2, 3])
    _info['total'] = sum([_data[i][0] for i in range(0,2)])
    _info['min_'] = min(_data[0])
    _info['max_'] = max(_data[0])
    _info['last_'] = _data[0][len(_data[0]) - 1]
