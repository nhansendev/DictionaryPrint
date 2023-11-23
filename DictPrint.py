# Copyright (c) 2023, Nathan Hansen
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

def try_format(data, format):
    def func(data, format):
        try:
            return f'{data:{format}}'
        except TypeError:
            return data
    return _format(data, func, format)


def try_round(data, places):
    def func(data, places):
        try:
            return round(data, places)
        except TypeError:
            return data
    return _format(data, func, places)


def _format(data, func, arg):
    if isinstance(data, list) or isinstance(data, tuple):
        out = []
        for d in data:
            out.append(func(d, arg))
        return out if isinstance(data, list) else tuple(out)
    else:
        return func(data, arg)


def dict_print(data, level_char='>', offset_char=' ', pad_char='_', rounding=None, sort_kwargs=None, compact=False, _offset=0, _first=False, num_format=None, exclude=None):
    # Fancy printing of dictionaries in a human-readable format
    def _recurr(data, level_char=level_char, offset_char=offset_char, rounding=rounding, sort_kwargs=sort_kwargs, _offset=_offset, _first=_first):
        key_list = [k for k in list(data.keys()) if exclude is None or k not in exclude]
        if len(key_list) > 0:
            if sort_kwargs is not None:
                if sort_kwargs == 'len':
                    sort_kwargs={'reverse': True, 'key': lambda x: len(x)}
                key_list.sort(**sort_kwargs)
            key_lens = [len(str(k)) for k in key_list]
            long_key = max(key_lens)

            for idx in range(len(key_list)):
                v = data[key_list[idx]]
                diff = long_key-key_lens[idx]
                prefix = pad_char*diff
                if len(prefix) > 0:
                    prefix = prefix[:-1] + ' '
                if _first:
                    _first = False
                else:
                    if _offset > 0:
                        prefix = offset_char*(_offset-2) + level_char + ' ' + prefix
                    print()
                if isinstance(v, dict):
                    print(f'{prefix}{key_list[idx]}: ', end='')
                    _recurr(v, _offset=_offset+long_key+2, _first=compact, level_char=level_char)
                else:
                    if rounding is not None:
                        print(f'{prefix}{key_list[idx]}: {try_round(v, rounding)}', end='')
                    elif num_format is not None:
                        print(f'{prefix}{key_list[idx]}: {try_format(v, num_format)}', end='')
                    else:
                        print(f'{prefix}{key_list[idx]}: {v}', end='')
        else:
            print(f'<Input dictionary is empty: {data}>')

    _recurr(data, level_char=level_char, offset_char=offset_char, rounding=rounding, sort_kwargs=sort_kwargs, _offset=_offset, _first=_first)
    print()
