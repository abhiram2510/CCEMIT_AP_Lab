def count_local_variable():
    var1=5
    var2="nnvr"
    var3=[9,8,7]
    var4={"a":1,"b":2}
    local_variable=locals()
    return len(local_variable)
n_local_variable=count_local_variable()
print("no.of local variables:",n_local_variable)