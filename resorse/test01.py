import json
str_json = """
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "creationTimestamp": "2023-03-22T10:01:51Z",
                "generateName": "oncall-celery-7566dfdd45-",
                "labels": {
                    "app.kubernetes.io/component": "celery",
                    "app.kubernetes.io/instance": "oncall",
                    "app.kubernetes.io/name": "oncall",
                    "pod-template-hash": "7566dfdd45"
                },
                "name": "oncall-celery-7566dfdd45-gp2xb",
                "namespace": "grafana",
                "ownerReferences": [
                    {
                        "apiVersion": "apps/v1",
                        "blockOwnerDeletion": true,
                        "controller": true,
                        "kind": "ReplicaSet",
                        "name": "oncall-celery-7566dfdd45",
                        "uid": "4744a56a-3f1b-4374-a271-a4f8137f43d2"
                    }
                ],
                "resourceVersion": "156635372",
                "uid": "73b9482a-6bdd-4120-877a-00253261a4a5"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "./celery_with_exporter.sh"
                        ],
                        "env": [
                            {
                                "name": "CELERY_WORKER_QUEUE",
                                "value": "default,critical,long,slack,telegram,webhook,celery"
                            },
                            {
                                "name": "CELERY_WORKER_CONCURRENCY",
                                "value": "1"
                            },
                            {
                                "name": "CELERY_WORKER_MAX_TASKS_PER_CHILD",
                                "value": "100"
                            },
                            {
                                "name": "CELERY_WORKER_BEAT_ENABLED",
                                "value": "True"
                            },
                            {
                                "name": "CELERY_WORKER_SHUTDOWN_INTERVAL",
                                "value": "65m"
                            },
                            {
                                "name": "BASE_URL",
                                "value": "https://on-call.grafana.invitro.k8s"
                            },
                            {
                                "name": "SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "MIRAGE_SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_CIPHER_IV",
                                "value": "1234567890abcdef"
                            },
                            {
                                "name": "DJANGO_SETTINGS_MODULE",
                                "value": "settings.helm"
                            },
                            {
                                "name": "AMIXR_DJANGO_ADMIN_PATH",
                                "value": "admin"
                            },
                            {
                                "name": "OSS",
                                "value": "True"
                            },
                            {
                                "name": "UWSGI_LISTEN",
                                "value": "1024"
                            },
                            {
                                "name": "BROKER_TYPE",
                                "value": "rabbitmq"
                            },
                            {
                                "name": "GRAFANA_API_URL",
                                "value": "https://grafana.invitro.ru"
                            },
                            {
                                "name": "FEATURE_SLACK_INTEGRATION_ENABLED",
                                "value": "False"
                            },
                            {
                                "name": "FEATURE_TELEGRAM_INTEGRATION_ENABLED",
                                "value": "True"
                            },
                            {
                                "name": "TELEGRAM_WEBHOOK_HOST",
                                "value": "https://grafana.invitro.ru"
                            },
                            {
                                "name": "TELEGRAM_TOKEN",
                                "value": "6038133314:AAFaWUtZjii8-YMsnFd0IB1vv43Yxqk9s9Q"
                            },
                            {
                                "name": "FEATURE_EMAIL_INTEGRATION_ENABLED",
                                "value": "False"
                            },
                            {
                                "name": "MYSQL_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "MYSQL_PORT",
                                "value": "3306"
                            },
                            {
                                "name": "MYSQL_DB_NAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_USER",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "mariadb-root-password",
                                        "name": "oncall-mysql-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_USERNAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "RABBITMQ_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "rabbitmq-password",
                                        "name": "oncall-rabbitmq-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "RABBITMQ_PORT",
                                "value": "5672"
                            },
                            {
                                "name": "RABBITMQ_PROTOCOL",
                                "value": "amqp"
                            },
                            {
                                "name": "RABBITMQ_VHOST",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "REDIS_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "REDIS_PORT",
                                "value": "6379"
                            },
                            {
                                "name": "REDIS_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "redis-password",
                                        "name": "oncall-redis-external"
                                    }
                                }
                            }
                        ],
                        "image": "grafana/oncall:v1.1.41",
                        "imagePullPolicy": "Always",
                        "livenessProbe": {
                            "exec": {
                                "command": [
                                    "bash",
                                    "-c",
                                    "celery -A engine inspect ping -d celery@$HOSTNAME"
                                ]
                            },
                            "failureThreshold": 3,
                            "initialDelaySeconds": 30,
                            "periodSeconds": 300,
                            "successThreshold": 1,
                            "timeoutSeconds": 10
                        },
                        "name": "oncall",
                        "resources": {
                            "limits": {
                                "cpu": "1",
                                "memory": "1Gi"
                            },
                            "requests": {
                                "cpu": "200m",
                                "memory": "512Mi"
                            }
                        },
                        "securityContext": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-8875n",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
                "initContainers": [
                    {
                        "command": [
                            "sh",
                            "-c",
                            "until (python manage.py migrate --check); do echo Waiting for database migrations; sleep 2; done"
                        ],
                        "env": [
                            {
                                "name": "BASE_URL",
                                "value": "https://on-call.grafana.invitro.k8s"
                            },
                            {
                                "name": "SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "MIRAGE_SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_CIPHER_IV",
                                "value": "1234567890abcdef"
                            },
                            {
                                "name": "DJANGO_SETTINGS_MODULE",
                                "value": "settings.helm"
                            },
                            {
                                "name": "AMIXR_DJANGO_ADMIN_PATH",
                                "value": "admin"
                            },
                            {
                                "name": "OSS",
                                "value": "True"
                            },
                            {
                                "name": "UWSGI_LISTEN",
                                "value": "1024"
                            },
                            {
                                "name": "BROKER_TYPE",
                                "value": "rabbitmq"
                            },
                            {
                                "name": "GRAFANA_API_URL",
                                "value": "https://grafana.invitro.ru"
                            },
                            {
                                "name": "MYSQL_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "MYSQL_PORT",
                                "value": "3306"
                            },
                            {
                                "name": "MYSQL_DB_NAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_USER",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "mariadb-root-password",
                                        "name": "oncall-mysql-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_USERNAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "RABBITMQ_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "rabbitmq-password",
                                        "name": "oncall-rabbitmq-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "RABBITMQ_PORT",
                                "value": "5672"
                            },
                            {
                                "name": "RABBITMQ_PROTOCOL",
                                "value": "amqp"
                            },
                            {
                                "name": "RABBITMQ_VHOST",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "REDIS_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "REDIS_PORT",
                                "value": "6379"
                            },
                            {
                                "name": "REDIS_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "redis-password",
                                        "name": "oncall-redis-external"
                                    }
                                }
                            }
                        ],
                        "image": "grafana/oncall:v1.1.41",
                        "imagePullPolicy": "Always",
                        "name": "wait-for-db",
                        "resources": {},
                        "securityContext": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-8875n",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "nodeName": "sv-dck17",
                "preemptionPolicy": "PreemptLowerPriority",
                "priority": 0,
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "serviceAccount": "oncall",
                "serviceAccountName": "oncall",
                "terminationGracePeriodSeconds": 30,
                "tolerations": [
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/not-ready",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    },
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/unreachable",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    }
                ],
                "volumes": [
                    {
                        "name": "kube-api-access-8875n",
                        "projected": {
                            "defaultMode": 420,
                            "sources": [
                                {
                                    "serviceAccountToken": {
                                        "expirationSeconds": 3607,
                                        "path": "token"
                                    }
                                },
                                {
                                    "configMap": {
                                        "items": [
                                            {
                                                "key": "ca.crt",
                                                "path": "ca.crt"
                                            }
                                        ],
                                        "name": "kube-root-ca.crt"
                                    }
                                },
                                {
                                    "downwardAPI": {
                                        "items": [
                                            {
                                                "fieldRef": {
                                                    "apiVersion": "v1",
                                                    "fieldPath": "metadata.namespace"
                                                },
                                                "path": "namespace"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "status": {
                "conditions": [
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-03-22T10:02:23Z",
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-07-05T13:02:15Z",
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-07-05T13:02:15Z",
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-03-22T10:01:51Z",
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://62c62706e581ad901ad4fac61ab8f2530fa288c8ed1e7ef7dbdb726cb79b0ff0",
                        "image": "docker.io/grafana/oncall:v1.1.41",
                        "imageID": "docker.io/grafana/oncall@sha256:4542246bc1a1c2ea825bacc3b8b4352f2e6b71e7b1300528046231a640f9ea69",
                        "lastState": {
                            "terminated": {
                                "containerID": "containerd://c25e780456aa1d47ee05ccc882caeb80548027a10ff83ad050253488ba5bb0a1",
                                "exitCode": 0,
                                "finishedAt": "2023-07-05T13:02:13Z",
                                "reason": "Completed",
                                "startedAt": "2023-07-05T11:57:10Z"
                            }
                        },
                        "name": "oncall",
                        "ready": true,
                        "restartCount": 2364,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2023-07-05T13:02:14Z"
                            }
                        }
                    }
                ],
                "hostIP": "172.17.92.139",
                "initContainerStatuses": [
                    {
                        "containerID": "containerd://944f44c4b27dbe518977d54efc35d122af5ee94cbbc5ef61f1e904e34a634048",
                        "image": "docker.io/grafana/oncall:v1.1.41",
                        "imageID": "docker.io/grafana/oncall@sha256:4542246bc1a1c2ea825bacc3b8b4352f2e6b71e7b1300528046231a640f9ea69",
                        "lastState": {},
                        "name": "wait-for-db",
                        "ready": true,
                        "restartCount": 0,
                        "state": {
                            "terminated": {
                                "containerID": "containerd://944f44c4b27dbe518977d54efc35d122af5ee94cbbc5ef61f1e904e34a634048",
                                "exitCode": 0,
                                "finishedAt": "2023-03-22T10:02:22Z",
                                "reason": "Completed",
                                "startedAt": "2023-03-22T10:02:18Z"
                            }
                        }
                    }
                ],
                "phase": "Running",
                "podIP": "10.233.70.123",
                "podIPs": [
                    {
                        "ip": "10.233.70.123"
                    }
                ],
                "qosClass": "Burstable",
                "startTime": "2023-03-22T10:01:51Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "creationTimestamp": "2023-07-04T12:44:35Z",
                "generateName": "oncall-celery-7566dfdd45-",
                "labels": {
                    "app.kubernetes.io/component": "celery",
                    "app.kubernetes.io/instance": "oncall",
                    "app.kubernetes.io/name": "oncall",
                    "pod-template-hash": "7566dfdd45"
                },
                "name": "oncall-celery-7566dfdd45-t5992",
                "namespace": "grafana",
                "ownerReferences": [
                    {
                        "apiVersion": "apps/v1",
                        "blockOwnerDeletion": true,
                        "controller": true,
                        "kind": "ReplicaSet",
                        "name": "oncall-celery-7566dfdd45",
                        "uid": "4744a56a-3f1b-4374-a271-a4f8137f43d2"
                    }
                ],
                "resourceVersion": "156635375",
                "uid": "0ec846d7-7722-44d9-a208-1267cf1a4f89"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "./celery_with_exporter.sh"
                        ],
                        "env": [
                            {
                                "name": "CELERY_WORKER_QUEUE",
                                "value": "default,critical,long,slack,telegram,webhook,celery"
                            },
                            {
                                "name": "CELERY_WORKER_CONCURRENCY",
                                "value": "1"
                            },
                            {
                                "name": "CELERY_WORKER_MAX_TASKS_PER_CHILD",
                                "value": "100"
                            },
                            {
                                "name": "CELERY_WORKER_BEAT_ENABLED",
                                "value": "True"
                            },
                            {
                                "name": "CELERY_WORKER_SHUTDOWN_INTERVAL",
                                "value": "65m"
                            },
                            {
                                "name": "BASE_URL",
                                "value": "https://on-call.grafana.invitro.k8s"
                            },
                            {
                                "name": "SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "MIRAGE_SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_CIPHER_IV",
                                "value": "1234567890abcdef"
                            },
                            {
                                "name": "DJANGO_SETTINGS_MODULE",
                                "value": "settings.helm"
                            },
                            {
                                "name": "AMIXR_DJANGO_ADMIN_PATH",
                                "value": "admin"
                            },
                            {
                                "name": "OSS",
                                "value": "True"
                            },
                            {
                                "name": "UWSGI_LISTEN",
                                "value": "1024"
                            },
                            {
                                "name": "BROKER_TYPE",
                                "value": "rabbitmq"
                            },
                            {
                                "name": "GRAFANA_API_URL",
                                "value": "https://grafana.invitro.ru"
                            },
                            {
                                "name": "FEATURE_SLACK_INTEGRATION_ENABLED",
                                "value": "False"
                            },
                            {
                                "name": "FEATURE_TELEGRAM_INTEGRATION_ENABLED",
                                "value": "True"
                            },
                            {
                                "name": "TELEGRAM_WEBHOOK_HOST",
                                "value": "https://grafana.invitro.ru"
                            },
                            {
                                "name": "TELEGRAM_TOKEN",
                                "value": "6038133314:AAFaWUtZjii8-YMsnFd0IB1vv43Yxqk9s9Q"
                            },
                            {
                                "name": "FEATURE_EMAIL_INTEGRATION_ENABLED",
                                "value": "False"
                            },
                            {
                                "name": "MYSQL_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "MYSQL_PORT",
                                "value": "3306"
                            },
                            {
                                "name": "MYSQL_DB_NAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_USER",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "mariadb-root-password",
                                        "name": "oncall-mysql-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_USERNAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "RABBITMQ_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "rabbitmq-password",
                                        "name": "oncall-rabbitmq-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "RABBITMQ_PORT",
                                "value": "5672"
                            },
                            {
                                "name": "RABBITMQ_PROTOCOL",
                                "value": "amqp"
                            },
                            {
                                "name": "RABBITMQ_VHOST",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "REDIS_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "REDIS_PORT",
                                "value": "6379"
                            },
                            {
                                "name": "REDIS_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "redis-password",
                                        "name": "oncall-redis-external"
                                    }
                                }
                            }
                        ],
                        "image": "grafana/oncall:v1.1.41",
                        "imagePullPolicy": "Always",
                        "livenessProbe": {
                            "exec": {
                                "command": [
                                    "bash",
                                    "-c",
                                    "celery -A engine inspect ping -d celery@$HOSTNAME"
                                ]
                            },
                            "failureThreshold": 3,
                            "initialDelaySeconds": 30,
                            "periodSeconds": 300,
                            "successThreshold": 1,
                            "timeoutSeconds": 10
                        },
                        "name": "oncall",
                        "resources": {
                            "limits": {
                                "cpu": "1",
                                "memory": "1Gi"
                            },
                            "requests": {
                                "cpu": "200m",
                                "memory": "512Mi"
                            }
                        },
                        "securityContext": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-dbms7",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
                "initContainers": [
                    {
                        "command": [
                            "sh",
                            "-c",
                            "until (python manage.py migrate --check); do echo Waiting for database migrations; sleep 2; done"
                        ],
                        "env": [
                            {
                                "name": "BASE_URL",
                                "value": "https://on-call.grafana.invitro.k8s"
                            },
                            {
                                "name": "SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "MIRAGE_SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_CIPHER_IV",
                                "value": "1234567890abcdef"
                            },
                            {
                                "name": "DJANGO_SETTINGS_MODULE",
                                "value": "settings.helm"
                            },
                            {
                                "name": "AMIXR_DJANGO_ADMIN_PATH",
                                "value": "admin"
                            },
                            {
                                "name": "OSS",
                                "value": "True"
                            },
                            {
                                "name": "UWSGI_LISTEN",
                                "value": "1024"
                            },
                            {
                                "name": "BROKER_TYPE",
                                "value": "rabbitmq"
                            },
                            {
                                "name": "GRAFANA_API_URL",
                                "value": "https://grafana.invitro.ru"
                            },
                            {
                                "name": "MYSQL_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "MYSQL_PORT",
                                "value": "3306"
                            },
                            {
                                "name": "MYSQL_DB_NAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_USER",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "mariadb-root-password",
                                        "name": "oncall-mysql-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_USERNAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "RABBITMQ_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "rabbitmq-password",
                                        "name": "oncall-rabbitmq-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "RABBITMQ_PORT",
                                "value": "5672"
                            },
                            {
                                "name": "RABBITMQ_PROTOCOL",
                                "value": "amqp"
                            },
                            {
                                "name": "RABBITMQ_VHOST",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "REDIS_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "REDIS_PORT",
                                "value": "6379"
                            },
                            {
                                "name": "REDIS_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "redis-password",
                                        "name": "oncall-redis-external"
                                    }
                                }
                            }
                        ],
                        "image": "grafana/oncall:v1.1.41",
                        "imagePullPolicy": "Always",
                        "name": "wait-for-db",
                        "resources": {},
                        "securityContext": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-dbms7",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "nodeName": "sv-dck14",
                "preemptionPolicy": "PreemptLowerPriority",
                "priority": 0,
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "serviceAccount": "oncall",
                "serviceAccountName": "oncall",
                "terminationGracePeriodSeconds": 30,
                "tolerations": [
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/not-ready",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    },
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/unreachable",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    }
                ],
                "volumes": [
                    {
                        "name": "kube-api-access-dbms7",
                        "projected": {
                            "defaultMode": 420,
                            "sources": [
                                {
                                    "serviceAccountToken": {
                                        "expirationSeconds": 3607,
                                        "path": "token"
                                    }
                                },
                                {
                                    "configMap": {
                                        "items": [
                                            {
                                                "key": "ca.crt",
                                                "path": "ca.crt"
                                            }
                                        ],
                                        "name": "kube-root-ca.crt"
                                    }
                                },
                                {
                                    "downwardAPI": {
                                        "items": [
                                            {
                                                "fieldRef": {
                                                    "apiVersion": "v1",
                                                    "fieldPath": "metadata.namespace"
                                                },
                                                "path": "namespace"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "status": {
                "conditions": [
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-07-04T12:45:45Z",
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-07-05T13:02:16Z",
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-07-05T13:02:16Z",
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-07-04T12:44:35Z",
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://2f04402c0cc474638e3667c69e7e84f9b3a125d48b8093a88bc957d97389a7e0",
                        "image": "docker.io/grafana/oncall:v1.1.41",
                        "imageID": "docker.io/grafana/oncall@sha256:4542246bc1a1c2ea825bacc3b8b4352f2e6b71e7b1300528046231a640f9ea69",
                        "lastState": {
                            "terminated": {
                                "containerID": "containerd://a2d03a805826ecb7e8e430ba58eda00782f408167a7b3bc7c77824ddfff3718c",
                                "exitCode": 0,
                                "finishedAt": "2023-07-05T13:02:13Z",
                                "reason": "Completed",
                                "startedAt": "2023-07-05T11:57:11Z"
                            }
                        },
                        "name": "oncall",
                        "ready": true,
                        "restartCount": 23,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2023-07-05T13:02:15Z"
                            }
                        }
                    }
                ],
                "hostIP": "172.17.92.136",
                "initContainerStatuses": [
                    {
                        "containerID": "containerd://3e845a6410a2832bf5426c4c0ffe6d74e4afae7aa69ebd31da9130c648aa7493",
                        "image": "docker.io/grafana/oncall:v1.1.41",
                        "imageID": "docker.io/grafana/oncall@sha256:4542246bc1a1c2ea825bacc3b8b4352f2e6b71e7b1300528046231a640f9ea69",
                        "lastState": {},
                        "name": "wait-for-db",
                        "ready": true,
                        "restartCount": 0,
                        "state": {
                            "terminated": {
                                "containerID": "containerd://3e845a6410a2832bf5426c4c0ffe6d74e4afae7aa69ebd31da9130c648aa7493",
                                "exitCode": 0,
                                "finishedAt": "2023-07-04T12:45:45Z",
                                "reason": "Completed",
                                "startedAt": "2023-07-04T12:45:41Z"
                            }
                        }
                    }
                ],
                "phase": "Running",
                "podIP": "10.233.68.215",
                "podIPs": [
                    {
                        "ip": "10.233.68.215"
                    }
                ],
                "qosClass": "Burstable",
                "startTime": "2023-07-04T12:44:35Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/restartedAt": "2023-04-19T13:44:05Z"
                },
                "creationTimestamp": "2023-04-19T13:44:05Z",
                "generateName": "oncall-engine-b49c7498b-",
                "labels": {
                    "app.kubernetes.io/component": "engine",
                    "app.kubernetes.io/instance": "oncall",
                    "app.kubernetes.io/name": "oncall",
                    "pod-template-hash": "b49c7498b"
                },
                "name": "oncall-engine-b49c7498b-gpkfp",
                "namespace": "grafana",
                "ownerReferences": [
                    {
                        "apiVersion": "apps/v1",
                        "blockOwnerDeletion": true,
                        "controller": true,
                        "kind": "ReplicaSet",
                        "name": "oncall-engine-b49c7498b",
                        "uid": "ece53268-e607-4c60-b4c2-fa4d8ae87a7e"
                    }
                ],
                "resourceVersion": "117456842",
                "uid": "d518c4b5-a9ee-4cc3-acac-4875f0ac512c"
            },
            "spec": {
                "containers": [
                    {
                        "env": [
                            {
                                "name": "BASE_URL",
                                "value": "https://on-call.grafana.invitro.k8s"
                            },
                            {
                                "name": "SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "MIRAGE_SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_CIPHER_IV",
                                "value": "1234567890abcdef"
                            },
                            {
                                "name": "DJANGO_SETTINGS_MODULE",
                                "value": "settings.helm"
                            },
                            {
                                "name": "AMIXR_DJANGO_ADMIN_PATH",
                                "value": "admin"
                            },
                            {
                                "name": "OSS",
                                "value": "True"
                            },
                            {
                                "name": "UWSGI_LISTEN",
                                "value": "1024"
                            },
                            {
                                "name": "BROKER_TYPE",
                                "value": "rabbitmq"
                            },
                            {
                                "name": "GRAFANA_API_URL",
                                "value": "https://grafana.invitro.ru"
                            },
                            {
                                "name": "FEATURE_SLACK_INTEGRATION_ENABLED",
                                "value": "False"
                            },
                            {
                                "name": "FEATURE_TELEGRAM_INTEGRATION_ENABLED",
                                "value": "True"
                            },
                            {
                                "name": "TELEGRAM_WEBHOOK_HOST",
                                "value": "https://grafana.invitro.ru"
                            },
                            {
                                "name": "TELEGRAM_TOKEN",
                                "value": "6038133314:AAFaWUtZjii8-YMsnFd0IB1vv43Yxqk9s9Q"
                            },
                            {
                                "name": "FEATURE_EMAIL_INTEGRATION_ENABLED",
                                "value": "False"
                            },
                            {
                                "name": "MYSQL_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "MYSQL_PORT",
                                "value": "3306"
                            },
                            {
                                "name": "MYSQL_DB_NAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_USER",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "mariadb-root-password",
                                        "name": "oncall-mysql-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_USERNAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "RABBITMQ_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "rabbitmq-password",
                                        "name": "oncall-rabbitmq-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "RABBITMQ_PORT",
                                "value": "5672"
                            },
                            {
                                "name": "RABBITMQ_PROTOCOL",
                                "value": "amqp"
                            },
                            {
                                "name": "RABBITMQ_VHOST",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "REDIS_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "REDIS_PORT",
                                "value": "6379"
                            },
                            {
                                "name": "REDIS_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "redis-password",
                                        "name": "oncall-redis-external"
                                    }
                                }
                            }
                        ],
                        "image": "grafana/oncall:v1.1.41",
                        "imagePullPolicy": "Always",
                        "livenessProbe": {
                            "failureThreshold": 3,
                            "httpGet": {
                                "path": "/health/",
                                "port": "http",
                                "scheme": "HTTP"
                            },
                            "periodSeconds": 60,
                            "successThreshold": 1,
                            "timeoutSeconds": 3
                        },
                        "name": "oncall",
                        "ports": [
                            {
                                "containerPort": 8080,
                                "name": "http",
                                "protocol": "TCP"
                            }
                        ],
                        "readinessProbe": {
                            "failureThreshold": 3,
                            "httpGet": {
                                "path": "/ready/",
                                "port": "http",
                                "scheme": "HTTP"
                            },
                            "periodSeconds": 60,
                            "successThreshold": 1,
                            "timeoutSeconds": 3
                        },
                        "resources": {
                            "limits": {
                                "cpu": "1",
                                "memory": "1Gi"
                            },
                            "requests": {
                                "cpu": "200m",
                                "memory": "512Mi"
                            }
                        },
                        "securityContext": {},
                        "startupProbe": {
                            "failureThreshold": 3,
                            "httpGet": {
                                "path": "/startupprobe/",
                                "port": "http",
                                "scheme": "HTTP"
                            },
                            "periodSeconds": 60,
                            "successThreshold": 1,
                            "timeoutSeconds": 3
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-vzjxk",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
                "initContainers": [
                    {
                        "command": [
                            "sh",
                            "-c",
                            "until (python manage.py migrate --check); do echo Waiting for database migrations; sleep 2; done"
                        ],
                        "env": [
                            {
                                "name": "BASE_URL",
                                "value": "https://on-call.grafana.invitro.k8s"
                            },
                            {
                                "name": "SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_SECRET_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "MIRAGE_SECRET_KEY",
                                        "name": "oncall"
                                    }
                                }
                            },
                            {
                                "name": "MIRAGE_CIPHER_IV",
                                "value": "1234567890abcdef"
                            },
                            {
                                "name": "DJANGO_SETTINGS_MODULE",
                                "value": "settings.helm"
                            },
                            {
                                "name": "AMIXR_DJANGO_ADMIN_PATH",
                                "value": "admin"
                            },
                            {
                                "name": "OSS",
                                "value": "True"
                            },
                            {
                                "name": "UWSGI_LISTEN",
                                "value": "1024"
                            },
                            {
                                "name": "BROKER_TYPE",
                                "value": "rabbitmq"
                            },
                            {
                                "name": "GRAFANA_API_URL",
                                "value": "https://grafana.invitro.ru"
                            },
                            {
                                "name": "MYSQL_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "MYSQL_PORT",
                                "value": "3306"
                            },
                            {
                                "name": "MYSQL_DB_NAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_USER",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "MYSQL_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "mariadb-root-password",
                                        "name": "oncall-mysql-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_USERNAME",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "RABBITMQ_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "rabbitmq-password",
                                        "name": "oncall-rabbitmq-external"
                                    }
                                }
                            },
                            {
                                "name": "RABBITMQ_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "RABBITMQ_PORT",
                                "value": "5672"
                            },
                            {
                                "name": "RABBITMQ_PROTOCOL",
                                "value": "amqp"
                            },
                            {
                                "name": "RABBITMQ_VHOST",
                                "value": "grafana_oncall"
                            },
                            {
                                "name": "REDIS_HOST",
                                "value": "sv-mt03.invitro.ru"
                            },
                            {
                                "name": "REDIS_PORT",
                                "value": "6379"
                            },
                            {
                                "name": "REDIS_PASSWORD",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "key": "redis-password",
                                        "name": "oncall-redis-external"
                                    }
                                }
                            }
                        ],
                        "image": "grafana/oncall:v1.1.41",
                        "imagePullPolicy": "Always",
                        "name": "wait-for-db",
                        "resources": {},
                        "securityContext": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-vzjxk",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "nodeName": "sv-dck17",
                "preemptionPolicy": "PreemptLowerPriority",
                "priority": 0,
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "serviceAccount": "oncall",
                "serviceAccountName": "oncall",
                "terminationGracePeriodSeconds": 30,
                "tolerations": [
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/not-ready",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    },
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/unreachable",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    }
                ],
                "volumes": [
                    {
                        "name": "kube-api-access-vzjxk",
                        "projected": {
                            "defaultMode": 420,
                            "sources": [
                                {
                                    "serviceAccountToken": {
                                        "expirationSeconds": 3607,
                                        "path": "token"
                                    }
                                },
                                {
                                    "configMap": {
                                        "items": [
                                            {
                                                "key": "ca.crt",
                                                "path": "ca.crt"
                                            }
                                        ],
                                        "name": "kube-root-ca.crt"
                                    }
                                },
                                {
                                    "downwardAPI": {
                                        "items": [
                                            {
                                                "fieldRef": {
                                                    "apiVersion": "v1",
                                                    "fieldPath": "metadata.namespace"
                                                },
                                                "path": "namespace"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "status": {
                "conditions": [
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-04-19T13:44:13Z",
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-04-19T13:45:06Z",
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-04-19T13:45:06Z",
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2023-04-19T13:44:05Z",
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://b0722e3aa9d7bbdfd6b3f13a4655ec6c1a4c47975918052e73450fb7567beb40",
                        "image": "docker.io/grafana/oncall:v1.1.41",
                        "imageID": "docker.io/grafana/oncall@sha256:4542246bc1a1c2ea825bacc3b8b4352f2e6b71e7b1300528046231a640f9ea69",
                        "lastState": {},
                        "name": "oncall",
                        "ready": true,
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2023-04-19T13:44:14Z"
                            }
                        }
                    }
                ],
                "hostIP": "172.17.92.139",
                "initContainerStatuses": [
                    {
                        "containerID": "containerd://9168bed3f9ae1c11d1e7acb3d0f1489a65edaf62991bc859f40ffdfc4623eb2d",
                        "image": "docker.io/grafana/oncall:v1.1.41",
                        "imageID": "docker.io/grafana/oncall@sha256:4542246bc1a1c2ea825bacc3b8b4352f2e6b71e7b1300528046231a640f9ea69",
                        "lastState": {},
                        "name": "wait-for-db",
                        "ready": true,
                        "restartCount": 0,
                        "state": {
                            "terminated": {
                                "containerID": "containerd://9168bed3f9ae1c11d1e7acb3d0f1489a65edaf62991bc859f40ffdfc4623eb2d",
                                "exitCode": 0,
                                "finishedAt": "2023-04-19T13:44:12Z",
                                "reason": "Completed",
                                "startedAt": "2023-04-19T13:44:07Z"
                            }
                        }
                    }
                ],
                "phase": "Running",
                "podIP": "10.233.70.147",
                "podIPs": [
                    {
                        "ip": "10.233.70.147"
                    }
                ],
                "qosClass": "Burstable",
                "startTime": "2023-04-19T13:44:05Z"
            }
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": "",
        "selfLink": ""
    }
}
"""
data = json.loads(str_json)
print(data)