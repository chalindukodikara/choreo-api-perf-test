from faker import Faker
import uuid

fake = Faker()

def generate_component_kind(table_name):
    if table_name == "desired_store":
        return generate_component_kind_desired()
    return generate_component_kind_actual()

def generate_build_kind(table_name):
    if table_name == "desired_store":
        return generate_build_kind_desired()
    return generate_build_kind_actual()

def generate_deployment_kind(table_name):
    if table_name == "desired_store":
        return generate_deployment_kind_desired()
    return generate_deployment_kind_actual()

def generate_project_kind(table_name):
    if table_name == "desired_store":
        return generate_project_kind_desired()
    return generate_project_kind_actual()

def generate_component_kind_desired():
    component_name = fake.name()
    uuid_str = str(uuid.uuid4())
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Component",
        "metadata": {
            "name": component_name.lower().replace(' ', '_') + fake.word(),
            "projectName": fake.name().lower().replace(' ', '_'),
            "orgName": str(uuid.uuid4()),
            "displayName": component_name,
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
        }
    }
    return fake_data


def generate_build_kind_desired():
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Build",
        "metadata": {
            "name": fake.name().lower().replace(' ', '_'),
            "projectName": fake.name().lower().replace(' ', '_'),
            "deploymentTrackId": str(uuid.uuid4()),
            "orgName": str(uuid.uuid4()),
            "componentName": fake.name().lower().replace(' ', '_'),
            "labels": {
                "environment": fake.random_element(["Development", "Staging", "Production"])
            }
        },
        "spec": {
            "revision": str(uuid.uuid4())
        }
    }
    return fake_data



def generate_deployment_kind_desired():
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Deployment",
        "metadata": {
            "name": str(uuid.uuid4()),
            "projectName": fake.name().lower().replace(' ', '_'),
            "deploymentTrackId": str(uuid.uuid4()),
            "componentName": fake.name().lower().replace(' ', '_'),
            "orgName": str(uuid.uuid4()),
            "environment": fake.random_element(["Development", "Staging", "Production"])
        },
        "spec": {
            "buildRef": str(uuid.uuid4())
        }
    }
    return fake_data


def generate_project_kind_desired():
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Project",
        "metadata": {
            "name": fake.name().lower().replace(' ', '_'),
            "orgName": str(uuid.uuid4())
        },
        "spec": {
            "'type": fake.random_element(["mono-repo", "multi-repo"]),
            "owner": fake.name()
        }
    }
    return fake_data

def generate_component_kind_actual():
    component_name = fake.name()
    uuid_str = str(uuid.uuid4())
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Component",
        "metadata": {
            "name": component_name.lower().replace(' ', '_') + fake.word(),
            "projectName": fake.name().lower().replace(' ', '_'),
            "orgName": str(uuid.uuid4()),
            "displayName": component_name,
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
        "status": {
            "state": fake.random_element(["Completed", "Pending", "Failed", "Running"]),
            "completedAt": fake.date(),
        }
    }
    return fake_data


def generate_build_kind_actual():
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Build",
        "metadata": {
            "name": fake.name().lower().replace(' ', '_'),
            "projectName": fake.name().lower().replace(' ', '_'),
            "deploymentTrackId": str(uuid.uuid4()),
            "orgName": str(uuid.uuid4()),
            "componentName": fake.name().lower().replace(' ', '_'),
            "labels": {
                "environment": fake.random_element(["Development", "Staging", "Production"])
            }
        },
        "spec": {
            "revision": str(uuid.uuid4())
        },
        "status": {
            "state": fake.random_element(["Completed", "Pending", "Failed", "Running"]),
            "completedAt": fake.date(),
        }
    }
    return fake_data



def generate_deployment_kind_actual():
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Deployment",
        "metadata": {
            "name": str(uuid.uuid4()),
            "projectName": fake.name().lower().replace(' ', '_'),
            "deploymentTrackId": str(uuid.uuid4()),
            "componentName": fake.name().lower().replace(' ', '_'),
            "orgName": str(uuid.uuid4()),
            "environment": fake.random_element(["Development", "Staging", "Production"])
        },
        "spec": {
            "buildRef": str(uuid.uuid4())
        },
        "status": {
            "state": fake.random_element(["Completed", "Pending", "Failed", "Running"]),
            "completedAt": fake.date(),
            "runs": fake.random_int(min=1, max=1000)
        }
    }
    return fake_data


def generate_project_kind_actual():
    fake_data = {
        "apiVersion": "core.choreo.dev/v1alpha1",
        "kind": "Project",
        "metadata": {
            "name": fake.name().lower().replace(' ', '_'),
            "orgName": str(uuid.uuid4())
        },
         "spec": {
            "'type": fake.random_element(["mono-repo", "multi-repo"]),
            "owner": fake.name()
        },
        "status": {
            "state": fake.random_element(["Completed", "Pending", "Failed", "Running"]),
            "completedAt": fake.date()
        }
    }
    return fake_data
