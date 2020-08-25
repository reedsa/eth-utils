# flake8: noqa
from eth_utils import (
    ExtendedDebugLogger,
    HasExtendedDebugLogger,
    HasExtendedDebugLoggerMeta,
    HasLogger,
    HasLoggerMeta,
    ValidationError,
    add_0x_prefix,
    apply_formatter_at_index,
    apply_formatter_if as non_curried_apply_formatter_if,
    apply_formatter_to_array,
    apply_formatters_to_dict,
    apply_formatters_to_sequence,
    apply_key_map,
    apply_one_of_formatters as non_curried_apply_one_of_formatters,
    apply_to_return_value,
    big_endian_to_int,
    clamp,
    combine_argument_formatters,
    combomethod,
    decode_hex,
    denoms,
    encode_hex,
    event_abi_to_log_topic,
    event_signature_to_log_topic,
    flatten_return,
    from_wei,
    function_abi_to_4byte_selector,
    function_signature_to_4byte_selector,
    get_extended_debug_logger,
    get_logger,
    hexstr_if_str as non_curried_hexstr_if_str,
    humanize_bytes,
    humanize_hash,
    humanize_integer_sequence,
    humanize_ipfs_uri,
    humanize_seconds,
    import_string,
    int_to_big_endian,
    is_0x_prefixed,
    is_address,
    is_binary_address,
    is_boolean,
    is_bytes,
    is_canonical_address,
    is_checksum_address,
    is_checksum_formatted_address,
    is_dict,
    is_hex,
    is_hex_address,
    is_hexstr,
    is_integer,
    is_list,
    is_list_like,
    is_normalized_address,
    is_null,
    is_number,
    is_same_address,
    is_string,
    is_text,
    is_tuple,
    keccak,
    remove_0x_prefix,
    replace_exceptions,
    reversed_return,
    setup_DEBUG2_logging,
    sort_return,
    text_if_str,
    to_bytes,
    to_canonical_address,
    to_checksum_address,
    to_dict,
    to_hex,
    to_int,
    to_list,
    to_normalized_address,
    to_ordered_dict,
    to_set,
    to_text,
    to_tuple,
    to_wei,
)
from eth_utils.toolz import curry
from typing import Any, Callable, Sequence, Tuple, TypeVar, Union, overload

TReturn = TypeVar("TReturn")
TValue = TypeVar("TValue")


@overload
def apply_formatter_if(
    condition: Callable[..., bool]
) -> Callable[[Callable[..., TReturn]], Callable[[TValue], Union[TReturn, TValue]]]:
    ...


@overload
def apply_formatter_if(
    condition: Callable[..., bool], formatter: Callable[..., TReturn]
) -> Callable[[TValue], Union[TReturn, TValue]]:
    ...


@overload
def apply_formatter_if(
    condition: Callable[..., bool], formatter: Callable[..., TReturn], value: TValue
) -> Union[TReturn, TValue]:
    ...


# This is just a stub to appease mypy, it gets overwritten later
def apply_formatter_if(
    condition: Callable[..., bool],
    formatter: Callable[..., TReturn] = None,
    value: TValue = None,
) -> Union[
    Callable[[Callable[..., TReturn]], Callable[[TValue], Union[TReturn, TValue]]],
    Callable[[TValue], Union[TReturn, TValue]],
    TReturn,
    TValue,
]:
    ...


@overload
def apply_one_of_formatters(
    formatter_condition_pairs: Sequence[
        Tuple[Callable[..., bool], Callable[..., TReturn]]
    ]
) -> Callable[[TValue], TReturn]:
    ...


@overload
def apply_one_of_formatters(
    formatter_condition_pairs: Sequence[
        Tuple[Callable[..., bool], Callable[..., TReturn]]
    ],
    value: TValue,
) -> TReturn:
    ...


# This is just a stub to appease mypy, it gets overwritten later
def apply_one_of_formatters(
    formatter_condition_pairs: Sequence[
        Tuple[Callable[..., bool], Callable[..., TReturn]]
    ],
    value: TValue = None,
) -> TReturn:
    ...


@overload
def hexstr_if_str(
    to_type: Callable[..., TReturn]
) -> Callable[[Union[bytes, int, str]], TReturn]:
    ...


@overload
def hexstr_if_str(
    to_type: Callable[..., TReturn], to_format: Union[bytes, int, str]
) -> TReturn:
    ...


# This is just a stub to appease mypy, it gets overwritten later
def hexstr_if_str(
    to_type: Callable[..., TReturn], to_format: Union[bytes, int, str] = None
) -> TReturn:
    ...


apply_formatter_at_index = curry(apply_formatter_at_index)
apply_formatter_if = curry(non_curried_apply_formatter_if)
apply_formatter_to_array = curry(apply_formatter_to_array)
apply_formatters_to_dict = curry(apply_formatters_to_dict)
apply_formatters_to_sequence = curry(apply_formatters_to_sequence)
apply_key_map = curry(apply_key_map)
apply_one_of_formatters = curry(non_curried_apply_one_of_formatters)
from_wei = curry(from_wei)
get_logger = curry(get_logger)
hexstr_if_str = curry(non_curried_hexstr_if_str)
is_same_address = curry(is_same_address)
text_if_str = curry(text_if_str)
to_wei = curry(to_wei)
clamp = curry(clamp)

# Delete any methods and classes that are not intended to be importable from
#   eth_utils.curried
# We do this approach instead of __all__ because this approach actually prevents
#   importing the wrong thing, while __all__ only affects `from eth_utils.curried import *`
del Any
del Callable
del Sequence
del TReturn
del TValue
del Tuple
del TypeVar
del Union
del curry
del non_curried_apply_formatter_if
del non_curried_apply_one_of_formatters
del non_curried_hexstr_if_str
del overload
