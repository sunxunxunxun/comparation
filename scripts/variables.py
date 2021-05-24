OYNETE = {
    'evm_code_coverage': 0,    # float
    'callstack': 1,  # bool
    'reentrancy': 2, # bool
    'integer_overflow': 3,   # int
    'integer_underflow': 4,  # int
    'time_dependency': 5,    # bool
    'money_concurrency': 6,  # bool
}

OSIRIS = {
    'evm_code_coverage': 0,    # float
    'callstack': 1,  # bool
    'reentrancy': 2, # bool
    'overflow': 3,   # int
    'underflow': 4,  # int
    'time_dependency': 5,    # bool
    'money_concurrency': 6,  # bool
    'timeout': 7,   # bool
    'division': 8,  # int
    'execution_time': 9,    # float
    'signedness': 10,   # int
    'assertion_failure': 11,    # bool
    'modulo': 12,   # bool
    'execution_paths': 13,  # int
    'truncation': 14,
}

VANDAL = {
    'reentrantCall': 0, # int
    'originUsed': 1,     #
    'checkedCallStateUpdate': 2,  #
    'uncheckedCall': 3,  # int
    'unsecuredValueSend': 4, #
    'destroyable': 5,    #
}

mythril = {
    "100": "Function Default Visibility",
    "101": "Integer Overflow and Underflow",
    "102": "Outdated Compiler Version",
    "103": "Floating Pragma",
    "104": "Unchecked Call Return Value",
    "105": "Unprotected Ether Withdrawal",
    "106": "Unprotected SELFDESTRUCT Instruction",
    "107": "Reentrancy",
    "108": "State Variable Default Visibility",
    "109": "Uninitialized Storage Pointer",
    "110": "Assert Violation",
    "111": "Use of Deprecated Solidity Functions",
    "112": "Delegatecall to Untrusted Callee",
    "113": "DoS with Failed Call",
    "114": "Transaction Order Dependence",
    "115": "Authorization through tx.origin",
    "116": "Timestamp Dependence",
    "117": "Signature Malleability",
    "118": "Incorrect Constructor Name",
    "119": "Shadowing State Variables",
    "120": "Weak Sources of Randomness from Chain Attributes",
    "121": "Missing Protection against Signature Replay Attacks",
    "122": "Lack of Proper Signature Verification",
    "123": "Requirement Violation",
    "124": "Write to Arbitrary Storage Location",
    "125": "Incorrect Inheritance Order",
    "127": "Arbitrary Jump with Function Type Variable",
    "128": "DoS With Block Gas Limit",
    "129": "Typographical Error",
    "132": "Unexpected Ether Balance",
    "135": "Effect Free Code",
}
