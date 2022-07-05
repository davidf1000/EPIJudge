from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    # TODO - you fill in here.
    # looping item in str 
    # .. -> pop stack (directory)
    # . -> do nothing 
    # '//' -> empty -> do nothing
    stack = []

    if not path:
        raise ValueError()
    # special case: absolute path
    if path[0] == '/':
        stack.append('/')
    for item in (token for token in path.split('/') if token not in['','.']):
        if item=='..':
            # can only append if path name is stack is empty or [-1]==//
            if len(stack)==0 or stack[-1]=='..':
                stack.append(item)
            else:
                if stack[-1] == '/':
                    raise ValueError()
                stack.pop()
        else:
            stack.append(item)
    result = '/'.join(stack) 
    return result[1:] if result[0:2]=='//' else result


if __name__ == '__main__':
    # string = '/usr/bin/david//../../../'
    # print(shortest_equivalent_path(string))
    # exit()
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
