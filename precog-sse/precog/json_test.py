import json

{
    "ecfffb00-28b5-4f79-9808-96de5035f889": {
        "name": "SpaceX Rocket",
        "description": {
            "table": {
                "steps": [
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "atKey",
                                                                        "value": {
                                                                            "cursor": {
                                                                                "tag": "Nothing"
                                                                            },
                                                                            "key": "launch_site"
                                                                        }
                                                                    }
                                                                },
                                                                "key": "site_name_long"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e6fd9519-bd9e-4584-93ee-eb70c57e142e",
                                                "path": "/latest",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "daf74161-6d2e-4a34-8109-37a683dc9deb"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "atKey",
                                                                        "value": {
                                                                            "cursor": {
                                                                                "tag": "Nothing"
                                                                            },
                                                                            "key": "launch_site"
                                                                        }
                                                                    }
                                                                },
                                                                "key": "site_name"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e6fd9519-bd9e-4584-93ee-eb70c57e142e",
                                                "path": "/latest",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "25d00714-f243-4a8b-9f07-8b20072f3d2c"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "details"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e6fd9519-bd9e-4584-93ee-eb70c57e142e",
                                                "path": "/latest",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "3bb3a6d8-47c1-46c1-a1bd-65bac68aec99"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "atKey",
                                                                        "value": {
                                                                            "cursor": {
                                                                                "tag": "Nothing"
                                                                            },
                                                                            "key": "rocket"
                                                                        }
                                                                    }
                                                                },
                                                                "key": "rocket_type"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e6fd9519-bd9e-4584-93ee-eb70c57e142e",
                                                "path": "/latest",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "4f1f5083-38b6-4565-9749-2fc88cf7cb03"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "atKey",
                                                                        "value": {
                                                                            "cursor": {
                                                                                "tag": "Nothing"
                                                                            },
                                                                            "key": "rocket"
                                                                        }
                                                                    }
                                                                },
                                                                "key": "rocket_name"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e6fd9519-bd9e-4584-93ee-eb70c57e142e",
                                                "path": "/latest",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "421beb9b-4c70-4db4-8f6e-39e4aff6c4dc"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "launch_year"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e6fd9519-bd9e-4584-93ee-eb70c57e142e",
                                                "path": "/latest",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "e7fd74ae-49a4-4bbe-9b34-bbae94a51de5"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "mission_name"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e6fd9519-bd9e-4584-93ee-eb70c57e142e",
                                                "path": "/latest",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "a6138613-5585-4426-908c-2ed2baf8e9c6"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "flight_number"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "Number"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e6fd9519-bd9e-4584-93ee-eb70c57e142e",
                                                "path": "/latest",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "ae544d7a-1334-45d1-a441-432b6f46bed1"
                            }
                        },
                        "sxv": "v32.0.0"
                    }
                ]
            }
        }
    },
    "24a0d841-24c5-4491-a08f-0a9f485d06a4": {
        "name": "LA Active Business",
        "description": {
            "table": {
                "steps": [
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "CITY"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "00d39c1d-47a9-4c30-bbf3-c599444d5bf6",
                                                "path": "/LosAngeles-OpenData/Active_Business/Listing_of_Active_Businesses.csv",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "39ef02e6-7adc-46fc-a60a-a764865100eb"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "BUSINESS NAME"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "00d39c1d-47a9-4c30-bbf3-c599444d5bf6",
                                                "path": "/LosAngeles-OpenData/Active_Business/Listing_of_Active_Businesses.csv",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "eae7bd41-35d3-400b-ba41-d7132662597a"
                            }
                        },
                        "sxv": "v32.0.0"
                    }
                ]
            }
        }
    },
    "da38eb59-8af6-4c98-bec6-05d7b0b6e363": {
        "name": "FDA Drugs",
        "description": {
            "table": {
                "steps": [
                    {
                        "act": {
                            "tag": "removeColumns",
                            "value": [
                                "f0e4c0fa-b686-4320-82c5-b005145c2d19"
                            ]
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "medicinalproduct"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "1cf07b17-51f2-4048-b186-0817975a2893"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "drugtreatmentduration"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "47d3a53d-340b-4854-83e8-bffacd70493e"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "drugstartdateformat"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "5d97af3a-0add-4968-9b62-e558bd57cf61"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "drugstartdate"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "cd0611d7-7fab-4a2b-a3d0-6eb6a569bf1c"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "drugenddateformat"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "f7938680-2d9e-4b64-86da-3a078158803a"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "drugenddate"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "044f3fee-af32-4893-8e37-4b5eaf9b95a8"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "drugdosagetext"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "1f2e6e94-7ad7-48cb-8ae8-c00b39557f1d"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "drugcharacterization"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "74ac401e-f577-4504-8246-e724636c1239"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "drugauthorizationnumb"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "025e1e8c-d725-4bf0-979b-5fac7d98b9d6"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "drugadministrationroute"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "355a12f9-21aa-4c83-bd52-68035c8e0dae"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Just",
                                                                                        "value": {
                                                                                            "tag": "atKey",
                                                                                            "value": {
                                                                                                "cursor": {
                                                                                                    "tag": "Just",
                                                                                                    "value": {
                                                                                                        "tag": "shiftArray",
                                                                                                        "value": {
                                                                                                            "tag": "Just",
                                                                                                            "value": {
                                                                                                                "tag": "shiftMap",
                                                                                                                "value": {
                                                                                                                    "tag": "Nothing"
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                                "key": "patient"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "key": "drug"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "medicinalproduct"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "9e4db1ae-dfdd-43b3-bc28-4f4195519def"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftMap",
                                                                        "value": {
                                                                            "tag": "Nothing"
                                                                        }
                                                                    }
                                                                },
                                                                "key": "last_updated"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "e3d41543-cf0d-4fbb-a900-e0b6264530ee",
                                                "path": "/event.json",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "f0e4c0fa-b686-4320-82c5-b005145c2d19"
                            }
                        },
                        "sxv": "v32.0.0"
                    }
                ]
            }
        }
    },
    "4552a571-47fc-4b62-91fc-1327102b9c74": {
        "name": "Covid API",
        "description": {
            "table": {
                "steps": [
                    {
                        "act": {
                            "tag": "removeColumns",
                            "value": [
                                "cc6036de-ffa0-45fa-bea9-0a03754992d3",
                                "d5db96a1-c308-4cb8-8283-72e6c4aa9dcf"
                            ]
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "Date"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "1c05223b-885c-4f2b-a8d4-6e6f304d39f2",
                                                "path": "/api.covid19api.com/summary",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "b7d95025-44ca-42e1-97b0-1ca298865088"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Nothing"
                                                                                    },
                                                                                    "key": "Countries"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "TotalRecovered"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "Number"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "1c05223b-885c-4f2b-a8d4-6e6f304d39f2",
                                                "path": "/api.covid19api.com/summary",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "5c718a88-cd11-43ae-8ec5-32ba272c22a1"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Nothing"
                                                                                    },
                                                                                    "key": "Countries"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "TotalDeaths"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "Number"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "1c05223b-885c-4f2b-a8d4-6e6f304d39f2",
                                                "path": "/api.covid19api.com/summary",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "133fa956-b83a-418e-8c78-b89c0cab0e9a"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Nothing"
                                                                                    },
                                                                                    "key": "Countries"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "TotalConfirmed"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "Number"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "1c05223b-885c-4f2b-a8d4-6e6f304d39f2",
                                                "path": "/api.covid19api.com/summary",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "a0d7521d-f83b-4e8f-9b7d-6205a5fba1a9"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Nothing"
                                                                                    },
                                                                                    "key": "Countries"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "NewRecovered"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "Number"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "1c05223b-885c-4f2b-a8d4-6e6f304d39f2",
                                                "path": "/api.covid19api.com/summary",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "2188a0fd-a5ea-4a0f-8c50-9d6a7f544fa0"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Nothing"
                                                                                    },
                                                                                    "key": "Countries"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "NewDeaths"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "Number"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "1c05223b-885c-4f2b-a8d4-6e6f304d39f2",
                                                "path": "/api.covid19api.com/summary",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "dcc8282c-8acf-4b55-8d69-bb84550d4c67"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Nothing"
                                                                                    },
                                                                                    "key": "Countries"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "Country"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "1c05223b-885c-4f2b-a8d4-6e6f304d39f2",
                                                "path": "/api.covid19api.com/summary",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "3ff80d03-e330-49c7-8099-87839b7c5687"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Nothing"
                                                                        }
                                                                    }
                                                                },
                                                                "key": "Slug"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "1c05223b-885c-4f2b-a8d4-6e6f304d39f2",
                                                "path": "/api.covid19api.com/countries",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "d5db96a1-c308-4cb8-8283-72e6c4aa9dcf"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Nothing"
                                                                        }
                                                                    }
                                                                },
                                                                "key": "Country"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "1c05223b-885c-4f2b-a8d4-6e6f304d39f2",
                                                "path": "/api.covid19api.com/countries",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "cc6036de-ffa0-45fa-bea9-0a03754992d3"
                            }
                        },
                        "sxv": "v32.0.0"
                    }
                ]
            }
        }
    },
    "b85f349b-aaaf-474b-8ee7-260e523f4d22": {
        "name": "Atlas-Sample-Companies",
        "description": {
            "table": {
                "steps": [
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Nothing"
                                                                                    },
                                                                                    "key": "offices"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "country_code"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "06016eb6-f7d6-4d23-a34a-e2eff14bdd8f"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Nothing"
                                                                                    },
                                                                                    "key": "offices"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "city"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "3d4e3eb4-7d38-457a-a713-c759f9e7e592"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Just",
                                                                    "value": {
                                                                        "tag": "shiftArray",
                                                                        "value": {
                                                                            "tag": "Just",
                                                                            "value": {
                                                                                "tag": "atKey",
                                                                                "value": {
                                                                                    "cursor": {
                                                                                        "tag": "Nothing"
                                                                                    },
                                                                                    "key": "offices"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "key": "address1"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "a464d099-6ef4-48ea-8f4d-33d61bc58b16"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "total_money_raised"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "46dbcab4-a557-4f29-82de-7e13b6a5bc7d"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "founded_year"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "Number"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "bfb2cdbb-147d-45ae-83a0-116fcda038dd"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "number_of_employees"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "Number"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "b316b142-6a73-41c9-a3a2-2e37ef082fd2"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "category_code"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "902c5725-b775-4337-af2a-2e55fe9c0fc5"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "twitter_username"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "d82ec513-5634-4073-ac96-68e185720ba7"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "crunchbase_url"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "557c7b76-5baf-4209-acba-95f7f944cb62"
                            }
                        },
                        "sxv": "v32.0.0"
                    },
                    {
                        "act": {
                            "tag": "addColumn",
                            "value": {
                                "alias": {
                                    "dynamic": ""
                                },
                                "content": {
                                    "tag": "pick",
                                    "value": {
                                        "tag": "extract",
                                        "value": {
                                            "interp": [],
                                            "proj": {
                                                "tag": "atType",
                                                "value": {
                                                    "cursor": {
                                                        "tag": "Just",
                                                        "value": {
                                                            "tag": "atKey",
                                                            "value": {
                                                                "cursor": {
                                                                    "tag": "Nothing"
                                                                },
                                                                "key": "name"
                                                            }
                                                        }
                                                    },
                                                    "scalar": "String"
                                                }
                                            },
                                            "resource": {
                                                "dataSource": "cb12ad6e-9903-4a36-b0cc-1130b10cbd4b",
                                                "path": "/sample_training/companies",
                                                "resourceType": "normal"
                                            }
                                        }
                                    }
                                },
                                "id": "cd69afd7-757d-4f9a-9e45-0686a477dda8"
                            }
                        },
                        "sxv": "v32.0.0"
                    }
                ]
            }
        }
    }
}
# convert into JSON:
y = x.json()

# the result is a JSON string:
