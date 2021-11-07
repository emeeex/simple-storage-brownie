// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 favouriteNumber;
    bool favouriteBool;

    struct People {
        uint256 favouriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavouriteNumber;

    function store(uint256 _favouriteNumber) public returns(uint256) {
        favouriteNumber = _favouriteNumber;
        return _favouriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favouriteNumber;
    }

    function addPerson(string memory _name, uint256 _favouriteNumber) public {
        people.push(People(_favouriteNumber, _name));
        nameToFavouriteNumber[_name] = _favouriteNumber;
    }
}