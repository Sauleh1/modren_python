from nptyping import DataFrame, Structure as S
from beartype import beartype

@beartype
def func(df: DataFrame[S["a: Int, b: Str"]]) -> DataFrame[S["a: Int, b"]]:
    return df

func("Hello, world!")
