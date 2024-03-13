from faker import Faker
import uuid

fake = Faker()

def generate_component_kind():
    component_name = fake.name()
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Component",
        "metadata": {
            "name": component_name.lower().replace(' ', '_'),
            "projectName": fake.word(),
            "displayName": component_name
        },
        "spec": {
            "type": fake.random_element(["miApiService", "miCronjob", "miJob", "miWebhook", "byocCronjob", 
                                          "byocJob", "byocWebApp", "byocService", "byocWebhook", 
                                          "byocWebAppsDockerfileLess", "buildpackCronjob", "buildpackWebApp", 
                                          "buildpackService", "buildpackTestRunner"]),
            "source": {
                "github": {
                    "repository": "https://github.com/example/choreo-samples/tree/main/hello-world",
                    "branch": "main",
                    "path": "hello-world"
                }
            },
            "build": {
                "default": {
                    "version": "1.x",
                    "port": str(fake.random_int(min=1, max=65535))
                }
            }
        },
        "level1": {
            "value1": fake.word(),
            "level2": {
                "value2": fake.word(),
                "level3": {
                    "value3": fake.word(),
                    "level4": {
                        "value4": fake.word(),
                        "level5": {
                            "value5": fake.word(),
                            "level6": {
                                "value6": fake.word(),
                                "level7": {
                                    "value7": fake.word(),
                                    "level8": {
                                        "value8": fake.word(),
                                        "level9": {
                                            "value9": fake.word(),
                                            "level10": {
                                                "value10": fake.word()
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return fake_data


def generate_build_kind():
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Build",
        "metadata": {
            "name": fake.name().lower().replace(' ', '_'),
            "projectName": fake.word(),
            "deploymentTrackId": str(uuid.uuid4()),
            "componentName": fake.name().lower().replace(' ', '_')
        },
        "spec": {
            "revision": str(uuid.uuid4())
        },
        "level1": {
            "value1": fake.word(),
            "level2": {
                "value2": fake.word(),
                "level3": {
                    "value3": fake.word(),
                    "level4": {
                        "value4": fake.word(),
                        "level5": {
                            "value5": fake.word(),
                            "level6": {
                                "value6": fake.word(),
                                "level7": {
                                    "value7": fake.word(),
                                    "level8": {
                                        "value8": fake.word(),
                                        "level9": {
                                            "value9": fake.word(),
                                            "level10": {
                                                "value10": fake.word()
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return fake_data



def generate_deployment_kind():
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Deployment",
        "metadata": {
            "name": str(uuid.uuid4()),
            "projectName": fake.word(),
            "deploymentTrackId": str(uuid.uuid4()),
            "componentName": fake.name().lower().replace(' ', '_'),
            "environment": fake.random_element(["Development", "Staging", "Production"])
        },
        "spec": {
            "buildRef": str(uuid.uuid4())
        },
        "level1": {
            "value1": fake.word(),
            "level2": {
                "value2": fake.word(),
                "level3": {
                    "value3": fake.word(),
                    "level4": {
                        "value4": fake.word(),
                        "level5": {
                            "value5": fake.word(),
                            "level6": {
                                "value6": fake.word(),
                                "level7": {
                                    "value7": fake.word(),
                                    "level8": {
                                        "value8": fake.word(),
                                        "level9": {
                                            "value9": fake.word(),
                                            "level10": {
                                                "value10": fake.word()
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return fake_data


def generate_project_kind():
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Project",
        "metadata": {
            "name": fake.name(),
            "orgName": fake.word()
        },
        "level1": {
            "value1": fake.word(),
            "level2": {
                "value2": fake.word(),
                "level3": {
                    "value3": fake.word(),
                    "level4": {
                        "value4": fake.word(),
                        "level5": {
                            "value5": fake.word(),
                            "level6": {
                                "value6": fake.word(),
                                "level7": {
                                    "value7": fake.word(),
                                    "level8": {
                                        "value8": fake.word(),
                                        "level9": {
                                            "value9": fake.word(),
                                            "level10": {
                                                "value10": fake.word()
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return fake_data
