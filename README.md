# json-ql

[![PyPI version](https://badge.fury.io/py/json-ql.svg)](https://badge.fury.io/py/json-ql)
[![Upload Python Package](https://github.com/Bharat23/json-ql/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Bharat23/wpt-ql/actions/workflows/python-publish.yml)

- ## [Getting Started](#getting-started)
    * [Prerequiste](#prerequiste)
    * [Installation](#installation)
    * [Examples](#example)
        * [Key Types](#key-type)
- ## [Available Methods](#available-methods)

## Getting Started

- ### Prerequisites
    - Python >= 3.6.x
    - pip

- ### Installation
    ```bash
    $ pip install json-ql
    ```

- ### Examples
    - Using the JSON ql
    ```python
    # import the class
    from json_ql import JSONQL
    
    test_json = Fetch().json()
    keys = ['data.median.firstView.loadTime',]
    # returns a new dict with specified keys
    JSONQL(test_json).pick(keys=keys).exec()

    ```

    - Using the JSONQL like a normal dictionary
    ```python
    # create an instance of the JSONQLDict
    # this creates a read only copy of original dictionary
    test_json = JSONQLDict({"name": "John Doe", "details": {"age": 23}})

    # query using the sample query language
    test_json['details.age']
    > 23
    ```
- ### Key Types:
    - #### key_name
        - Works like simple JSON extraction. Provide the name of the key and boom!.
        - For extraction from beyond first level, append keys with a separator and provide `key_delimiter` for the program to recognize the start of next level.
        - Example: 
        ```python
        """
        {
            keylevel11: {
                keylevel21: value,
                keylevel22: {
                    keylevel31: value
                }
            }
        }
        """
        # key to extract first level
        # keylevel11
        # returns {keylevel21: ...}

        # key to extract second level, first key
        # keylevel11.keylevel21
        # returns value
        ```
    - #### [list_index]
        - When you have a list as value and you want to extract a specific index value/object.
        - For extraction from beyond first level, append keys with a separator and provide `key_delimiter` for the program to recognize the start of next level.
        - Example: 
        ```python
        """
        {
            keylevel11: {
                keylevel21: [
                    1, 2, 3
                ],
                keylevel22: {
                    keylevel31: value
                }
            }
        }
        """
        # key to extract second level, third index
        # keylevel11.keylevel21.[2]
        # returns 3
        ```
    - #### [{key=value}]
        - When you have a unordered list of object and you want extract a specific object from the list based on the key and value inside the object
        - For extraction from beyond first level, append keys with a separator and provide `key_delimiter` for the program to recognize the start of next level.
        - Example: 
        ```python
        """
        {
            keylevel11: {
                keylevel21: [
                    1, 2, 3
                ],
                keylevel22: {
                    keylevel31: value
                },
                keylevel23: [
                    {
                        name: Awesome,
                    },
                    {
                        name: Package
                    }
                ]
            }
        }
        """
        # key to extract second level, and from that extarct the object with name = Awesome
        # keylevel11.keylevel23.[{name=Awesome}]
        # return {name: Awesome}
        ```
    
    - #### [{key~regex}]
        - When you have a unordered list of object and you want extract a specific object from the list based on the key and a regex of value inside the object
        - For extraction from beyond first level, append keys with a separator and provide `key_delimiter` for the program to recognize the start of next level.
        - The regex search is case sensitive. You do not need to add `//` or `r''` to write your regex.
        - The search will find all the matches and return a list
        - Example: 
        ```python
        """
        {
            keylevel11: {
                keylevel21: [
                    1, 2, 3
                ],
                keylevel22: {
                    keylevel31: value
                },
                keylevel23: [
                    {
                        name: Awesome123,
                    },
                    {
                        name: Package
                    }
                ]
            }
        }
        """
        # key to extract second level, and from that extarct the object with name matching Awesome
        # keylevel11.keylevel23.[{name~Awesome}]
        # return [{name: Awesome}]
        ```
    - #### [[ ... ]]
        - When the dict has a nested list and search needs to be done inside those wrap with `[]` to loop throught the list and find the data.
        - Inside the bracket `[]` add other expressions to do the lookup at inner most nested array.
        - Add `[]` pair for each nesting. 
        - `[]` in this is separate from `[index]`, `[{key~regex}]`, `[{key=value}]`. If there is a nested list of dictionary and we want to find an object by matching key value. Expression will look like this `[[{key=value}]]`
            - The outer most `[]` is for the outer list and inner `[]` is part of the key lookup expression syntax.
        - Example: 
        ```python
        """
        {
            keylevel11: {
                keylevel21: [
                    [{"key_arr": "1"}, {"key_arr": "4"}], 
                    [{"key_arr": "2"}, {"key_arr": "5"}], 
                    [{"key_arr": "3"}, {"key_arr": "6"}]
                ],
            }
        }
        """
        # key to extract second level, and from that extarct the object with name matching Awesome
        # keylevel11.keylevel21.[[{key_arr=5}]]
        # return {"keylevel11.keylevel21.[[{key_arr=5}]]": {"key_arr": "5"}}
        ```

### Available Methods

- JSONQL

| Method | Params | type | default | Description 
| --- | --- | --- | --- | --- |
| pick | key | str | None | selects a key to be returned
| pick | keys | list | [] | selects a list key to be returned
| pick | key_delimiter | str | "." | Separator used to identify multi level JSON
| pick | key_mapping | dict | {} | Mapping of keys for picking with custom key name. 

### Note:
 - The package is under development and will be prone to more frequent updates
