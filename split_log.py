# 根据日志格式进行日志切割，参考nginx的日志格式配置
# 预处理出来变量名数组和分隔符数组，然后对照实际日志进行处理（按顺序查找分隔符，然后取出对应的变量名和实际日志中的日志字段，进行匹配）
# 这样做个练习或者简单的切割分析下日志还可以，还有一种更通用的方式：使用正则匹配来切割日志，这是trex可以去改进的一个方向
# 实际上这两个方式还是值得探讨的，如果使用正则的形式，需要自己构造正确的正则匹配式。自己切割的只需要把新的日志格式更新到配置文件中即可，剩下的就能自己去做切割了。

# 都先匹配成dict，然后针对dict中的字段进行处理
import re


def split_logformat(logformat):
    """
    返回两个列表vars，seqs，分别存储分割出来的变量key与变量之间的分隔符
    """
    vars = []
    seqs = []
    in_var = False
    var = seq = ''

    # 别看这几行代码简单，实际上逻辑还是挺有点绕的
    # 我有个思路：不用把情况区分到特别清晰明确的时候，类似状态机，每次遭遇某种情况就把所有相关的状态置成目标状态即可
    for ch in logformat:
        if ch == '$':
            if in_var:
                vars.append(var)
                var = ''
            else:
                var = ''
                in_var = True
                if seq:
                    seqs.append(seq)
                    seq = ''
        elif re.search(r'[0-9a-zA-Z_]+', ch):
            if in_var:
                var += ch
            else:
                seq += ch
        else:
            if in_var:
                vars.append(var)
                var = ''
                in_var = False
            seq += ch

    if var:
        vars.append(var)

    if seq:
        seqs.append(seq)

    return vars, seqs


def parse_log(line, seqs, vars):
    """根据采集到的字段名和分隔符逐行进行日志处理
    1. 逐次查询seqs中的字符，找到索引值，0-索引值为var_value
    2. var_key是顺序取到vars数组里的值
    3. 取出的数据使用hash表来存储
    """
    log_hash = {}
    var_idx = 0
    for seq in seqs:
        idx = line.index(seq)
        val = line[:idx]
        line = line[idx+len(seq):]
        log_hash[vars[var_idx]] = val
        var_idx += 1

    # 有些要根据测试去调整
    if line:
        log_hash[vars[var_idx]] = line

    return log_hash


if __name__ == "__main__":
    # """ """这个里面的空格也是会被计入的，所以下面的字符串为了防止多余的空格换行后要顶格写
    NGINX_LOG_FORMAT = """'$time_iso8601 $host $http_client_ip $http_x_haproxy_for $remote_addr "$request"'
' $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for" $request_time'
' "$upstream_addr" "$upstream_status"'
' "$upstream_connect_time" "$upstream_response_time"'
' "$upstream_response_length" "$upstream_http_x_reserve"'
' $kong_service_id "$kong_service_name"'
' $kong_route_id "$kong_route_paths"'
' $kong_consumer_id "$kong_consumer_username"'
' "$http_x_api_method" "$http_request_id"'"""

    logformat = re.sub(r"[\n']", "", NGINX_LOG_FORMAT)
    print(logformat)
    vars, seqs = split_logformat(logformat)
    print(vars)
    print(seqs)
    log_line = '2020-06-15T15:35:00+08:00 fire.com - - 127.0.0.1 "GET /atom HTTP/1.1" 200 3 "-" "curl/7.29.0" "-" 0.268 "127.0.0.1:4567" "200" "0.014" "0.248" "3" "-" 2767e1d9-1b5a-4174-a656-d91fbe8462f6 "fire.com" ff71632c-13e4-4dc5-9a13-462900c880c7 "/atom" - "-" "-" "-"'
    log_hash = parse_log(log_line, seqs, vars)
    print(log_hash)

    # 构造一个正则匹配的日志格式
    re_str = '^'
    for i, v in enumerate(vars):
        pre_re = '(?P<'
        post_re = '>.+)'
        re_str += pre_re + str(v) + post_re
        if i <= len(seqs) - 1:
            re_str += seqs[i]
    print(re_str)

    rs = re.search(re_str, log_line)
    print(rs.groupdict())