# Your code here
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    file_dict = {}
    for path in files:
        #split paths into directories
        file_dirs = path.split('/')[-1]
        #if directory already exists, append path
        if file_dirs in file_dict:
            file_dict[file_dirs].append(path)
        else:
            file_dict[file_dirs] = path

    results = []
    # TODO: reduce complexity
    #check all queries for files with matching paths
    for query in queries:
        if query in file_dict:
            result = file_dict[query]            
            for path in result:
                results.append(path)
    
    return results

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
