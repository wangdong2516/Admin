namespace py example


struct Data {
    1: string text,
    2: i32 id,
}

const i32 INT_MAX= 10

service format_data {
    /* 返回值 函数名(参数类型 参数名)*/
    Data do_format(1:Data data),
}