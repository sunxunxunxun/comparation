pragma solidity ^0.4.25;
contract Signal {
    event Signal(address indexed source, bytes32 indexed topic, string value);

    constructor() public {}

    function signal(bytes32 topic, string memory value) public {
        emit Signal(msg.sender, topic, value);
    }
}