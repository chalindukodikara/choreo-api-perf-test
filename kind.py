from faker import Faker
import time

fake = Faker()

def generate_component_kind():
    component_name = fake.name()
    unique_value = int(time.time() * 1000)
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Component",
        "metadata": {
            "name": component_name.lower().replace(' ', '_') + f"_{unique_value}",
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
